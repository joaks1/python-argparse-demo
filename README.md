A simple demo and exercise using the `argparse` module in Python.


# Getting set up

At this point, you should have
(1) an account on [Github](https://github.com/) and
(2) been introduced to the very basics of [Git](https://git-scm.com/).

1.  Login to your [Github](https://github.com/) account.

1.  Fork [this repository](https://github.com/joaks1/python-argparse-demo), by
    clicking the 'Fork' button on the upper right of the page.

    After a few seconds, you should be looking at *your* 
    copy of the repo in your own Github account.

1.  Click the 'Clone or download' button, and copy the URL of the repo via the
    'copy to clipboard' button.

1.  In your terminal, navigate to where you want to keep this repo (you can
    always move it later, so just your home directory is fine). Then type:

        $ git clone the-url-you-just-copied

    and hit enter to clone the repository. Make sure you are cloning **your**
    fork of this repo.

1.  Next, `cd` into the directory:

        $ cd the-name-of-directory-you-just-cloned

1.  At this point, you should be in your own local copy of the repository.

1.  As you work on the exercise below, be sure to frequently `add` and `commit`
    your work and `push` changes to the *remote* copy of the repo hosted on
    GitHub. Don't enter these commands now; this is just to jog your memory:

        $ # Do some work
        $ git add file-you-worked-on.py
        $ git commit
        $ git push origin master


# Types of command-line arguments

Before we get into parsing command-line arguments with argparse,
let's first talk about two types of command-line arguments:
**Keyword** and **positional** command-line arguments.
For example, on the command line, when we type:

```bash
ls --sort=time $HOME
```

`$HOME` is a positional argument, and `--sort=time` is an optional keyword
argument.
A positional argument is an argument provided after the
name of the program, that does not have an option flag associated with it.
Because there is no flag for the argument, its identity is determined by its
position (like `$HOME` in the above example).

A keyword argument is also provided after the name of program, but has
a keyword flag to identify it.
In our example above, the `time` argument was identified by the `--sort`
keyword flag, so the `ls` program knows we want to sort the list of
files/directories in our home folder by time.


# Intro to argparse

Python's `argparse` module provides flexible ways of handling
command-line arguments within your own scripts.
Let's go over the basic workflow of using `argparse`.
Much of the example code snippets below are in the `demo.py` script in this
directory (folder).
So, you might find it helpful to have `demo.py` open while you read through the
steps below.

## 1. Import the argparse module

```python
import argparse
```

## 2. Create an ArgumentParser object

After importing `argparse`, you create an instance of the `ArgumentParser`
class.
For example:

```python
parser = argparse.ArgumentParser()
```

You can provide arguments when creating the `ArgumentParser`.
For example, I often like to specify a `formatter_class` that includes default
values for command-line options in the help menu:

```python
parser = argparse.ArgumentParser(
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
)
```

## 3. Add command-line arguments

With the `ArgumentParser` object "in hand", we can easily add command-line
arguments we need for our script.
These arguments could be numbers, strings, boolean options, or paths to files.
Let's look at some examples.

### 3.1. Add a positional argument

Let's assume our script needs an input file.
We can use our ArgumentParser object called `parser` to easily add
a positional argument for the file:

```python
parser.add_argument(
    "file_path",
    type = str,
    metavar = "FILE-PATH",
    help = "A path to a file.",
)
```

In the example above:

-   `"file_path"` will be the key we use to access the argument provided on the
    command line within our script (see Step 5 below)
-   `type = str` tells `argparse` what type of object the command-line argument
    should be converted into
-   `metavar = "FILE-PATH"` is the placeholder name for this argument shown in
    the help menu that `argparse` automatically creates for our script
-   `help = ...` is the text provided in the help menu `argparse` automatically
    creates for our script

By default, positional arguments will be required for our script.
If our script is run without the positional argument, `argparse` will create
a helpful error message for us.
For example, the `demo.py` script in this directory (folder) expects one or
more positional arguments.
Try running it without any positional arguments:

```python
python3 demo.py
```

You should get an error message like:

    usage: demo.py [-h] [-n NUMBER] [-t THRESHOLD] [-c] FILE-PATH [FILE-PATH ...]
    demo.py: error: the following arguments are required: FILE-PATH

If you look in the `demo.py` file, you will not find any code that produces the
message above.
`argparse` did that for us.

If we want our script to handle one or more files, we can change our
`add_argument` above to:

```python
parser.add_argument(
    "file_path",
    type = str,
    metavar = "FILE-PATH",
    help = "A path to a file.",
    nargs = "+",
)
```

The `nargs = "+"` tells `argparse` that we require at least one file, but there
might be more.

### 3.2. Add keyword arguments

Let's assume our script uses a number that is an integer, and we want to allow
the value of that number to be specified on the command line.
We can easily add an argument to our command-line interface to handle this:

```python
parser.add_argument(
    "-n", "--number",
    type = int,
    default = 1,
    help = "An integer.",
)
```

Let's break down the parts of this `.add_argument` call:

-   The first two arguments ("-n" and "--number") specify how this keyword
    argument is identified on the command line.
    For example, someone can provide a number to our script using

        python3 demo.py -n 3 ...

    or

        python3 demo.py --number=3 ...

    Also, `--number` also specifies the key we use to access the argument
    within our script. The dashes are removed and we will use `number` as the
    key to access the value; more on this in Step 5 below.

-   `type = int` tells `argparse` what type of object the command-line argument
    will be converted into; an `int` in this case.

-   `default = 1` creates a default value for this argument. So, if it is not
    provided on the command line, the value will default to 1 in this example.

-   `help = ...` is the text provided in the help menu `argparse` automatically
    creates for our script.

Let's assume our script also uses a floating-point number as a threshold value
for something.
We can add an argument to our command-line interface so that the value of this
threshold can be specified on the command line:

```python
parser.add_argument(
    "-t", "--threshold",
    type = float,
    default = 3.4,
    help = "A super duper important threshold.",
)
```

Lastly, let's assume we want to enable a boolean option to our script to turn
on a feature.
We can add a boolean option using `argparse` like:

```python
parser.add_argument(
    "-c", "--i-am-cool",
    default = False,
    action = "store_true",
    help = "An example of a boolean option.",
)
```

This tells `argparse` that if we see `-c` or `--i-am-cool` as a command-line
argument, we want the `i_am_cool` key (first two hyphens removed and the others
converted to underscores) to be `True`. Otherwise, by default, `i_am_cool` will
be `False`.

## 4. Parse the command-line arguments provided to our script

After telling the `parser` object all the command-line option we want our
script to support, then we tell it to parse those options from the
command-line:

```python
args = parser.parse_args()
```

This returns a `dict`-like object that we gave the variable name `args`. We can
now use the `args` object to access the values of the arguments provided on the
command-line (or the default values if some optional arguments were not
provided on the command line).

## 5. Access the argument values

We can use "dot" syntax to access the values of the arguments from our `args`
object.
For example, in our script, we can now access the value of the threshold
argument using `args.threshold`.
This is true for all the arguments.
For example, in our script we can do something like:

```python
print("Number:", args.number)
print("Threshold:", args.threshold)
print("I am cool?", args.i_am_cool)
```

Note, that for the keyword flag that had hyphens, `--i-am-cool`, these have
been converted to underscores so that they are a valid Python variable name.

# Try out demo.py

The `demo.py` script in this directory (folder) contains much of the code
examples from above.
Open it with your favorite text editor and look it over,
and then try it out on the command line.
First, use this command to check out the help menu `argparse` automatically
creates for us:

    python3 demo.py -h
    usage: demo.py [-h] [-n NUMBER] [-t THRESHOLD] [-c] FILE-PATH [FILE-PATH ...]
    
    positional arguments:
      FILE-PATH             A path to a file.
    
    options:
      -h, --help            show this help message and exit
      -n, --number NUMBER   An integer. (default: 1)
      -t, --threshold THRESHOLD
                            A super duper important threshold. (default: 3.4)
      -c, --i-am-cool       A boolean option. (default: False)

Note, `python demo.py --help` will also work.

Next, try out some of the options and look at how the outputs change.
Some examples:

    python3 demo.py -n 3 dummy-path.txt
    The args after being processed by the argparse parser object:
     Namespace(file_path=['dummy-path.txt'], number=3, threshold=3.4, i_am_cool=False)
    Paths: ['dummy-path.txt']
    Number: 3
    Threshold: 3.4
    I am cool? False

    python3 demo.py --threshold 5.5 --i-am-cool dummy-path.txt
    The args after being processed by the argparse parser object:
     Namespace(file_path=['dummy-path.txt'], number=1, threshold=5.5, i_am_cool=True)
    Paths: ['dummy-path.txt']
    Number: 1
    Threshold: 5.5
    I am cool? True

## argparse will handle common errors for us

Because we told `argparse` the `type` for each argument, it will handle common
errors for us.

For example, try:

    python3 demo.py --number 5.5 --i-am-cool dummy-path.txt
    usage: demo.py [-h] [-n NUMBER] [-t THRESHOLD] [-c] FILE-PATH [FILE-PATH ...]
    demo.py: error: argument -n/--number: invalid int value: '5.5'

Because we told `argpare` that `number` should be an integer, it throws an
error if something else is provided on the command line.
That saves us from a lot of sanity checking of inputs within our script; nice!


# Exercise

For this exercise, you will be adding one more command-line argument to
`demo.py`.
Use the `parser.add_argument` method to add an optional keyword argument with
the short and long flags "-q" and "--quiet".
When this option is given on the command line, the `demo.py` script should not
print its normal output, but rather output "Shhh. Be vewy, vewy quiet, I'm
hunting wabbits...".

If successful, your modified `demo.py` script should behave like this:

    python3 demo.py dummy-path.txt
    The args after being processed by the argparse parser object:
     Namespace(file_path=['dummy-path.txt'], number=1, threshold=3.4, i_am_cool=False, quiet=False)
    Paths: ['dummy-path.txt']
    Number: 1
    Threshold: 3.4
    I am cool? False

And:

    python3 demo.py --quiet dummy-path.txt
    Shhh. Be vewy, vewy quiet, I'm hunting wabbits...


# Additional resources

For more about `argparse` here's the documentation and the tutorial:

-   Docs: <https://docs.python.org/3/library/argparse.html>
-   Tutorial: <https://docs.python.org/3/howto/argparse.html>


# Acknowledgments

This work was made possible by funding provided to [Jamie
Oaks](http://phyletica.org) from the National Science Foundation (DEB 1656004).


# License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US">Creative Commons Attribution 4.0 International License</a>.

<h1>Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#math" data-toc-modified-id="math-1">math</a></span></li><li><span><a href="#os" data-toc-modified-id="os-2">os</a></span><ul class="toc-item"><li><span><a href="#Working-directory" data-toc-modified-id="Working-directory-2.1">Working directory</a></span></li><li><span><a href="#Paths" data-toc-modified-id="Paths-2.2">Paths</a></span><ul class="toc-item"><li><span><a href="#Absolute-paths" data-toc-modified-id="Absolute-paths-2.2.1">Absolute paths</a></span></li><li><span><a href="#Relative-paths" data-toc-modified-id="Relative-paths-2.2.2">Relative paths</a></span></li></ul></li></ul></li><li><span><a href="#Third-party-packages" data-toc-modified-id="Third-party-packages-3">Third-party packages</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-4">Exercises</a></span><ul class="toc-item"><li><span><a href="#1" data-toc-modified-id="1-4.1">1</a></span></li><li><span><a href="#2" data-toc-modified-id="2-4.2">2</a></span></li></ul></li></ul></div>

# The standard library

In the [previous lesson](modules.md), we saw that Python programs can [import](extras/glossary.md#import) some of their components from other files. Such additional files that are not in themselves programs but instead provide *components* for programs are known as [modules](extras/glossary.md#module).

We started out by writing our own modules, to see how the whole idea works. But we can also import modules that we get from elsewhere. For even moderately complex programs, we will almost always need to import and use some additional components that we did not write ourselves. If we start work on a new task and we find that it cannot easily be accomplished using the basic operations and data types, or if we don't even know how to begin, then we should ask ourselves: Is this a task that lots of other people will probably have needed to do before? If it is, then we might be able to save ourselves some time by searching first for a pre-made module that provides some of the building blocks that we need.

We might find that we first need to download and install some of the modules that we decide we want to use. But in many cases this is not necessary. A standard Python installation comes with a large collection of pre-made modules for many common programming tasks. This collection of modules that is already included when we install Python is known as the 'standard library'. The term 'library' is used here to indicate that, like the knowledge stored in a library, the contents of these extra modules are not immediately available to us, but can be accessed by going to the library and 'reading in' one of the 'books'. The Python language is organized so as to provide only the very basics at its core: a few [built-in functions](extras/glossary.md#builtin), mathematical [operators](extras/glossary.md#operator), the most useful [data types](extras/glossary.md#type), and some [control statements](extras/glossary.md#control) (there are admittedly a *few* more things than just these, but we won't look at many more of them in this class). The core of the language is kept small and simple, and programmers only bring in as much of the extras as they need for a given task.

So what extra modules are contained in the standard library? You can find a full list of them at the official Python documentation pages [here](https://docs.python.org/3/library/), but this is a little overwhelming to read all at once. Instead of going through them exhaustively, we will just consider some examples of how to use them. In future lessons, we will meet more modules from the standard library that are useful for specific tasks.

Let's set ourselves two example tasks, each of which will require a module from the standard library. The first is fairly short and straightforward, the second a bit more complex.

## math

Here is our first task:

* We want to create a new module for working with circles.
* The module should provide two functions:
  * Calculate the circumference of a circle given its radius.
  * Calculate the area of a circle given its radius.

The relevant formulas relating a circle's circumference $C$ and area $A$ to its radius are:

$$
C = 2 \pi r
$$

$$
A = \pi r^2
$$


Both of these involve the mathematical constant [*pi*](https://en.wikipedia.org/wiki/Pi) ($\pi$). How do we build it into our module?

We could of course go ahead and define a suitable approximation to *pi* ourselves:


```python
pi = 3.14159265359
```

But the digits of *pi* go on forever, so we will need to type them out for quite a long time before reaching the closest approximation that our computer can store.

If you ever find yourself muttering at your computer "There has *got* to be a better way of doing this," this is usually a sign that there is a ready-made solution out there somewhere, either in Python's standard library, or in some other module that somebody else has already written. If you head to Google and search for 'Python pi' you will find that the first few results mention the `math` module. `math` is a module in Python's standard library that provides some additional mathematical functions, as well as constants like *pi* or *[e](https://en.wikipedia.org/wiki/E_(mathematical_constant))*.

We can [import](extras/glossary.md#import) a module from the standard library in just the same way as importing a module that we wrote ourselves. The only difference is that we don't need to make sure that we have the module file ready in the same directory as our main program; modules from the standard library can be imported from anywhere regardless of which directory we are working in.

So let's begin by importing the `math` module:


```python
import math
```

As we have seen before, if we encounter a new module, we can use the `dir()` function in the console to see its contents.


```python
dir(math)
```




    ['__doc__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'acos',
     'acosh',
     'asin',
     'asinh',
     'atan',
     'atan2',
     'atanh',
     'ceil',
     'copysign',
     'cos',
     'cosh',
     'degrees',
     'e',
     'erf',
     'erfc',
     'exp',
     'expm1',
     'fabs',
     'factorial',
     'floor',
     'fmod',
     'frexp',
     'fsum',
     'gamma',
     'gcd',
     'hypot',
     'inf',
     'isclose',
     'isfinite',
     'isinf',
     'isnan',
     'ldexp',
     'lgamma',
     'log',
     'log10',
     'log1p',
     'log2',
     'modf',
     'nan',
     'pi',
     'pow',
     'radians',
     'sin',
     'sinh',
     'sqrt',
     'tan',
     'tanh',
     'tau',
     'trunc']



The names of many of its contents may be familiar to you from math class. We see that `pi` is in there.

Let's remind ourselves of the [syntax](extras/glossary.md#syntax) for using something from an imported module. We need the name of the module, then `.`, then the name of whatever it is we want to use from it:


```python
math.pi
```




    3.141592653589793



Note that `math.pi` is a variable, not a function, so we don't place any parentheses after it. We have so far just been getting functions from modules, and often most of the contents of a module will be functions, but there is no reason that modules cannot also store variables. The output of `dir()` doesn't tell us which of the contents of a module are functions and which are variables, but if we are unsure about any of them we can check their [type](extras/glossary.md#type):


```python
type(math.pi)
```




    float




```python
type(math.sqrt)
```




    builtin_function_or_method



Now we can use `math.pi` like any other variable. For example:


```python
radius = 10

circumference = 2 * math.pi * radius

print(circumference)
```

    62.83185307179586


That's it. Now that we know how to import the `math` module and use its contents in calculations, we know everything we need in order to write our target program. Go ahead and try to write the 'circle' module yourself, then take a look at it in the example file [circle.py](examples/circle.py). If you need to remind yourself about writing modules, take a look back at the [lesson on modules](modules.md).

Here is our module in action:


```python
import circle

circle.circumference(10)
```




    62.83185307179586




```python
circle.area(10)
```




    314.1592653589793



## os

That was a very short introduction to using the standard library. Our next task is a little more complex. Here it is:

* We are preparing to organize our tax returns for the last five years and would like to generate a folder structure in which to store them.
* We need one folder for each of the last five years.
* Inside each of those year folders, we would like a separate folder for each month.

How do we even make new folders in Python? We don't know. But we head over to Google and search for 'Python make new folder' and see that the first few results all mention the `os` module.

`os` is another module from Python's standard library. The letters 'OS' stand for [Operating System](extras/glossary.md#os), and the `os` module handles various tasks that involve interacting with the operating system of a computer, primarily with its system of files and folders. `os` is probably the most commonly-used module from the standard library. Once we go beyond the simplest programs, we will almost always need to use the computer's file system to locate or create files.

Let's import it.


```python
import os
```

We won't `dir()` the `os` module here, simply because it contains *a lot* of things. But if you like you can go to the console in Spyder and type in `dir(os)` to see the full list of contents (make sure you have first typed in `import os` so that you too have imported the `os` module).

The functions from `os` that are relevant for our task are `os.mkdir()` and `os.makedirs()`. As their (somewhat abbreviated) names suggest, these functions are for making new directories (and [directory](extras/glossary.md#directory) is just a more technical-sounding term for a 'folder' in a computer's file system).

Let's use `os.mkdir()`, which creates a single new directory, to make an example new directory, just to test it out:


```python
os.mkdir('my_new_directory')
```

If you enter this command in your Spyder console, you should then be able to go to your file explorer, find whatever directory you are working in in Spyder, and see that a new directory called 'my_new_directory' has been created there.

And in case you are not even sure what directory you are working in, `os` provides a function `os.getcwd()` for finding out (the 'cwd' part stands for 'current working directory'). Just type it into the Spyder console to see. For me it is:


```python
os.getcwd()
```




    '/home/lt/GitHub/introduction-to-programming/content'



`os` also provides a function `os.listdir()` for listing the contents of a directory, by default the current wokring directory. So if you are too lazy to go and open your file explorer you can use this function instead to check whether creating a new directory worked for you.


```python
os.listdir()
```




    ['my_new_directory',
     'modules.ipynb',
     'functions.md',
     'intro.md',
     'images',
     'types.md',
     'sequences_mappings.md',
     'standard_library.ipynb',
     'types.ipynb',
     'files.ipynb',
     'intro.ipynb',
     '.ipynb_checkpoints',
     'sequences_mappings.ipynb',
     'testing.md',
     'testing.ipynb',
     'conditions.ipynb',
     '.pytest_cache',
     'files.md',
     'command_line.ipynb',
     'iteration.ipynb',
     'convert_page_formats.sh',
     'modules.md',
     'iteration.md',
     'command_line.md',
     'README.md',
     'functions.ipynb',
     'examples',
     'extras',
     'standard_library.md',
     'html',
     'conditions.md']



The contents of your current directory may of course differ from mine, but you should see that 'my_new_directory' is in there.

Since this first new directory was just an example to test out the workings of `os.mkdir()`, let's tidy up and delete the example directory. `os` provides a function for this too, `os.rmdir()` (in programming, 'rm' is often used as an abbreviation for 'remove'):


```python
os.rmdir('my_new_directory')
```

And just to show off, let's also combine our new `os` skills with our existing knowledge to write a logical statement that checks whether removing the example directory has really worked:


```python
'my_new_directory' in os.listdir()
```




    False



Note that many of the `os` functions that create or remove directories will [raise an exception](extras/glossary.md#exception) if we try to create a directory that already exists or if we try to remove a directory that does not exist:


```python
os.rmdir('nonexistent_directory')
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-17-17b14c181fc8> in <module>
    ----> 1 os.rmdir('nonexistent_directory')
    

    FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_directory'


It is a fairly common situation that we would like to create a directory only if it does not already exist, or remove a directory only if it does exist. We can use a `try` and `except` [control statement](extras/glossary.md#control) to deal with this:


```python
try:
    os.rmdir('nonexistent_directory')
except FileNotFoundError:
    print("Didn't remove the directory because it doesn't exist, but that's ok.")
```

    Didn't remove the directory because it doesn't exist, but that's ok.


(If you need to remind yourself how `try` ... `except` works, look back at the section on [handling errors](conditions.md#Handling-errors) in the lesson on conditions.)

We are close to being able to write our target program. But as usual, we need to learn just one more little thing before we are there. We have learned how to use `os.mkdir()` to create a new directory, but our program also requires creating directories within those new directories. It turns out that this is not completely straightforward, and to arrive at a good solution we need to take a short detour to learn a bit more about directories and file systems.

### Working directory

The initial problem we have is that the function `os.mkdir()` creates the requested new directory inside our current working directory. We saw this behavior above. This is fine for the first step of our target program, creating the per-year folders. But we then want the per-month folders to be inside each of the per-year folders. So how do we tell `os` to put a new directory not in our current working directory but somewhere else?

There is one relatively simple solution that we will not use. But let's look at it anyway, to see why it isn't so great. This solution involves changing the current working directory to be one of the newly-created per-year folders, then using `os.mkdir()` to create the per-month folders there, then switching back to our current working directory, and then repeating the process for another per-year folder.

The function `os.chdir()` changes the current working directory. It is rather like the Python programming equivalent of going into a folder in your file explorer by clicking on it. Here is how we could use it for the first few steps of this solution:


```python
year = '2015'
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

os.mkdir(year)
os.chdir(year)

for m in months:
    os.mkdir(m)
```

Now we need to switch back to our original working directory to create a directory for the next year. How do we do that? If we know the name of our original working directory, we can use that. But that would be a very fragile solution; if we later choose to run our program in a different directory or send it to someone else for them to use, then the specific name of our original working directory will no longer be valid. Fortunately, file systems provide a shortcut for this sort of situation. In a file system, two dots (`..`) stand for 'the directory that contains the current one' (sometimes termed the 'parent' directory). So we can instruct `os.chdir()` to go to `'..'`:


```python
os.chdir('..')
```

Let's check whether all that worked. We need to check a few things:

* Are we back in our original working directory?


```python
os.getcwd()
```




    '/home/lt/GitHub/introduction-to-programming/content'



* Is there a new directory in there called '2015'?


```python
year in os.listdir()
```




    True



* And are all the per-month directories now in the '2015' directory?


```python
os.listdir(year)
```




    ['May',
     'Aug',
     'Jun',
     'Sep',
     'Nov',
     'Jul',
     'Oct',
     'Dec',
     'Jan',
     'Mar',
     'Feb',
     'Apr']



Great, it worked. But we aren't going to use this solution. Why not?

For a short and simple task like this one, it is totally fine. But as we have seen on a few occasions already, there are some good habits that we can get into now that will serve us well when we come to write more complex programs. The 'good habit' that is relevant here is a fairly specific one: We should try to avoid changing directory within a program; we should instead try to let a program run from just one directory. Why does this matter? After all, in our example above, we switch back into the original working directory using `os.chdir('..')`, so the change is only a temporary one and by the time our program has finished, the working directory has been set back to what it was at the start.

But imagine instead that we are writing a slightly more complex program, one that might encounter an [exception](extras/glossary.md#exception) or be terminated at some point in between changing the working directory and changing it back again. For example:


```python
os.mkdir('my_new_directory')
os.chdir('my_new_directory')

n_dirs = input('How many new folders would you like to create? ')
n_dirs = int(n_dirs)

for d in range(n_dirs):
    os.mkdir(str(d+1))

os.chdir('..')
```

    How many new folders would you like to create? five please



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-24-43edc0bffdc9> in <module>
          3 
          4 n_dirs = input('How many new folders would you like to create? ')
    ----> 5 n_dirs = int(n_dirs)
          6 
          7 for d in range(n_dirs):


    ValueError: invalid literal for int() with base 10: 'five please'


In this example, the error halted our program before it could run the command switching back the working directory. So our program now leaves us in a different directory from the one we started in. 


```python
os.getcwd()
```




    '/home/lt/GitHub/introduction-to-programming/content/my_new_directory'



So in order to return to our original working directory, we need to switch back manually. Let's do that now, just so things are fixed for the rest of this lesson.


```python
os.chdir('..')
os.getcwd()
```




    '/home/lt/GitHub/introduction-to-programming/content'



Even this is on its own not such a big deal, more of a minor annoyance. The real problems arise if our program is part of a larger program that may continue running after our program exits. As a result of the error in our program, this other program might now be working in a directory other than the one it expects, and so may end up doing some things wrong, such as putting files in the wrong place or not finding other files that it needs.

### Paths

The slightly more robust solution that we will use in our program is to always stay in the current working directory, and when we have an action that should take place in another directory, specify the 'path' that leads to that directory from the current one.

The [path](extras/glossary.md#path) to a file or directory is a description of its location within the file system of the computer. The path describes a series of turnings to take in the file system in order to get to a particular location. A particular character, known as a [separator](extras/glossary.md#separator) (or occasionally as a 'delimiter') marks out each new directory along the path.

The result of `os.getcwd()` that you see above is an example of a path. It gives the path to the directory in which the files for these lessons are located on my computer. So this path tells us to start in the 'home' directory, then go into the 'lt' directory, and so on. Because the [operating system](extras/glossary.md#os) on my computer is Linux, the separator for the directories along the path is the forward slash '/'. If you are working on a Windows computer, you will see a different separator in the path that you get from `os.getcwd()`.

The `os` module contains an entire submodule, called `path`, for dealing with paths. The `os.path` submodule provides a variable (note: not a function, so no parentheses needed) that stores the path separator for the operating system that you are using:


```python
os.path.sep
```




    '/'



It also provides a function for joining together the names of directories using the appropriate separator for the current operating system. This is useful to make sure that your program is compatible with Windows and other operating systems. For example:


```python
os.path.join('folder', 'subfolder', 'subsubfolder')
```




    'folder/subfolder/subsubfolder'



#### Absolute paths

The 'absolute' path to a file or directory is the full path starting from the top directory on the whole computer, sometimes termed the 'root' directory. On Linux or macOS, the root directory is just named '/'. On Windows, it is a letter denoting the drive on which the files are stored, usually 'C:'.

Occasionally we might need to know the absolute path to a file or directory. The `abspath()` function from the `os.path` module gives us the absolute path to an existing directory within the current working directory. For example:


```python
os.path.abspath('examples')
```




    '/home/lt/GitHub/introduction-to-programming/content/examples'



#### Relative paths

Our target program does not require absolute paths, so we will set them aside for now. Instead, it only needs to know the locations of the new directories we want to create 'relative' to the current working directory. Paths that specify a location relative to some other location are known as 'relative paths'. We can recognize relative paths because they do not begin with the root directory ('/' on macOS and Linux, 'C:' or some other drive letter on Windows). Python will interpret such paths as starting in the current working directory.

So to specify the relative path to one of the per-month directories within one of the per-year directories in our target program, we can write something like `'2015/Jan'`. Or better, in order to make our program compatible across different operating systems, we can insert the appropriate path separator by using `os.path.join()`. Like this:


```python
os.path.join('2015', 'Jan')
```




    '2015/Jan'



So let's try putting this together with some of the other ingredients of our target program to create the next per-year directory and the next per-month directory inside it:


```python
dirname = os.path.join('2016', 'Jan')

os.mkdir(dirname)
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-31-00f059584001> in <module>
          1 dirname = os.path.join('2016', 'Jan')
          2 
    ----> 3 os.mkdir(dirname)
    

    FileNotFoundError: [Errno 2] No such file or directory: '2016/Jan'


Unfortunately, this fails. The reason is that `os.mkdir()` is strictly for creating a single new directory. Here we would like to create a new directory and a new subdirectory at the same time. Since `os.mkdir()` doesn't find the '2016' directory in which to create the 'Jan' subdirectory, it [raises an exception](extras/glossary.md#raise).

Fortunately, there is an alternative function for creating directories containing directories. `os.makedirs()` makes a new directory, along with any intermediate directories along the specified [path](extras/glossary.md#path) to that new directory. (In `makedirs()` 'make' is inexplicably not abbreviated to 'mk' despite the fact that the name of the function is longer than that of `mkdir()`.)


```python
os.makedirs(dirname)

os.listdir('2016')
```




    ['Jan']



It works! That completes the ingredients we need in order to write our target program. It remains to use some [loops](extras/glossary.md#loop) to avoid repeating the `os.makedirs()` command manually for every year and month, but this is something we have [already learned about](iteration.md#Loops).

Try to finish writing the target program yourself, then take a look at it in the example file [make_monthly_directories.py](examples/make_monthly_directories.py).

## Third-party packages

If the standard library is called 'standard', is there a 'non-standard' library? Yes there is. We mentioned before that it is possible to download and install modules that somebody else has written. If you install such extra modules, they are added to your Python 'library' on your computer, and you can import them just like modules from the standard library.

Installable extra modules that were written by somebody else are often termed 'third-party' packages. A [package](extras/glossary.md#package) is a program that adds new capabilities to an existing program. Third-party packages for Python add new modules to your Python installation. The 'third-party' in this case is some other programmer that is neither you nor the developers of Python itself (you are presumably the 'first party' and the developers of Python are the 'second party'). Because Python is such a popular programming language, there is a huge variety of third-party packages out there on the internet, all dealing with various specialist tasks. When you come to write real programs, you will often find that you need to make use of one or more third-party packages, which you may first need to install before you start work on your program.

It is sometimes possible to just download somebody else's *py* files containing the components that you want to use. But this is usually not a good idea. If you use manually-downloaded files, you will also need to update them manually if newer versions become available, and you will need to ensure that the files are in the working directory that your main program runs in when it imports them. Instead, you will usually want to install third-party packages so that they are available wherever you are working, and you will want to install them from some central location that you can refer back to if you need to update them. The Python Package Index ([PyPI](https://pypi.org/)) is an online [repository](extras/glossary.md#repository) of Python packages. It is the standard place to look for existing third-party packages that might help you with your current programming task.

It is important to note some caveats when it comes to third-party packages. That a package is stored on PyPI is not of itself any guarantee that the package works correctly or even that it won't damage your Python installation. More or less anybody can upload their own Python package to PyPI, and many of the packages stored there are out of date, broken, or don't do correctly what they claim. The standard library is produced by the developers of Python, so it can almost always be relied on to work correctly and efficiently, or to be quickly fixed if it does not.

For this reason, it is a good idea to stick to the standard library when you can. But if you perform specialized tasks in programming, you will often be unable to avoid relying on third-party packages. Here are a couple of things to check when deciding whether to use one, and which one to choose if more than one is available for what you want to do:

* Do many other people use this package? If lots of people are using a package, that probably means that it at least works. And the fact that lots of people are using it usually means that bugs won't go unnoticed and may even be quickly fixed by one of the other users.
* Is the package still being 'maintained' (i.e. are the developers of the package currently still fixing bugs and responding to questions)? If a package hasn't been updated for a long time, it might no longer work in the current version of Python, or you might have nobody to turn to if you have problems.

For some of the specialist topics later on we will need to [import](extras/glossary.md#import) modules from third-party packages. When we do, I will note whether an `import` is from the standard library or whether it is from a third-party package, and I will provide instructions for installing it if necessary.

(However, if you have installed Python via Anaconda, then almost all of the third-party packages that we need for this class will already have been installed by default. You can read a list of all the additional packages that Anaconda installs for you [here](https://docs.anaconda.com/anaconda/packages/pkg-docs/)).

## Exercises

### 1

The `string` module provides some additional variables that can be useful for working with strings. Among them is the `punctuation` variable, which contains punctuation characters. Use this variable to create a function called `standardized_words()`. This function returns a list of the words in a text, but in a 'standardized' form. Your function should take a string input argument containing some text, remove all the punctuation, make the contents lowercase, and then return a list of the words in the text.

Here is an example of the function in action:

```
>>> standardized_words('She said: "Hello, world!"')
['she', 'said', 'hello', 'world']
```

### 2

A '[Magic 8-Ball](https://en.wikipedia.org/wiki/Magic_8-Ball)' is a popular toy that when shaken gives a random answer to a question. Write a program that simulates the behavior of a Magic 8-Ball. When you run the program it prints out one of a number of possible answers, at random. You can find a list of the 20 possible answers from the original Magic 8-Ball [here](https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers), or you can define your own shorter list of answers if you don't fancy typing all those into your program.

(Hint: There is a module in the standard library for working with randomness.)

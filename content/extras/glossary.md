# Glossary

Like any other specialists, computer programmers use a lot of arcane vocabulary. Although some of this vocabulary could be simplified to everyday words that mean almost the same things, it is worth knowing the following basic technical terms, for a few reasons:

* You are more likely to find the answers to your programming questions in internet searches if you formulate your search using the right terms.
* The answers you find in internet searches will mostly be written using these terms.
* Once you start working in programming, you will need to talk about the workings of your programs with other programmers.

## argument

An argument is the input to a [function](#function). When we use a function, we place any arguments that we want to give it in the parentheses following the function name. A function can have no arguments, or just one, or many. In the case of more than one argument, the arguments are separated by commas. For example the `print()` function can have multiple arguments:

```python
name = 'Mildred'
middle_initial = 'L'
surname = 'Bonk'
print(name, middle_initial, surname)
```

## assertion

An assertion is a statement that 'asserts' that a particular statement is true, in the same sense of the English verb 'to assert'. If the asserted statement is true, nothing happens and the program may continue as normal, but if it is not true, then an [exception](#exception) is raised.

Assertions can be used to make sure that a program is running as expected at a crucial point, because to continue otherwise would be time-consuming or would make the problem more difficult to diagnose later. Assertions are also commonly used in test programs that check the correct functioning of another program.

There are a few different ways to write assertions in Python, but the simplest is using the `assert` [keyword](#keyword) together with the statement to be checked. For example:

```python
assert 2 + 2 == 4
```

## assignment

If one part of our program generates a piece of information, we may want to store that information and use it in some later part of our program. In this case, we can 'assign' the information into a [variable](#variable). This just means storing something under that variable name. In Python, assignment is done with the equals `=` symbol. Whatever results from the right-hand side is assigned into the variable name on the left-hand side.

For example if we have asked for the user's name using the `input()` function, we can assign the result into a variable called `name`:

```python
name = input('What is your name? ')
```

## attribute

An attribute is like a variable that is 'attached' to another variable, providing some additional information or functionality. For example, file objects have an attribute called `closed`, which stores a [boolean](#boolean) value stating whether the file is closed or not. We can access attributes using a `.`, like this:

```python
f = open('example.txt', mode='w')
f.closed
```

This is the same [syntax](#syntax) as for accessing a [method](#method). Indeed, methods are a kind of attribute.

## boolean

A [variable](#variable) of boolean data [type](#type) (abbreviated to `bool` in Python) stores either of the two possible [values](#value) `True` or `False`. Boolean values often result from a Python command that checks a given condition, for example `2 > 1` [evaluates](#evaluate) to `True` because `2` is indeed greater than `1`.

(The term 'boolean' is derived from the name of [George Boole](https://en.wikipedia.org/wiki/George_Boole), who developed various mathematical methods for working with logical True/False values.)

## bug

A bug is an aspect of a program that does not function as desired. For example, a [function](#function) might give the wrong [return value](#return), or part of the program might unexpectedly raise an [exception](#exception).

## builtin

Python provides a few fundamental [functions](#function) that are already available from the start. These are termed built-in functions, or 'builtins'. The `print()` function is one example of a builtin. You can read a full list of them [here](https://docs.python.org/3/library/functions.html#built-in-functions).

## call

To 'call' a [function](#function) simply means to run that function and make it do its work. The [syntax](#syntax) for calling a function is to place parentheses `()` after the function name, and optionally to place any input [arguments](#argument) inside the parentheses.

(See the entry on [functions](#function) for an example of a 'function call'.)

## comment

A comment is a human-language piece of text that we insert into our Python program. We indicate a comment by prepending the hash character `#`. The Python [interpreter](#interpreter) just ignores any line beginning with a hash character, so we can write whatever we like in our comments; they do not have to be valid Python commands. Comments have a few uses:

* 'headings' to organize sections of the program
* short explanations of how parts of the program work (where this is not otherwise obvious)
* reminders to ourselves and collaborators of problems or parts of the program that need attention

## comprehension

A comprehension is a technique for creating multiple values by writing a 'formula' that generates those values, instead of writing them all out one by one. The [syntax](#syntax) for a comprehension uses the [keywords](#keyword) `for` and `in`.

A 'list comprehension' creates the items in a new [list](#list). For example, the formula might apply some Python command `for` every entry `in` some other existing list, and store the result in a new list:

```python
shopping = ['eggs', 'bacon', 'black pudding', 'sausages']
shopping_initials = [item[0] for item in shopping]
```

There are also comprehensions for creating [dictionaries](#dictionary).

## concatenate

In computing, to 'concatenate' means to stick together one after the other. So the result of concatenating `'Hello '` and `'world!'` is `'Hello world!'`.

## condition

A condition is a [control statement](#control) that ensures that part of our program will run only if a certain statement is true, and optionally what should be run if that statement is false. A condition begins with the [keyword](#keyword) `if`. For example:

```python
if 2 + 2 == 4:
    print('Math is currently working correctly in this universe.')
else:
    print('Nothing is forbidden, everything is permitted.')
```

## control

'Control' (or sometimes 'flow control') refers to controlling which parts of our program are run under which circumstances. A 'control statement' is a command that determines when a particular part of our program is run. [Indentation](#indentation) is used to mark which lines of the program are controlled by the control statement.

Examples of control statements include [conditions](#condition), [loops](#loop), and statements for handling [exceptions](#exception).

## csv

'CSV' stands for 'Comma Separated Values' and refers to a text file format for storing spreadsheet data. In a CSV file, the comma character is used as a [separator](#separator) between the columns of the spreadsheet.

For example, the contents of a simple CSV file might look like this when viewed in a text editor:

```
Name,Age,Location
Mildred,22,USA
Ishmael,19,USA
Sherlock,39,GB
```

## dataframe

A structure that stores data in rows and columns is sometimes termed a 'dataframe' in computing. A more everyday term is simply 'table'.

## delimiter

See [separator](#separator).

## dictionary

A dictionary (often abbreviated to 'dict') is a [data type](#type) that can store multiple values. It does so by storing the values under labels, termed '[keys](#key)'.

The [syntax](#syntax) for creating a dictionary is to place pairs of keys and values inside the 'curly braces' `{}`, separating each key from its associated value with a colon `:` and separating each pair from the next with a comma:

```python
info = {'name':'Mildred', 'age':22, 'location':'USA'}
```

The keys of the dictionary can then be used as [indices](#index) to retrieve the values. For example:

```python
info['age']
```

## directory

Another term for a folder in a computer's file system.

## docstring

A docstring is a [string](#string) (i.e. a piece of text) that provides some human-readable information about the workings of our program. We can write docstrings into our programs o help the users of our programs understand what the program does and how they should use it. We indicate a docstring in our program by enclosing it in 'triple quotes' (`""" """`). A docstring at the top of a *.py* file provides information about the whole file, and a docstring underneath the definition of a [function](#function) provides information about that function.

## DRY

'Don't Repeat Yourself' is a principle that can help with developing flexible programs that can more easily be extended, or can more easily be fixed when mistakes are discovered. A feature of a program that is repeated in many places will need to be found and changed in many places if you decide it must be changed. This opens up a lot of scope for mistakes.

## dunder

The 'double underscore' `__ __` is sometimes abbreviated to 'dunder', because people who have to say 'double underscore' a lot are usually very busy people and need to save every second they can. Python uses double underscores surrounding a name to indicate that that name is involved in the 'behind the scenes' workings of Python and is not usually intended to be used directly.

If a [method](#method) is enclosed in double underscores, that method determines something about the behavior of a particular [data type](#type) in different circumstances. For example, the `__add__()` method determines what happens when a variable of that type is used in conjunction with the `+` [operator](#operator). So:

```python
x.__add__(1)
```

is what happens behind the scenes when we write:

```python
x + 1
```

If a [variable](#variable) is enclosed in double underscores, that variable determines something about the organization of a program. For example, the `__file__` variable stores the [path](#path) to the file that the current program is in.

## encoding

Computers store information in the form of numbers. If we want to store text in a computer, we need some way of allocating each text character a unique number, so that when we read the text data, we turn the stored numbers back into the correct characters. A system for allocating a unique number to each character is known as a 'text encoding'. If we need to transfer text data from one computer to another, we need to make sure that the computer reading the data uses the same encoding for reading as the computer that wrote the data used for writing it.

There are many different text encodings, but the two most important ones to be aware of are:

* [ASCII](https://en.wikipedia.org/wiki/ASCII). This system is universally agreed upon and standard across all normal computers, but it only covers the English alphabet. We cannot use ASCII for non-English characters such as `'à'` or for Devanagari, Sinhalese, emojis, etc.
* [UTF-8](https://en.wikipedia.org/wiki/UTF-8). This system includes many symbols in many writing systems and is by far the most widely-used on the internet. It is also usually the default encoding on Linux [operating systems](#os). For characters that are defined in the ASCII encoding, UTF-8 uses the same system as ASCII, so for these characters the two encodings are equivalent.

Some [operating systems](#os), most notably Windows and macOS, do not always use UTF-8 by default to encode non-ASCII characters. They may instead use a variety of other encodings with names like 'Latin-1', 'ISO-8859', or 'Windows-1252'. Some of these are equivalent for certain subsets of characters, and only become incompatible for a few obscure characters, such as special kinds of quote mark. And to add yet more to the confusion, these various non-UTF-8 encodings are frequently given the wrong name, even in official places such as the documentation for Windows.

## error

Sometimes our program fails and cannot be completed, either because we have not written the program according to the allowed [syntax](#syntax) or because an [exception](#exception) occurs that our program cannot handle. In this case, our program will stop running and Python will display a message with some information about the 'error' that occurred. Any parts of the program that follow the occurrence of the error will not be carried out.

An example error message:

```
  File "my_first_program.py", line 9
    Python, please do some amazing machine learning.
                    ^
SyntaxError: invalid syntax
```

## evaluate

To evaluate a command or expression means to 'work out' its result. So the result of evaluating the Python expression `round(1.618 * 2)` is `3`. The Python interpreter first evaluates `1.618 * 2` and gets `3.236`, then evaluates `round(3.236)` and gets `3`. We sometimes say that a certain expression 'evaluates to' its result. So for example `round(1.618 * 2)` evaluates to `3`, and `2 + 2 == 5` evaluates to `False`.

## exception

Sometimes something 'exceptional' happens during the running of our program. These things are not necessarily fatal for our program, but need to be dealt with in order for our program to continue running as normal. Example exceptions include unexpected input from the user (such as entering a word when our program expects a number), or trying to open a file that has been moved or deleted. When an exception occurs, we say that our program has '[raised](#raise)' an exception.

Python distinguishes among various different kinds of exception. Some of the most common ones that we are likely to encounter are:

* `NameError`: We have tried to use a [variable](#variable), but no variable with that name has been [assigned](#assignment) yet.
* `IndexError`: We have used an [index](#index) that goes beyond the length of whatever we are trying to apply the index to (e.g. a [list](#list)).
* `ValueError`: We have supplied an invalid input [value](#value) to a [function](#function).
* `TypeError`: We have tried to do something with a particular [data type](#type), but that thing only works for a different data type.
* `FileNotFoundError`: We have tried to open a file that does not exist.

We can handle exceptions with a [control statement](#control) that instructs Python to 'try' one action, but to carry out a different action if the first action raises an exception. For example:

```python
try:
    open('melville-moby_dick.txt')
except FileNotFoundError:
    print('The file is not there.')
```

If an exception is raised and we have not specified in our program what to do about it, then the result is an [error](#error) and our program stops.

## float

In Python, and in computing in general, 'float' is a term for a non-whole number, such as 1.618. This is one of the basic data [types](#type) that Python can represent. It is distinguished from whole numbers (or [integers](#integer)) such as 1, 2, 3, etc. Strictly speaking, the term 'float' does not refer to non-whole numbers in general but rather to a specific method for storing non-whole numbers in computers, called '[floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)'. But for basic purposes we can take the term 'float' to mean simply 'non-whole number'.

## function

A function is a sequence of commands that performs a particular action (or multiple actions), and can be used in programs again and again. `print()` is an example of a function, and the action it performs is to display text for the user. Functions can come from many places. Some, such as `print()`, are already [built in](#builtin) to Python, but we can also create our own functions, or [import](#import) them from a program somebody else has written. When we run a function, we say that we [call](#call) the function. A function can have input [arguments](#argument). It may also have a [return value](#return), which we can [assign](#assignment) into a variable.

In the example below, we call the `len()` function with the argument `'floccinaucinihilipilification'`, and it returns the value `29` (which we then assign into the variable `word_length`).

```python
word_length = len('floccinaucinihilipilification')
```

## IDE

An Integrated Development Environment (or IDE) is a computer application that makes the process of programming easier. A typical IDE provides a text editor for writing the actual program, along with various tools for running the program, checking its contents for mistakes, searching for help, etc. [Spyder](https://www.spyder-ide.org/) is the Python IDE that we use in this class.

## import

The contents of a [module](#module) contained in one file can be 'brought in' to the current program file using the Python [keyword](#keyword) `import`. This is known as 'importing' the module, in the same sense as importing foreign goods into a country.

Once imported, the contents of a module are available under the module's [namespace](#namespace).

## indentation

Python uses indentation (spaces at the beginning of a line) to mark some lines of a program as 'belonging to' a preceding [control statement](#control) that determines when or how often those lines should be run.

This use of indentation is fairly specific to Python. In most other programming languages indentation is optional, and is used only for visual clarity; parentheses or other characters are used to control the structure of the program instead.

## index

An 'index' is the position of a particular item in a [sequence](#sequence), such as in a [list](#list) or a [tuple](#tuple). Python's indexing system begins at 0. So the index of the first item in a sequence is 0, the index of the second item is 1, and so on. We can use indices to refer to an item that is stored in a sequence. The Python [syntax](#syntax) for using an index is to place it in square parentheses `[]` after the name of the variable that stores the sequence. So to print out the third item in a list we can type:

```python
shopping = ['eggs', 'bacon', 'black pudding', 'sausages']
print(shopping[2])
```

## integer

An integer is a whole number. So 2 is an integer, but 1.618 is not. 'Integer', abbreviated to `int`, is one of the basic data [types](#type) that Python can represent. A non-whole number is instead called a '[float](#float)'.

## interpreter

A Python interpreter is a computer program that takes our text files of Python commands and turns them into machine code instructions that our computer can understand. We do not especially need to know about or get involved in this process ourselves. Instead, we write our programs as text files of Python commands, and the interpreter takes care of getting our computer to understand them. Strictly, the term 'Python' itself refers to the Python programming language, i.e. a specific set of [syntactical rules](#syntax) that converts text commands into computer actions, but in practice many people use 'Python' to refer also to a Python interpreter program.

## IO

In computing, 'IO' is an abbreviation of 'Input/Output', and refers to anything to do with getting information into and out of a computer program or system. For example, a program may get input from a human being typing at the keyboard or by reading from a text file, and it may send output to the screen or write it into a text file.

## iterable

A [data type](#type) is 'iterable' if it contains multiple values, and it is possible to 'go through' those values one by one. 'Going through' the values in an iterable is called 'iterating'. [Strings](#string) are iterable (we can iterate through their characters), and so are [lists](#list) and [tuples](#tuple) (we can iterate through their items). The most common way of iterating is to use a [loop](#loop).

## JSON

JavaScript Object Notation (JSON) is a text file format for storing data. It stores data as a group of nested [lists](#list) and [dictionaries](#dictionary) that contain [strings](#string) and numbers, using the same [syntax](#syntax) as Python. As the name suggests, JSON was inspired by the JavScript programming language, but the syntax of this language was itself inspired by Python and by other similar programming languages. The JSON format is commonly used for transferring data between programs written in different languages, or for transferring data over the internet.

## key

The 'keys' of a dictionary are the labels under which the values in the dictionary are stored. See the entry on [dictionaries](#dictionary) for a more detailed explanation of this term.

## keyword

A keyword (sometimes also referred to as 'reserved word') is a word that has a special fixed meaning for Python. For example, the keyword `del` deletes something from Python's memory. We cannot use keywords as the names of [variables](#variable) (hence the term 'reserved word'). For a full list of all the keywords in Python, see [here](https://docs.python.org/3/reference/lexical_analysis.html#keywords).

## list

A tuple is a kind of [sequence](#sequence); it can store multiple [values](#value) arranged in order. The [syntax](#syntax) for creating a list is to enclose the values in the sequence inside square parentheses `[]` and separate the values with commas. For example:

```python
shopping = ['eggs', 'bacon', 'black pudding', 'sausages']
```

Lists are very similar to [tuples](#tuple), another kind of sequence. The difference is that tuples are [immutable](#mutability), whereas lists are [mutable](#list).

## locale

Computer users want to be able to interact with their computer in way that takes into account certain pieces of information about the user's language and location. For example, the user may want dates and currency amounts displayed in a certain format, or they may want to see the time displayed in their time zone. A computer's [operating system](#os) may store this user-specific information and make it available to all programs so that they can use it to customize the user's experience. This bundle of information is often termed a 'locale'.

Among other things, the locale may contain information on the user's preferred [encoding](#encoding) for new text files.

## loop

A loop is a [control statement](#control) that repeats certain lines of a program multiple times.

Loops can use the `for` and `in` [keywords](#keyword) to repeat the given actions for every item in an [iterable](#iterable). For example:

```python
shopping = ['eggs', 'bacon', 'black pudding', 'sausages']
for item in shopping:
    print(item)
```

Or they can use the `while` [keyword](#keyword) to repeat the given actions until a particular condition is no longer fulfilled. For example:

```python
answer = 'yes'
while answer == 'yes':
    answer = input("Do you want to keep typing 'yes'? ")
```

## mapping

See [dictionary](#dictionary).

## method

A method is a [function](#function) that is defined specially for variables of one data [type](#type). For example, there is a [string](#string) method called `upper()`, which [returns](#return) an all UPPERCASE version of the string. This function is not defined for other data types such as numbers. The [syntax](#syntax) for using a method is to access it via the variable that we want to apply it to, by placing a `.` after the name of the variable. For example to get an uppercase version of a string variable using the `upper()` method:

```python
name = 'Mildred'
shouty_name = name.upper()
```

## module

A 'module' is simply any text file containing Python commands. However, in practice the term 'module' tends to be reserved for files that do not in themselves run any program that accomplishes a task or produces an output, but instead serve merely to define various [functions](#function) or [variables](#variable) that can be used in other programs. The contents of a module can be incorporated into another program file by [importing](#import) them.

(Compare the term '[script](#script)'.)

We may write our own modules, or we may make use of pre-made modules that are either built in to Python or are provided as part of additional [packages](#package) that we have installed.

## mutability

If a [type](#type) is 'mutable', this means that a [variable](#variable) of that type can have its contents changed or updated without having to be completely overwritten and [re-assigned](#assignment). For example, [lists](#list) are mutable, because applying a list [method](#method) can change the contents of the list without us assigning any result back into the list with `=`. When a mutable variable is changed even though we have not re-assigned it, we sometimes say that it has been changed 'in-place'.

The list in the following example is changed in-place by the `.reverse()` method:

```python
shopping = ['eggs', 'bacon', 'black pudding', 'sausages']
shopping.reverse()
```

The opposite of 'mutable' is 'immutable'. [Strings](#string), [integers](#integer), [floats](#float), and [tuples](#tuple), for example, are all immutable, since their contents can never be changed unless we overwrite them in a new assignment using `=`.

The string in the following example is not changed by calling its `.upper()` method:

```python
name = 'Mildred'
name.upper()
```

Only here is it changed, because of the re-assignment with `=`:

```python
name = 'Mildred'
name = name.upper()
```

('Mutable' [means 'changeable'](https://www.etymonline.com/word/mutable), and has the same origin as 'mutant', as in the *Teenage Mutant Ninja Turtles*.)

## namespace

We can think of our current Python program as creating a sort of 'workspace' in our computer's temporary memory, where all the [variables](#variable), [functions](#function), etc. created in the program are stored and held ready for use as the program runs. Within this main workspace we may have separate 'subspaces' that store some of these things together under a common name, for example because they have a common origin or because they all need to refer to one another in order to function properly. Such a subspace is known as a 'namespace'.

When we [import](#import) a [module](#module), its contents are available under a namespace that by default has the same name as the file containing the module.

To access things that are stored in a namespace rather than in the main workspace of our program, we simply prepend the name of the namespace, followed by a dot. So for example to use a function called `useful_function()` from a namespace called `my_module`:

```python
my_module.useful_function()
```

## newline

When we view a text file that is written over multiple lines, we just see the separate lines of text neatly displayed in our text editor or word processor. But behind the scenes our computer needs some way of storing information about where one line ends and the next begins. This is achieved by the use of a 'newline character' to represent the break between one line and the next. This character is not explicitly shown in a normal text editor, but it is there in the file. In some word processors, such as OpenOffice and Microsoft Word, you can opt to see the newline characters explicitly, and they are typically shown as a '[pilcrow](https://en.wikipedia.org/wiki/Pilcrow)' (¶).

If we want to include a newline character in a [string](#string) in Python, we can represent it with the character combination `'\n'`. These two characters together are interpreted as a single character meaning 'start a new line here'.

## none

The `None` data [type](#type) in Python is used to indicate something that is undefined or has no particular content.

## operator

An operator is a symbol that produces some result when written in an expression along with some other components. For example, the `+` operator produces the sum of two numbers (for example in the expression `2 + 2`). Some operators may have different effects depending on the [type](#type) of the other components of the expression. For example, if used with [strings](#string) instead of numbers the `+` operator [concatenates](#concatenate) the strings.

## OS

The Operating System (abbreviated to 'OS') for a computer is the 'main program' that runs on that computer when it starts, and within which all other programs run. The operating system handles the tasks that are common to all programs, such as locating files, connecting to external devices, and so on. The most popular types of operating system are Microsoft Windows, macOS, and Linux.

## package

A package is a program that adds to the functionality of an existing program. For example, Python packages add new [modules](#module) to a Python installation.

A 'package manager' is a program that downloads, installs, and updates packages. For example, one of the functions of [Anaconda](https://www.anaconda.com/distribution/) is to act as a package manager for Python and other data science software.

## path

The location of a file within the directory system of a computer is known as that file's 'path'. This is the same sense of 'path' as in the English phrase 'a path through the woods'; a file's path describes a series of turnings to take in the file system in order to get to that file.

Different [operating systems](#os) describe paths in different ways. Linux uses the forward slash character `/` as a [separator](#separator) between each branch in the path. So an example path looks like this:

```
/home/mildred/Documents/my_program.py
```

Windows uses the backslash `\` as the separator and starts with a letter identifying the drive on which the file is located. For example:

```
C:\Users\Mildred\Documents\my_program.py
```

Paths can be 'absolute', which means that they describe the full path to a file starting all the way back from the base of the directory system (sometimes called the 'root' directory). Or they can be 'relative', which means that they describe the path to a file starting from some other directory than the root directory, usually the directory that we are currently working in.

## raise

When an [exception](#exception) occurs during the running of a program, we say that the program has 'raised an exception'. (See the entry on [exceptions](#exception) for more details.) This is similar to the use of the word 'raise' in English in phrases like 'to raise an issue'.

We can also deliberately instruct our program to raise an exception, using the `raise` [keyword](#keyword). For example:

```python
raise ValueError('That is an invalid value.')
```

## refactor

Sometimes we may want to change the structure of a program, but without actually changing its behavior. For example, we may want our program to be more clearly readable, or to be easier to modify. Reorganizing a program without changing any of its behavior is termed 'refactoring' the program.

## regression

A situation in which a change to one part of a program unexpectedly breaks other aspects of the program.

## repository

A repository (sometimes abbreviated to 'repo') is a place where the various files constituting a computer program are stored, usually online. People who want to install a program can fetch the current version of the program from its repository.

There are various internet platforms that host repositories. [GitHub](https://github.com/) is one of the most popular. The Python Package Index ([PyPI](https://pypi.org/)) is a repository specifically for Python [packages](#package).

## return

[Functions](#function) usually finish by outputting some kind of result. For example, the `len()` function outputs the length of its argument, and the `round()` function outputs the result of rounding its argument to the nearest whole number. We say that when a function has finished its work, the function 'returns', and whatever it gives us when it has finished is the function's 'return value'. For example the return value of `len('floccinaucinihilipilification')` is `29`, and the return value of `round(1.618)` is `2`.

## script

A script is a text file containing commands that are intended to be run, in order, as a program. The sense of 'script' here is the same as in an actor's script, which tells them what to say and do. Not all text files containing commands are scripts. Some may instead be [modules](#module), which do not of themselves run a specific program, but instead provide extra components that other programs may make use of.

## separator

A separator is a character that is used to separate different parts of a piece of text. Separators can occur in many different contexts:

*Python commands*. For example, the comma character is used as the separator for multiple [arguments](#argument) to a [function](#function) in Python.

*File paths*. A separator character is used to divide the various directories that lead to the location of a file in a file [path](#path).

*Spreadsheet files*. A separator is used in some text file formats to separate the columns of a spreadsheet. For example, in the [csv](#csv) file format, a comma separates the columns.

You may occasionally also encounter the term 'delimiter' used with essentially the same meaning as 'separator'. Technically, a delimiter character marks the limits of some entity (i.e. its beginning and its end). For example, the quote marks `''` mark the beginning and end of a [string](#string). But since delimiting an entity can in a certain sense also be thought of as separating it from its surroundings, the two terms are often effectively synonyms and the distinction is one that only matters to the sort of person whose mission in life is to make sure nobody is wrong on the internet.

## sequence

Sequences are data [types](#type) that can store more than one [value](#value), and arrange those values in a given order. [Tuples](#tuple) and [lists](#list) are examples of sequences.

## slice

A slice is a subsection of a [sequence](#sequence). We can get a slice out of a sequence by giving a range of numbers as the [index](#index). The [syntax](#syntax) for this is to separate the beginning and end of the range with the colon character `:`. The end of a slice is interpreted as meaning 'up-to-but-not-including'.

For example to get a slice of a list containing entries `1` and `2` (i.e. 'from `1` up to but not including `3`'):

```python
shopping = ['eggs', 'bacon', 'black pudding', 'sausages']
shopping[1:3]
```

## string

In computing 'string' essentially means a piece of text (because a piece of text is a 'string' of characters). The string is one of the basic data [types](#type) in Python. We indicate that we want Python to treat something as a string by enclosing it in quote marks `''` (or `""`). The term 'string' is abbreviated to `str` in Python.

## syntax

Syntax refers to the rules governing what constitutes a valid command in a programming language. If we write a program that violates Python's syntax, then the Python interpreter will not be able to understand it, and instead will complain of a 'syntax [error](#error)'.

# TDD

TDD stands for 'Test-Driven Development', an approach to software development in which the developer first writes a test that will check that their change to the main program works as desired, and only then moves on to writing that change to the main program.

## tuple

A tuple is a kind of [sequence](#sequence); it can store multiple [values](#value) arranged in order. The [syntax](#syntax) for creating a tuple is simply to separate the values in the sequence using commas (and for clarity, we can and should also place a pair of parentheses around the whole sequence, though this is not always absolutely necessary). For example:

```python
grades = (5.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.9)
```

Tuples are very similar to [lists](#list), another kind of sequence. The difference is that tuples are [immutable](#mutability), whereas lists are [mutable](#list).

## type

Computer programs can handle information in different forms. For example, some pieces of information may be in the form of text, some may be numbers, and some may be more complex things such as a link to a file on the computer's disk, or a connection to a website. When we create or refer to information in our Python programs, Python needs to be able to know what type of information it is. Python has various [syntactical](#syntax) rules for determining what type a new variable is when we create one in our program. For example, quote marks `''` indicate a [string](#string) (i.e. text).

## value

The contents stored in a [variable](#variable) are often called its 'value'. For example, `name` might be a [string](#string) variable whose value is `'Mildred'`, and `height` might be a [float](#float) variable whose value is `1.96`.

## variable

A variable is a name that stores some information for the duration of our program. We choose the name ourselves, and [assign](#assignment) into that name whatever information we wish to store. We can then use the variable in subsequent steps of the program. For example:

```python
x = 2
print(x ** 0.5)
```

## whitespace

Any text characters that appear simply as blank space are termed 'whitespace' characters. The most common whitespace character is of course simply the space, but there are others, such as the [newline character](#newline) and the tab.

## wildcard

A wildcard is a symbol used in computing to stand for 'everything' or 'anything'. Wildcards are common to many programming languages, not just Python. The most common wildcard symbol is the asterisk (or 'star') `*`. Wildcards can be used together with other characters to refer to 'all things that match a particular pattern'. For example, when referring to file names, the expression `*.txt` means 'all files ending in *.txt*'.

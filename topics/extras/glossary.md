# Glossary

Like any other specialists, computer programmers use a lot of arcane vocabulary. Although much of this vocabulary could be simplified to everyday words that mean almost the same things, it is worth knowing the following basic technical terms, for a few reasons:

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

## assignment

If one part of our program generates a piece of information, we may want to store that information and use it in some later part of our program. In this case, we can 'assign' the information into a [variable](#variable). This just means storing something under that variable name. In Python, assignment is done with the equals `=` symbol. Whatever results from the right-hand side is assigned into the variable name on the left-hand side.

For example if we have asked for the user's name using the `input()` function, we can assign the result into a variable called `name`:

```python
name = input('What is your name? ')
```

## boolean

A [variable](#variable) of boolean data [type](#type) (abbreviated to `bool` in Python) stores either of the two possible [values](#value) `True` or `False`. Boolean values often result from a Python command that checks a given condition, for example `2 > 1` (which [evaluates](#evaluate) to `True` because `2` is indeed greater than `1`).

(The term 'boolean' is derived from the name of [George Boole](https://en.wikipedia.org/wiki/George_Boole), who developed various mathematical methods for working with logical True/False values.)

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
shopping = ['eggs', 'bacon', 'black pudding']
shopping_initials = [item[0] for item in shopping]
```

There are also comprehensions for creating [dictionaries](#dictionary).

## concatenate

In computing, to 'concatenate' means to stick together one after the other. So the result of concatenating `'Hello '` and `'world!'` is `'Hello world!'`.

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

## docstring

A docstring is a [string](#string) (i.e. a piece of text) that provides some human-readable information about the workings of our program. We can write docstrings into our programs o help the users of our programs understand what the program does and how they should use it. We indicate a docstring in our program by enclosing it in 'triple quotes' (`""" """`). A docstring at the top of a *py* file provides information about the whole file, and docstrings underneath the definitions of [functions](#function) provide information about that function.

## error

If part of our program cannot be carried out, either because we have not written it according to the allowed [syntax](#syntax) or because we have asked Python to do something that is not possible (such as open a non-existent file), then our program will stop running and Python will display a message with some information about the error. Any parts of the program that follow the occurrence of the error will not be carried out.

An example error message:

```python
  File "my_first_program.py", line 9
    Python, please do some amazing machine learning.
                    ^
SyntaxError: invalid syntax
```

## evaluate

To evaluate a command or expression means to 'work out' its result. So the result of evaluating the Python expression `round(1.618 * 2)` is `3`. The Python interpreter first evaluates `1.618 * 2` and gets `3.236`, then evaluates `round(3.236)` and gets `3`. We sometimes say that a certain expression 'evaluates to' its result. So `round(1.618 * 2)` evaluates to `3`.

## float

In Python, and in computing in general, 'float' is a term for a non-whole number, such as 1.618. This is one of the basic data [types](#type) that Python can represent. It is distinguished from whole numbers (or [integers](#integer)) such as 1, 2, 3, etc. Strictly speaking, the term 'float' does not refer to non-whole numbers in general but rather to a specific method for storing non-whole numbers in computers, called '[floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)'. But for our purposes we can take the term 'float' to mean simply 'non-whole number'.

## function

A function is a sequence of commands that performs a particular action (or multiple actions), and can be used in programs again and again. `print()` is an example of a function, and the action it performs is to display text for the user. Functions can come from many places. Some, such as `print()`, are already [built in](#builtin) to Python, but we can also create our own functions, or import them from a program somebody else has written. When we run a function, we say that we [call](#call) the function. A function can have input [arguments](#argument). It may also have a [return value](#return), which we can [assign](#assignment) into a variable.

In the example below, we call the `len()` function with the argument `'floccinaucinihilipilification'`, and it returns the value `29` (which we then assign into the variable `word_length`).

```python
word_length = len('floccinaucinihilipilification')
```

## IDE

An Integrated Development Environment (or IDE) is a computer application that makes the process of programming easier. A typical IDE provides a text editor for writing the actual program, along with various tools for checking and running the contents of the program, exploring files, searching for help, etc. [Spyder](https://www.spyder-ide.org/) is the Python IDE that we use in this class.

## index

An 'index' is the position of a particular item in a [sequence](#sequence), such as in a [list](#list) or a [tuple](#tuple). Python's indexing system begins at 0. So the index of the first item in a sequence is 0, the index of the second item is 1, and so on. We can use indices to refer to an item that is stored in a sequence. The Python [syntax](#syntax) for using an index is to place it in square parentheses `[]` after the name of the variable that stores the sequence. So to print out the third item in a list called `shopping` we can type:

```python
print(shopping[2])
```

## integer

An integer is a whole number. So 2 is an integer, but 1.618 is not. 'Integer', abbreviated to `int`, is one of the basic data [types](#type) that Python can represent. A non-whole number is instead called a '[float](#float)'.

## interpreter

A Python interpreter is a computer program that takes our text files of Python commands and turns them into machine code instructions that our computer can understand. We do not especially need to know about or get involved in this process ourselves. Instead, we write our programs as text files of Python commands, and the interpreter takes care of getting out computer to understand them. Strictly, the term 'Python' itself refers to the Python programming language, i.e. a specific set of rules that converts text commands into computer actions, but in practice many people use 'Python' to refer also to a Python interpreter program.

## key

The 'keys' of a dictionary are the labels under which the values in the dictionary are stored. See the entry on [dictionaries](#dictionary) for a more detailed explanation of this term.

## keyword

A keyword (sometimes also referred to as 'reserved word') is a word that has a special fixed meaning for Python. For example, the keyword `del` deletes something from Python's memory. We cannot use keywords as the names of [variables](#variable) (hence the term 'reserved word'). For a full list of all the keywords in Python, see [here](https://docs.python.org/3/reference/lexical_analysis.html#keywords).

## list

A tuple is a kind of [sequence](#sequence); it can store multiple [values](#value) arranged in order. The [syntax](#syntax) for creating a list is to enclose the values in the sequence inside square parentheses `[]` and separate the values with commas. For example:

```python
menu = ['jellied eels', 'black pudding', 'blancmange']
```

Lists are very similar to [tuples](#tuple), another kind of sequence. The difference is that tuples are [immutable](#mutability), whereas lists are [mutable](#list).

## mapping

See [dictionary](#dictionary).

## method

A method is a [function](#function) that is defined specially for variables of one data [type](#type). For example, there is a [string](#string) method called `upper()`, which [returns](#return) an all UPPERCASE version of the string. This function is not defined for other data types such as numbers. The [syntax](#syntax) for using a method is to access it via the variable that we want to apply it to. For example to get an uppercase version of a string variable using the `upper()` method:

```python
name = 'Mildred'
shouty_name = name.upper()
```

## mutability

If a [type](#type) is 'mutable', this means that a [variable](#variable) of that type can have its contents changed or updated without having to be completely overwritten and [re-assigned](#assignment). For example, [lists](#list) are mutable, because applying a list [method](#method) can change the contents of the list without us assigning any result back into the list with `=`. When a mutable variable is changed even though we have not re-assigned it, we sometimes say that it has been changed 'in-place'.

The list in the following example is changed in-place by the `.reverse()` method:

```python
shopping = ['eggs', 'bacon', 'black pudding']
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

## none

The `None` data [type](#type) in Python is used to indicate something that is absent or undefined.

## operator

An operator is a symbol that produces some result when written in an expression along with some other components. For example, the `+` operator produces the sum of two numbers (for example in the expression `2 + 2`). Some operators may have different effects depending on the [type](#type) of the other components of the expression. For example, if used with [strings](#string) instead of numbers the `+` operator [concatenates](#concatenate) the strings.

## return

[Functions](#function) usually finish by outputting some kind of result. For example, the `len()` function outputs the length of its argument, and the `round()` function outputs the result of rounding its argument to the nearest whole number. We say that when a function has finished its work, the function 'returns', and whatever it gives us when it has finished is the function's 'return value'. For example the return value of `len('floccinaucinihilipilification')` is `29`, and the return value of `round(1.618)` is `2`.

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
x = 5
print(x ** 0.5)
```

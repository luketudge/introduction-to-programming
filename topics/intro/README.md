# Creating a computer program with Python

## Computer programs

A computer program is a sequence of instructions for a computer. Ultimately, these instructions take the form of numbers, each of which refers to one action that the computer can take. But in modern computer programming we rarely have to concern ourselves directly with this 'machine code'. Instead, modern computer programs begin their lives simply as one or more text files. These text files are entirely like any other text file; they contain human-readable characters, and have no special properties in themselves. We can open them in a normal text editor like Notepad.

An intermediate step is required in order to run these text files as a program. There are different ways in which this intermediate step can be accomplished. Python, the programming language that we will learn, works via an intermediate computer program called the 'interpreter'. The Python interpreter reads the lines of a text file one by one, turns them into instructions for the computer, and gets the computer to execute those instructions immediately. The interpreter program does its work by applying a particular set of rules to the contents of the text file, rules that convert text commands into computer commands. It is this set of rules that constitutes a particular programming language.

Most computer programs are organized as a collection of multiple such text files, each containing instructions for one aspect of the program's capabilities. There may be one or two main files that represent the starting point of the program, and these main files then refer to others. In addition, the program may include non-text files containing data needed by the program, such as images, sounds, database files, and so on.

Click [here](https://github.com/metabrainz/picard) to see an example of a fairly complex computer program organized as a collection of files. This program, called [MusicBrainz Picard](https://picard.musicbrainz.org/), allows a user to tag music files with information about the artist, song name, album, etc. Take a look at just one file in the program, called [album.py](https://github.com/metabrainz/picard/blob/master/picard/album.py). This is a text file containing instructions written in Python. Its contents are not easily understandable at a first glance, even for an experienced programmer, but notice that it does at least contain some instructions that take the form of everyday English words, such as `from`, `for`, and `if`. It also contains some preamble detailing the license information for the program, which is completely intelligible to a normal human being (or to a lawyer). Further down, the contents become too complex to understand by skim reading, but we may notice some regularities. For example, this file seems to refer to other files in the overall program (note a reference to [config.py](https://github.com/metabrainz/picard/blob/master/picard/config.py) on [line 33](https://github.com/metabrainz/picard/blob/64c4153801ed418c11033ad73981f7209b9cbf63/picard/album.py#L33)).

We won't create any programs that are as complex as Picard, which is the result of several programmers collaborating over a fairly long period of time. However, our programs will have approximately the same structure; they will be collections of text files containing instructions written according to the rules of the Python programming language.

## A Python program

A Python computer program can be as simple as a single file. This is what we will start with. Try opening up Notepad or your favorite text editor, and typing into it the Python command below. Make sure that you use a pure text editor like Notepad and not a word processor like Microsoft Word, because a word processor may not be able to save plain text or may insert additional unwanted content into a text file.

```python
print('Hello.')
```

Programming languages are strict about the correct 'syntax' for their commands, so make sure that you have put the right number of parentheses and quotation marks in the right places. Then save this file somewhere on your computer as a *py* file, for example as `my_program.py`. Note also that most programming languages do not cope well with files that have spaces in their names (the interpreter may think that a file name with a space refers to two separate files or commands), so avoid spaces in the filename and use the underscore character (`_`) to separate words instead.

The *py* file suffix does not alter the properties of the file in any special way; it is just a way of indicating that the file contains commands intended for Python. The file remains just a text file. We can now send it to the Python interpreter in order to run it. (To do this you will need a Python interpreter installed on your computer. Follow the installation instructions [here](../../software) if you haven't already.)

There are various ways to run a *py* file with the Python interpreter. For example, we can just run it the old-school way from the command line as shown below.

![](images/command_line.png)

However, the steps for using the command line vary across different operating systems, so to avoid confusion we will omit this method here and instead go to the Spyder IDE for Python and open the file there. Make sure that you have first installed and [configured](../../software/spyder.md) Spyder, then start it up. In Spyder, use the **Open** option from the **File** menu (or the 'open' icon) to open the text file that you just created.

The green **Run** arrow will run the currently open Python file. Click on this arrow, and then look at the **Console** window to see the effects of running your program. Whereas the editor window displays the *contents* of the text file containing the program, just as any other text editor would, the console window shows the *effects* of running the program (or of running other Python commands).

![](images/console.png)

You should see the contents of the quoted text in your program (e.g. `Hello.`) printed out in the console window like in the screenshot above. We have now created and run our first Python program.

What did this program do and how?

Python is designed to be a more or less human-readable programming language, so in a simple program like this, it is easy to see how the commands in the program are structured:

* `print` is a built-in Python 'function'. It instructs Python to display a piece of text in the console window.
* The parentheses `()` following `print` provide the input (often termed the 'argument') to the function. In this case the argument is the text that we want to print out.
* The quote marks `''` indicate to Python that the text that they enclose should be treated just as plain text (and not for example as a math formula, or a reference to another Python file or some other stored information).

What if we write a program that does not contain valid Python syntax? For example, what if we forget to enclose the text that we would like to print in quote marks? Try editing your program so as to omit the quote marks, like this:

```python
print(Hello.)
```

If you save and run this new version of the program, you will see an 'error message' appear in the console, like the one below.

```
  File "my_program.py", line 1
    print(Hello.)
                ^
SyntaxError: invalid syntax
```

These error messages tell us that some part of our program is not a valid Python command, and so the Python interpreter could not finish running the program. The message tells us which line of our program was responsible (in this case line 1, the only line in the program).

Later on we will cover the rules of Python syntax in more detail, and we will learn more about understanding and fixing errors in our programs. For now, we will look at a few more example programs to get a general idea of how Python works.

## More Python programs

### [greeting.py](examples/greeting.py)

Open the example program *greeting.py* in Spyder (you can find all the example programs for this section [here](examples)). This program is functionally the same as the one we wrote above; it prints out a greeting. But it illustrates two non-functional but very important features of a Python program.

The first of these is the 'docstring' at the top of the program:

```python
"""
A program to print out a welcome message.
"""
```

Text placed in triple quotes at the top of a program (and in some other places, as we will learn later) provides extra information for other developers or users of our program. Use this space to describe briefly what your program does, and for more complex programs some indication of how to use it.

If you start a new Python text file in Spyder via **New file** in the **File** menu (or via the icon), you will see that Spyder inserts a docstring automatically. Something like this:

```python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:25:12 2019

@author: Morag.Chundergruff
"""
```

The exact contents of this automatic starter text may vary a little depending on how Spyder is configured on your operating system. For now, you may ignore any lines that appear before the docstring (like `# -*- coding: utf-8 -*-`); just leave these as they are and we will learn about them later.

The second new feature in *greeting.py* is the 'inline comment' on [line 8](examples/greeting.py#L8). This line is clearly not a Python command. It is instead written in plain English. Python will ignore any text that follows a hash symbol `#`. This allows us to use this symbol to introduce human-readable explanations of the workings of our program. In such a simple program as this, the comment on line 8 is somewhat superfluous; the command on the following line is clear enough on its own. However, as a beginner you should get into the habit of writing comments for most of the Python commands that you put into your program. This helps you to focus and remember how you created your programs, and helps others understand what you did or where you went wrong if your program doesn't work as you expected. Later when you have more experience you can save explanatory comments just for those sections of your program that are a too complex to understand at a first glance.

Finally, on [line 6](examples/greeting.py#L6) we see an example of another use of comments: to make a 'note to self' of what still needs to be added to the program. It is conventional to mark such comments with the text `TODO`. Here we have noted that we would like to make the greeting personal by asking the user to type in their name. This is what the next example program achieves.

### [greeting_personal.py](examples/greeting_personal.py)

Open the *greeting_personal.py* program. Before you run it, read the Python commands that it contains and try to guess what the effect of running the program will be. Then run the program to check your guess.

This program requires the user to type in some information. As with *greeting.py*, all the action occurs over in the console window. After you click on the 'run' icon, look to the console window. You should see that the program has displayed a 'prompt', i.e. some text telling the user what they are expected to do, and is now waiting for the user to type something in.

![](images/input.png)

Beware that when you run a program that requires user input, the program will wait indefinitely until it has received that input. While your program is still running, you won't be able to run it again or run any other program. You can tell that a program is currently running in the console if you see that the square 'stop' icon above the console is lit red, like in the screenshot above. To finish your program and continue editing it or working on other programs, you must first let your running program finish. In this case, you can achieve this by doing as the program asks and typing in your name at the console where the input prompt is displayed.

(Alternatively, if you get stuck with a program running and you just want to break off, you can stop it by clicking on the red 'stop' icon. You should then see that the 'stop' icon is no longer red, and that the console once again displays something like `In [...]:` ready for the next program to run.)

You should have seen that *greeting_personal.py* responded with a greeting containing whatever name you typed in.

How does this program work?

The simplicity of the Python language makes it fairly easy to understand what is going on here. The program begins by using another built-in Python function on [line 9](examples/greeting_personal.py#L9). Unlike the `print()` function that we saw in the preceding example, the `input()` function 'returns' some output. The output in this case is whatever piece of text the user types at the console. If we want to use the output of a function in our Python program we must 'assign' it into a 'variable'. The equals symbol `=` takes whatever output is generated on the right hand side and stores it under whatever name we have put on the left hand side. The name is then available for the rest of the program. Wherever we use this name in the remainder of the program, it stands for the contents that we assigned into it.

There are some important things to note about assigning variables. You can explore why these things are important by making some modifications to *greeting_personal.py* and checking their effects when you run the modified version of the program.

* Unlike in math, the two sides of an equation with `=` are not interchangeable. Instead, the result of the command on the right is first worked out (or 'evaluated') and then assigned into the name on the left. (Try swapping the two sides of the `=` command on [line 9](examples/greeting_personal.py#L9)).
* The order of lines in a Python program matters. Python runs each line in turn. So if our program uses a variable, that variable must be assigned *above* the line on which it is used. (Try placing [line 16](examples/greeting_personal.py#L16) at the top of the program file instead of at the bottom).
* We can use almost any name we like for a variable. We need only be consistent in using that same name throughout our program. (Try replacing both occurrences of the variable `name` with something arbitrary like `x` or `y`).
* There are however some limitations on valid variable names in Python. For example, they can contain numbers but cannot begin with a number. (Try replacing both occurrences of the variable `name` with either `name1` or `1name`).
* It is possible to use the name of a built-in function (such as `print` or `input`) as a variable name in Python, but this is not a good idea as it will overwrite (or 'mask') the function and prevent us from using it in the remainder of our program. (Try replacing both occurrences of the variable `name` with `print`).

In general, we should avoid choosing abstract variable names like `x` and try always to choose a variable name that describes the intended contents of the variable.

Now look at [line 13](examples/greeting_personal.py#L13) of *greeting_personal.py*. This line also assigns a new variable, called `message`. But in this case what is assigned is not the result of a function but an 'expression' involving an 'operator', the `+` symbol. When used with two pieces of text, the `+` operator just sticks them together as one. So this line creates a new piece of text with *Hello* and then whatever name the user typed in at the console.

Note that the text `'Hello '`  is enclosed in quote marks, but the variable `name` is not. This is important. *Hello* is not a variable but simply literal text, so it must be in quote marks. In contrast, `name` *is* a variable and so it should not be enclosed in quote marks. To check your understanding, try to predict what the program would do if `name` on line 13 were enclosed in quote marks, then make the change and run this new version of the program to check whether you were right.

Finally, the workings of [line 16](examples/greeting_personal.py#L16) should be clear if you have understood everything we have covered up to this point.

## Using an IDE

We have just introduced the basic workings of Python programs using a few simple examples. We have been editing and running these programs in the Spyder 'Integrated Development Environment' (IDE). So we turn finally to a few tips for using Spyder.

## Exercises

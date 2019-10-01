# Creating a computer program with Python

## Computer programs

A computer program is a sequence of instructions for a computer. Ultimately, these instructions take the form of numbers, each of which refers to one action that the computer can take. But in modern computer programming we rarely have to concern ourselves directly with this 'machine code'. Instead, modern computer programs begin their lives simply as one or more text files. These text files are entirely like any other text file; they contain human-readable characters, and have no special properties in themselves. We can open them in a normal text editor like Notepad.

An intermediate step is required in order to run these text files as a program. There are different ways in which this intermediate step can be accomplished. Conceptually the simplest of these is the process of 'interpreting' a text file. An intermediate computer program, called the 'interpreter', reads the lines of a text file one by one, turns them into instructions for the computer, and gets the computer to execute those instructions immediately. The interpreter program does its work by applying a particular set of rules to the contents of the text file, rules that convert text commands into computer commands. It is this set of rules that constitutes a particular programming language.

Most computer programs are organized as a collection of multiple such text files, each containing instructions for one aspect of the program's capabilities. There may be one or two main files that represent the starting point of the program, and these main files then refer to others. In addition, the program may include non-text files containing data needed by the program, such as images, sounds, database files, and so on.

Click [here](https://github.com/metabrainz/picard) to see an example of a fairly complex computer program organized as a collection of files. This program, called [MusicBrainz Picard](https://picard.musicbrainz.org/), allows a user to tag music files with information about the artist, song name, album, etc. Take a look at just one file in the program, called [album.py](https://github.com/metabrainz/picard/blob/master/picard/album.py). This is a text file containing instructions written in Python, the programming language that we will learn. Its contents are not easily understandable at a first glance, even for an experienced programmer, but notice that it does at least contain some instructions that take the form of everyday English words, such as `from`, `for`, and `if`. It also contains some preamble detailing the license information for the program, which is completely intelligible to a normal human being (or to a lawyer).

We won't create any programs that are as complex as Picard, which is the result of several programmers collaborating over a fairly long period of time. However, our programs will have approximately the same structure; they will be collections of text files containing instructions written according to the rules of the Python programming language.

## A Python program

A Python computer program can be as simple as a single file. This is what we will start with. Try opening up Notepad or your favorite text editor, and typing into it the Python command below. Make sure that you use a pure text editor like Notepad and not a word processor like Microsoft Word, because a word processor may not be able to save plain text or may insert additional unwanted content into a text file.

```python
print('Hello.')
```

Programming languages are strict about the correct 'syntax' for their commands, so make sure that you have put the right number of parentheses and quotation marks in the right places. Then save this file somewhere on your computer as a *py* file, for example as `my_program.py`. Note also that most programming languages do not cope well with files that have spaces in their names (the interpreter may think that a file name with a space refers to two separate files or commands), so avoid spaces in the filename and use the underscore character (`_`) to separate words instead.

The *py* file suffix does not alter the properties of the file in any special way; it is just a way of indicating that the file contains commands intended for Python. The file remains just a text file, but we can send it to the Python interpreter in order to run it. (To do this you will need a Python interpreter installed on your computer. Follow the installation instructions [here](../../software) if you haven't already.)

There are various ways to run a *py* file with the Python interpreter. For example, we can run it old-school style from the command line as shown below.

![](images/command_line.png)

However, the steps for using the command line vary across different operating systems, so to avoid confusion we will omit this method here and instead go to the Spyder IDE for Python and open the file there. Make sure that you have first installed and [configured](../../software/spyder.md) Spyder, then start it up. In Spyder, use the **Open** option from the **File** menu to open the text file that you just created.

The green **Run** arrow will run the currently open Python file. Click on this arrow, and then look at the **Console** window to see the effects of running your program. Whereas the editor window displays the *contents* of the text file containing the program, just as any other text editor would, the console window shows the *effects* of running the program.

![](images/console.png)

You should see the contents of the quoted text in your program (e.g. `Hello.`) printed out in the console window like in the screenshot above. We have now created and run our first Python program. What did this program do and how?

Python is designed to be a more or less human-readable programming language, so in a simple program like this, it is easy to see how the commands in the program are structured:

* `print` is a built-in Python function. It instructs Python to display a piece of text in the console window.
* The parentheses `()` following `print` provide the input (often termed *argument*) to the function. In this case the argument is the text that we want to print out.
* The quote marks `''` indicate to Python that the text that they enclose should be treated just as plain text, and not for example as a math formula, or a reference to another Python file or function, etc.)

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

These error messages tell us that some part of our program is not a valid Python command, and so the Python interpreter could not finish running the program. The message tells us which line of our program was responsible (in this case line 1, the only line in the program), and sometimes tells us a bit about what sort of error we made.

Later on we will cover the rules of Python syntax more systematically, and we will learn more about understanding and fixing errors in our programs. For now, we will look at a few more example programs to get a general idea of how Python works.

## More Python programs




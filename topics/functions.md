<h1>Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Calling-functions" data-toc-modified-id="Calling-functions-1">Calling functions</a></span></li><li><span><a href="#Arguments" data-toc-modified-id="Arguments-2">Arguments</a></span><ul class="toc-item"><li><span><a href="#Keyword-arguments" data-toc-modified-id="Keyword-arguments-2.1">Keyword arguments</a></span></li></ul></li><li><span><a href="#Return-values" data-toc-modified-id="Return-values-3">Return values</a></span><ul class="toc-item"><li><span><a href="#Side-effects" data-toc-modified-id="Side-effects-3.1">Side effects</a></span></li></ul></li><li><span><a href="#Defining-functions" data-toc-modified-id="Defining-functions-4">Defining functions</a></span><ul class="toc-item"><li><span><a href="#Objective" data-toc-modified-id="Objective-4.1">Objective</a></span></li><li><span><a href="#Default-values" data-toc-modified-id="Default-values-4.2">Default values</a></span></li><li><span><a href="#Raising-exceptions" data-toc-modified-id="Raising-exceptions-4.3">Raising exceptions</a></span></li></ul></li><li><span><a href="#Docstrings" data-toc-modified-id="Docstrings-5">Docstrings</a></span></li><li><span><a href="#Function-or-loop?" data-toc-modified-id="Function-or-loop?-6">Function or loop?</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-7">Exercises</a></span><ul class="toc-item"><li><span><a href="#1" data-toc-modified-id="1-7.1">1</a></span></li><li><span><a href="#2" data-toc-modified-id="2-7.2">2</a></span></li></ul></li></ul></div>

# Functions

We have been working with [functions](extras/glossary.md#function) since the very first lesson. For example, we have often used the `input()` function to allow users of our program to type something in, and the `print()` function to display messages for the user.


```python
name = input('What is your name? ')

print('Hello', name)
```

    What is your name? Mildred
    Hello Mildred


In addition, we have learned about a few other miscellaneous functions, such as `len()` for counting the number of items in a [sequence](extras/glossary.md#sequence) (or the number of characters in a [string](extras/glossary.md#string)).


```python
len(name)
```




    7



And we have learned about a special kind of function, called [methods](extras/glossary.md#method), that are 'attached' to just one [data type](extras/glossary.md#type). For example the [string](extras/glossary.md#string) method `upper()`:


```python
name.upper()
```




    'MILDRED'



The [syntax](extras/glossary.md#syntax) for using methods is slightly different from that for functions. We will set aside methods for now and focus on functions in general.

## Calling functions

The standard syntax for using a function is:

* write the name of the function
* open parentheses `(`
* (optionally) write any inputs to the function
  * multiple inputs must be separated by commas
* close parentheses `)`

The function will then output some result (although a few functions have no output).

There are a few important pieces of computing vocabulary associated with functions:

* **Call**. Running a function is known as '[calling](extras/glossary.md#call)' the function. When we run a function, this is sometimes termed a 'function call'. It is as if the function is playing outside in the garden, and then we call it in because we want it to do something for us.
* **Argument**. The inputs to a function, which go inside the parentheses, are known as the function's '[arguments](extras/glossary.md#argument)'. This is very different from the everyday use of the word 'argument', but is probably distantly related to the sense of 'argument' as meaning 'valid or confirmatory information'. According to *[The Origins of Mathematical Words](https://muse.jhu.edu/book/26769)*, astronomers used to compile tables of numbers about the positions of celestial bodies, and then input these numbers into further calculations. These validated input numbers were known as 'arguments' in the sense of 'supporting information'.
* **Return value**. The output of the function is known as its '[return value](extras/glossary.md#return)'. When the function has finished doing its work and reports back to us with the result, we say that the function has 'returned' that result.

We can see some of these terms in action in a few [error messages](extras/glossary.md#error) that we encounter if we use a function incorrectly. For example if we try to [call](extras/glossary.md#call) something that is not a function:


```python
some_number = 42

some_number()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-40e574c91384> in <module>
          1 some_number = 42
          2 
    ----> 3 some_number()
    

    TypeError: 'int' object is not callable


Or if we supply the wrong number of [arguments](extras/glossary.md#argument):


```python
len()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-adf3103c7c3e> in <module>
    ----> 1 len()
    

    TypeError: len() takes exactly one argument (0 given)



```python
len('Mildred', 'Bonk')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-e6b31188cf9e> in <module>
    ----> 1 len('Mildred', 'Bonk')
    

    TypeError: len() takes exactly one argument (2 given)


## Arguments

Some functions are flexible in the number of arguments they take. For example, `print()` can take an indefinite number of arguments, and just prints them all out one after the other:


```python
print('Hello', 'world', '!')
```

    Hello world !


`print()` can even take no arguments at all. In this case, it prints a [newline](extras/glossary.md#newline) (a blank line):


```python
print()
```

    


Notice that even if there are no input arguments, the parentheses are still required. The presence of the parentheses is what lets Python know that we actually want to [call](extras/glossary.md#call) the function. If we omit them, the function is not called. Instead, Python simply confirms: "yes, that is a function".


```python
print
```




    <function print>



### Keyword arguments

Some functions are a little more complex. As well as taking one or more arguments in the standard way that we have seen so far, some functions can take some additional special arguments that modify the behavior of the function in some way. These arguments have specific names, and we can assign values into those specific names (with `=`) in order to make them work.

If this sounds a little abstract, it will become much clearer with an example. The `print()` function can also take some additional named arguments called `sep` and `end`. `sep` (an abbreviation of 'separator') specifies characters to print in between all the other arguments, and `end` specifies some characters to print at the end:


```python
print('Hello', 'my name is', 'Mildred', sep='...', end='!')
```

    Hello...my name is...Mildred!

These special named arguments are known as 'keyword arguments' (and sometimes you may see them referred to by the abbreviation `kwargs`). Keyword arguments have fixed names. Unlike when we [assign](extras/glossary.md#assignment) a variable, we cannot just give them any name we like. Otherwise, the function would have no way of knowing which particular part of its behavior we intend each keyword argument to modify.

If we try to assign the keyword arguments to just any old name, the result is an error. And now that we know the relevant vocabulary, the text of the error message is pretty clear about what we did wrong:


```python
print('Hello', 'my name is', 'Mildred', x='...', y='!')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-abafff96c1e1> in <module>
    ----> 1 print('Hello', 'my name is', 'Mildred', x='...', y='!')
    

    TypeError: 'x' is an invalid keyword argument for this function


But up until now we have been using `print()` without specifying any values for the keyword arguments `sep` and `end`. So how did `print()` know what to do? Keyword arguments have 'default values', which are used if no keyword arguments are given. If you look at the standard behavior of `print()` you may be able to guess what the default values for `sep` and `end` are:


```python
print('Hello', 'my name is', 'Mildred')
```

    Hello my name is Mildred


That's right, the default for `sep` is a space (i.e. `sep=' '`). It is a little harder to see what the default for `end` is, because it is somewhat invisible, but it is a [newline character](extras/glossary.md#newline), starting a new line. If we ask `end` to be nothing (i.e. an empty string `''`), then anything that is printed next will continue printing on the same line, instead of on a new one:


```python
print('Hello', 'my name is', 'Mildred', end='')
print('and I am very excited to be using your computer program.')
```

    Hello my name is Mildredand I am very excited to be using your computer program.


When you look at the official Python [documentation for the `print()` function](https://docs.python.org/3/library/functions.html#print), you will see the possible input arguments written out in the header, and you will see the default values for the keyword arguments. For example, inside the parentheses you will see `end='\n'`, giving the default value for the `end` keyword argument (the character combination `'\n'` is used to represent the [newline character](extras/glossary.md#newline)). When you first encounter a function that you would like to use, it is a good idea to seek out the documentation and look for this header, to see what the input arguments are, and whether any of them set default behavior that you might want to change.

## Return values

The output of a function is called its [return value](extras/glossary.md#return). Usually, when we use a function, we [assign](extras/glossary.md#assignment) the return value into a variable by placing `=` in front of the [function call](extras/glossary.md#call). For example, the return value of the `input()` function is a [string](extras/glossary.md#string) containing whatever characters the user typed in, and the return value of the `len()` function is an integer containing the number of items in a sequence or number of characters in a string. We can assign return values into variables to make use of them in the rest of our program:


```python
name = input('Name: ')

n_letters = len(name)

print('Your name has', n_letters, 'letters.')
```

    Name: Mildred
    Your name has 7 letters.


### Side effects

Does the `print()` function have a [return value](extras/glossary.md#return)? At first, it may seem as though it does. Doesn't it return the printed text?


```python
text = print('Hello.')

type(text)
```

    Hello.





    NoneType



As we can see here, `print()` has no return value (it returns [`None`](extras/glossary.md#none)). It is important to distinguish between what a function *does* and what it *returns*. Sometimes, a function simply 'does things' but does not produce a return value that we can [assign](extras/glossary.md#assignment) into a variable. The *effect* of the `print()` function is to display text, but the text is not its return value. Any effects of a function that are not reflected in its return value are termed 'side effects' of the function. Displaying text is a 'side effect' of the `print()` function, though that may sound like a strange way of talking about it.

We have encountered this phenomenon before in a slightly different guise when we learned about list methods. Remember that list methods just go ahead and change the list, and they don't return the changed list, they return `None`. Changing the contents of the list is a 'side effect' of list methods.

Most functions, however, have no side effects; everything they do is reflected in their return value. For example, `len()` returns the length of something, and this is all that it does.

## Defining functions

All the functions that we have met so far are '[builtins](extras/glossary.md#builtin)', functions that are already 'built in' to Python and are ready for us to use whenever we write a Python program.

We are not limited to using the built-in functions. We can also define our own functions. We can then use these functions, either in the same program in which they are defined, or in another program, or we can even publish them online for other people to download and use in their own programs.

This is what we will learn about now.

### Objective

Let's again set ourselves a task to structure our learning. Imagine that we have a program that gathers user names. In this simple example program we will omit using `input()` to get the user names, because it gets tedious to keep testing the program by typing input at the console. Let's just define some names manually so we have a few to work with:


```python
user_name = 'Mildred Bonk'
aunts_name = 'Jennifer Boolean'
uncles_name = 'Julian Boolean'
```

Now imagine that we want to create for each user an abbreviated ID consisting of their initials (i.e. the first letters of their first and surnames).

We can do this using the string [method](extras/glossary.md#method) `split()` and some [indexing](extras/glossary.md#index), both of which we have learned about before:


```python
names = user_name.split()
firstname = names[0]
surname = names[1]
user_id = firstname[0] + surname[0]

print(user_id)
```

    MB


Now that we have confirmed that it works, let's do it for the other two users as well:


```python
names = aunts_name.split()
firstname = names[0]
surname = names[1]
aunts_id = firstname[0] + surname[0]

names = uncles_name.split()
firstname = names[0]
surname = names[1]
uncles_id = firstname[0] + surname[0]

print(aunts_id)
print(uncles_id)
```

    JB
    JB


We notice that the next two users have the same ID. So now we decide that a better way to allocate IDs would be to use the first *two* letters of each user's first and surname. We have not picked a great way of approaching this task. Because we have copied and pasted almost the same lines three times to accomplish the same task, we now have to change things in several places whenever we decide that we want to change something about the way that that task is accomplished. We are fallible human beings and we are likely to miss one of the places in which the change is necessary, thus introducing mistakes into our program. [DRY](https://en.wikipedia.org/wiki/Don't_repeat_yourself).

It would be nice if there were just a function that could take a user name as its [argument](extras/glossary.md#argument) and [return](extras/glossary.md#) the user's initials. Then we could use it in our program. Even better would be if we could modify this function's behavior, and for the modified behavior to take effect wherever the function is used. This would allow us to make changes in just one place that take effect for the whole program.

Maybe there is a built-in function that suits our needs?


```python
user_id = get_initials(user_name)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-05f0e1156bc4> in <module>
    ----> 1 user_id = get_initials(user_name)
    

    NameError: name 'get_initials' is not defined


No luck. We need to define this function ourselves.

Here is what we would like our function `get_initials()` to do:

* take a [string](extras/glossary.md#string) [argument](extras/glossary.md#argument) containing two names
* return a new string containing the initials of those names (i.e. the first letter of each)
* take two additional keyword arguments:
  * `n`: an [integer](extras/glossary.md#integer) specifying the number of initial letters to use from each name
    * this should default to `1` to produce the standard single initials
  * `uppercase`: a [boolean](extras/glossary.md#boolean) specifying whether to return the initials in UPPERCASE
    * this should default to `False` to produce lowercase initials
* in addition, the function should produce an informative error message if the input argument string does not contain exactly two names (e.g. `'Mildred'` or `'Mildred T. Bonk'`)

When we decide to define a new function of our own, we should think about four ingredients:

* the name of the function
* its input arguments
* what steps it carries out (the 'body' of the function)
* the return value

Below is the [syntax](extras/glossary.md#syntax) for defining a new function. A function definition is a kind of [control statement](extras/glossary.md#control), like a [condition](extras/glossary.md#condition) or a [loop](extras/glossary.md#loop), and some of the basic syntactical features of control statements, such as a colon `:` and [indentation](extras/glossary.md#indentation) appear here as well.

* write `def`
* write the name of the function (pick any name, just like for creating a variable)
* open parentheses `(`
* write the names of any arguments the function should have
  * these should be separated by commas
* write the steps that the function carries out
  * these should be indented
  * in these steps, use the names of the input arguments
* write `return`
* write what the function should return

Let's see this syntax in action for a simple first attempt at our target function (though note that this first attempt contains a deliberate mistake for didactic purposes):


```python
def get_initials(name):
    names = name.split()
    firstname = names[0]
    surname = names[1]
    initials = firstname[0] + surname[0]
```

Let's now [call](extras/glossary.md#call) our function, with an example name as the input argument:


```python
get_initials(user_name)
```

We don't seem to get any answer. Maybe the `initials` variable that is created inside the function is the place to look?


```python
print(initials)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-22-af522d26ad22> in <module>
    ----> 1 print(initials)
    

    NameError: name 'initials' is not defined


No luck there either. Any variables that we create inside the body of a function are only for the function's own internal use. They are discarded once the function has done its work.

The deliberate mistake in our first attempt at defining our function is that we have forgotten to use the `return` keyword on the last line. Like this:


```python
def get_initials(name):
    names = name.split()
    firstname = names[0]
    surname = names[1]
    return firstname[0] + surname[0]
```

Whatever we write just after `return` is the [return value](extras/glossary.md#return), the thing that the function will output. This is the only thing we can get from the function when we [call](extras/glossary.md#call) it. Any other variables created inside the function are just temporary intermediate steps on the way to the return value.

Note that `def` (an abbreviation of 'define') and `return` are [keywords](extras/glossary.md#keyword); their roles are fixed. But `get_initials` is our chosen name for the function. This could be different. Likewise `name` is the name we have given to the input argument. This too could be different if we wish. But just as in a [loop](extras/glossary.md#loop) or a [comprehension](extras/glossary.md#comprehension), we must be consistent in using this same name in the body of the function wherever we mean 'whatever input is given to the function'. So if we were to use something arbitrary like `x` for the name of the input argument, we would have to also use `x` on line 2 above and say `x.split()` instead of `name.split()`.

Now let's test the correct version of the function by calling it and [assigning](extras/glossary.md#assignment) the return value into a variable:


```python
user_initials = get_initials(user_name)

print(user_initials)
```

    MB


It works! It bloody works!

If you do not experience a brief twinge of transcendental joy when you have written a working function then there really is no hope for you. But our function isn't complete yet. Let's start adding the additional features that we want our function to have.

### Default values

We said that we wanted to add two keyword arguments, and that these should have specific default values. How do we specify default values for arguments? If you look again at the [documentation for the `print()` function](https://docs.python.org/3/library/functions.html#print), you will see an example of the syntax for default values. When we define our function, we just have to assign the default values using `=`. When we (or someone else) later [calls](extras/glossary.md#call) the function, if they do not enter these arguments, the default values will be used, but if they do enter them, then whatever values they enter will be used instead.

Let's create an updated version of our function, with the default values for the arguments `n` and `uppercase`. We should also incorporate these arguments into the body of the function. To make use of `n`, we should use it as a [slice](extras/glossary.md#slice) index to get the first `n` characters from each name (line 5 below). And to make use of `uppercase` we should put it in an `if` condition that applies the string [method](extras/glossary.md#method) `upper()` if the `uppercase` argument is `True` (line 6 below).


```python
def get_initials(name, n=1, uppercase=False):
    names = name.split()
    firstname = names[0]
    surname = names[1]
    initials = firstname[:n] + surname[:n]
    if uppercase:
        return initials.upper()
    else:
        return initials.lower()
```

(In case you are wondering: No, we do not need to write `if uppercase == True` as our condition. In everyday English, it would be redundant to say something like "If the statement 'it is raining' is true, take your umbrella." We can just say "If it is raining, take your umbrella." So too in Python. We do not have to ask `if x == True` when `x` is a [boolean](extras/glossary.md#boolean) variable that is already either `True` or `False`. We can just ask `if x`.)

And now let's test the new version of our function. We should check carefully that it works correctly both when we do not specify the keyword arguments, and when we do.


```python
get_initials(user_name)
```




    'mb'




```python
get_initials(user_name, n=2)
```




    'mibo'




```python
get_initials(user_name, uppercase=True)
```




    'MB'



Great.

### Raising exceptions

In the [lesson on conditions](conditions.md), we learned about [exceptions](extras/glossary.md#exception). Exceptions are notifications that a program has encountered something that it cannot normally deal with. We would like our function to produce an exception if the [string](extras/glossary.md#string) that comes in as the first input [argument](extras/glossary.md#argument) does not contain exactly two names, because this is an input that our function is not intended to deal with.

Producing an exception is termed '[raising](extras/glossary.md#raise)' an exception, where the verb 'to raise' is being used in the same sense as in 'to raise an issue' or 'to raise a question'. The `raise` [keyword](extras/glossary.md#keyword) allows us to raise an exception manually. The [syntax](extras/glossary.md#syntax) for raising an exception is:

* write `raise`
* write the name of the kind of exception you want to raise (see the glossary entry on [exceptions](extras/glossary.md#exception) for a list of the most common ones)
* open parentheses `(`
* write an informative error message
* close parentheses `)`

Let's raise an exception just for fun, to see how this works:


```python
raise ValueError('OMG that is not valid. You have broken your computer FOR EVER.')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-29-b55543e1f431> in <module>
    ----> 1 raise ValueError('OMG that is not valid. You have broken your computer FOR EVER.')
    

    ValueError: OMG that is not valid. You have broken your computer FOR EVER.


The `ValueError` is the most common [exception](extras/glossary.md#exception) that we will want to raise ourselves in our functions. For other programmers using our functions, a `ValueError` exception lets them know that they have tried to use the function with an input that it cannot handle.

Below is our function, updated to include checking the first input [argument](extras/glossary.md#argument) and raising an exception if it does not contain exactly two names. In order to produce an informative [error message](extras/glossary.md#error), we make use of the [string](extras/glossary.md#string) [method](extras/glossary.md#method) `format()`.


```python
def get_initials(name, n=1, uppercase=False):
    names = name.split()
    n_names = len(names)
    if n_names != 2:
        error_message = "'{}' contains {} names but should contain 2."
        raise ValueError(error_message.format(name, n_names))
    firstname = names[0]
    surname = names[1]
    initials = firstname[:n] + surname[:n]
    if uppercase:
        return initials.upper()
    else:
        return initials.lower()
```

Our function is starting to get quite complex. So let's first check that the changes we just made have not disrupted the normal workings of the function:


```python
get_initials(user_name)
```




    'mb'



And now let's check that we get an appropriate [error message](extras/glossary.md#error) if we input a string that does not contain the expected number of names:


```python
get_initials('Mildred T. Bonk')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-32-d78bf5992a4b> in <module>
    ----> 1 get_initials('Mildred T. Bonk')
    

    <ipython-input-30-ab9b076cef55> in get_initials(name, n, uppercase)
          4     if n_names != 2:
          5         error_message = "'{}' contains {} names but should contain 2."
    ----> 6         raise ValueError(error_message.format(name, n_names))
          7     firstname = names[0]
          8     surname = names[1]


    ValueError: 'Mildred T. Bonk' contains 3 names but should contain 2.


Yes! The transcendental joy that results from successfully raising an exception almost trumps that of writing a working function.

Our function is now complete. We can apply it again and again with many different input arguments in different parts of our program:


```python
get_initials(user_name)
```




    'mb'




```python
get_initials(aunts_name, n=2)
```




    'jebo'




```python
get_initials(uncles_name, n=2)
```




    'jubo'




```python
get_initials('David Hasselhoff', uppercase=True)
```




    'DH'



## Docstrings

Earlier, I briefly mentioned a few different ways in which we can use a function that we have defined. We can use the function right away within the same program, but we can also re-use a function in other programs or even publish our function online so that other programmers can use it.

In this last case, we should provide some documentation for our functions. Other programmers will want to know what our function does, how to use it, what sort of input [arguments](extras/glossary.md#argument) it expects, and what it [returns](extras/glossary.md#return).

In the very first lesson, we learned how to provide a human-readable description of our program by enclosing it in triple quotes at the top of the file. For example:

```python
"""
This is a program to do some amazing machine learning.
"""
```

A triple-quoted string used like this is known as a [docstring](extras/glossary.md#docstring). Python allows us to provide docstrings for individual functions as well as for our program as a whole. Like the docstring for a program, a function docstring does not have any effect on the workings of the function; it is just for human beings to read. You should get into the habit of writing docstrings for your functions, unless the function is so short as to be trivially understandable. Even if you don't plan to make your work public, collaborators and colleagues will probably need to look at it at some point, and you yourself will be surprised at how much you have forgotten about the workings of your own program when you return to it weeks later.

What information should we put in a docstring, and how should we organize it? There are various conventions that different groups of programmers follow. Google provides a Python style guide for its employees, and it makes some good recommendations about docstrings. You can read them [here](http://google.github.io/styleguide/pyguide.html#383-functions-and-methods). In general, we should include the following pieces of information:

* A very brief description of what the function does.
* An example of its use.
* A explanation of the input [arguments](extras/glossary.md#argument).
* The [return value](extras/glossary.md#return).
* Whether the function [raises](extras/glossary.md#raise) any exceptions.

You can see an example docstring for our `get_initials()` function in the example program [initials.py](examples/initials.py). (In case you are wondering what is going on on line 43 of this file, this will be explained in the next lesson.)

## Function or loop?

In the [previous lesson](iteration.md) we saw that [loops](extras/glossary.md#loop) are a good way of avoiding having to write out the same lines multiple times. And we began the current lesson with a similar sort of situation; we wanted to apply the same few Python commands repeatedly in order to create abbreviated user IDs for multiple users. So couldn't we just have done this in a loop?

Yes, we could. And for this simple example, a loop might have been ok. We can loop through the items in a list of user names, process each one in the loop, and append the result to a new list with the list [method](extras/glossary.md#method) `append()`. It would look something like this:


```python
user_names = ['Mildred Bonk', 'Jennifer Boolean', 'Julian Boolean']
user_ids = []

for name in user_names:
    names = name.split()
    firstname = names[0]
    surname = names[1]
    initials = firstname[:2] + surname[:2]
    user_ids.append(initials.upper())

user_ids
```




    ['MIBO', 'JEBO', 'JUBO']



But there are some important differences between loops and functions. The most important one is that a loop runs immediately in only one place in our program, whereas a function can be re-used in multiple places. Imagine that our program needed to collect and process some of the user names early on, and collect more user names after having carried out some intermediate actions. We could not achieve this with a loop, as the loop requires us to have a complete sequence of inputs ready to loop through. A function allows us to run some lines, then do something else, then go back and run the same lines again:


```python
user_names = ['Mildred Bonk', 'Jennifer Boolean', 'Julian Boolean']
user_ids = [get_initials(name) for name in user_names]

print('Carrying out some intermediate actions...')
print('Now adding the ID of the admin user...')

admin_id = get_initials('David Hasselhoff')
```

    Carrying out some intermediate actions...
    Now adding the ID of the admin user...


If this seems a little abstract to you, take a look at the second example program for this lesson, [fun_facts.py](examples/fun_facts.py). It demonstrates the re-use of a function (that gets the answer to a 'yes/no' question) in multiple places in a program.

The other important difference between loops and functions is that a function can be re-used in a *different* program, whereas a loop cannot (at least, not without manually copying and pasting it into the new program). Re-using functions in more than one file is the topic of the next lesson.

## Exercises

### 1

Take a look at the [fun_facts.py](examples/fun_facts.py) example program. It defines a function `yorn()` for prompting the user to answer a 'yes/no' question. Currently, the function only accepts `'y'` or `'n'` as responses. Modify it so that it also allows the user to type in the complete words `'yes'` or `'no'`. Make sure to run your modified version of the program a few times and type in different responses at the console to check that your changes are correct.

### 2

Write a new program, called *words.py*. The program defines a single function, called `first_n_words()`. The function turns a piece of text into a list of the first few words contained in the text. Here are the details of how it should work:

* Take a string argument called `text` and an integer argument called `n`.
* Return a list containing the first `n` words in `text`.
* `n` has a default value of `1` (i.e. if no `n` is given, return a list containing only the first word in `text`).
* Consider words as being any groups of characters separated by spaces.
* If the value of `n` is greater than the number of words in `text`, just return all the words in `text`.
* If the value of `n` is `0` (or there are no words in `text`), return an empty list.
* But if the value of `n` is negative, raise a `ValueError` stating that negative values are not valid.
* Include an appropriate docstring for the function.

Here are some examples of the function's desired behavior:

```
>>> first_n_words('Hello my name is Mildred.')
['Hello']
```

```
>>> first_n_words('Hello my name is Mildred.', n=4)
['Hello', 'my', 'name', 'is']
```

```
>>> first_n_words('Hello my name is Mildred.', n=9000)
['Hello', 'my', 'name', 'is', 'Mildred.']
```

```
>>> first_n_words('Hello my name is Mildred.', n=0)
[]
```

```
>>> first_n_words('Hello my name is Mildred.', n=-1)
ValueError: Cannot get a negative number of words.
```

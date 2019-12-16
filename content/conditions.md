<h1>Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Objective" data-toc-modified-id="Objective-1">Objective</a></span></li><li><span><a href="#Booleans" data-toc-modified-id="Booleans-2">Booleans</a></span><ul class="toc-item"><li><span><a href="#Logic" data-toc-modified-id="Logic-2.1">Logic</a></span></li><li><span><a href="#Conversion-to-boolean" data-toc-modified-id="Conversion-to-boolean-2.2">Conversion to boolean</a></span></li></ul></li><li><span><a href="#if" data-toc-modified-id="if-3">if</a></span><ul class="toc-item"><li><span><a href="#Indentation" data-toc-modified-id="Indentation-3.1">Indentation</a></span></li><li><span><a href="#Debugging" data-toc-modified-id="Debugging-3.2">Debugging</a></span></li></ul></li><li><span><a href="#if-elif-else" data-toc-modified-id="if-elif-else-4">if elif else</a></span></li><li><span><a href="#Nested-conditions" data-toc-modified-id="Nested-conditions-5">Nested conditions</a></span></li><li><span><a href="#More-debugging" data-toc-modified-id="More-debugging-6">More debugging</a></span></li><li><span><a href="#in" data-toc-modified-id="in-7">in</a></span></li><li><span><a href="#Handling-errors" data-toc-modified-id="Handling-errors-8">Handling errors</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-9">Exercises</a></span><ul class="toc-item"><li><span><a href="#1" data-toc-modified-id="1-9.1">1</a></span></li><li><span><a href="#2" data-toc-modified-id="2-9.2">2</a></span></li></ul></li></ul></div>

# Conditions

We are already able to write programs that are somewhat interactive; we get the user to type something in and then we process whatever they typed in. The next level of excitement for our users is to interact with a program that does completely *different* things depending on what they type in.

So far, the 'flow' of our programs has always been linear; they carry out a series of steps in order, with no variations. We would now like to give the flow of our programs a branching structure, such that its behavior will vary depending on the circumstances. This can be achieved with [control statements](extras/glossary.md#control): lines of our program that do not on their own produce any result, but instead control when (or how often, or in what variations) other lines are run.

One of the simplest kinds of control statement is a 'conditional' control statement. It tells Python to run certain lines of our program only if a certain condition is fulfilled. This is what we will learn about now.

## Objective

To give ourselves something to work towards, let's imagine a fairly simple toy program that we would like to create.

**hoff.py**:

* Ask the user to enter their name and surname.
* Find one interesting thing to say about their name:
  * If they are called 'David Hasselhoff', ask "Are you THE David Hasselhoff?"
    * If they say yes, say "Wow!"
    * If they say no, say "Well that is quite a coincidence that you have the same name."
  * Else if their surname is 'Hasselhoff', ask "Any relation to David Hasselhoff?"
    * If they say yes, say "Wow!"
    * If they say no, say "You never know, you might be."
  * Else if their initials are 'DH', say "You have the same initials as David Hasselhoff!"
  * Else if their first name is a variant of 'David' such as 'Dave', 'Davy', 'Dafydd', say "Your name is a bit like 'David', as in 'David Hasselhoff'."
  * Else, as a last resort, say " suppose you could change your name to something more interesting, like 'David Hasselhoff'."

The branching structure of our target program is moderately complex. We will build it up step by step, learning about the necessary programming techniques as we go.

## Booleans

We have already briefly met the [booleans](extras/glossary.md#boolean). Not Mrs. Boolean and her husband Julian, but the Python [data type](extras/glossary.md#type) that stores one of just two possible values: `True` or `False`. In order to be able to build conditions into our programs, we need first to learn a bit more about booleans and the logic that governs them.

### Logic

Certain statements in Python result in a boolean value. These are all 'logical' statements that ask a 'yes/no' question. The symbols used in them are mostly similar to mathematical notation:

* `>` 'is greater than'
* `<` 'is less than'
* `>=` 'is greater than or equal to'
* `<=` 'is less than or equal to'

Python allows us to combine such symbols with variables and with literal numbers in much the same way as in math:


```python
x = 2
y = 3
z = 7

x > y
```




    False




```python
x >= 2
```




    True




```python
0 < x <= z
```




    True



What if we want to check whether two things are exactly equal? Here there is a small syntactical problem, because the equals symbol `=` is already in use for [assigning](extras/glossary.md#assignment) to a variable. Python therefore uses a double equals symbol `==` to mean 'is equal to' in the mathematical sense.


```python
x == y
```




    False




```python
x == 2
```




    True



`==` is also applicable to strings. As you might expect, it checks whether the contents of the two strings are exactly the same.


```python
name1 = 'David Hasselhoff'
name2 = 'David Hasselhoff'

name1 == name2
```




    True



Remember that lowercase and uppercase letters are not considered to be the same character, and that a space counts as a character.


```python
name1 == 'david hasselhoff'
```




    False




```python
name1 == 'David Hasselhoff '
```




    False



Finally, we may combine or negate logical statements using the Python [keywords](extras/glossary.md#keyword) `and`, `or`, and `not`.


```python
2 + 2 == 4 or 1 > 2
```




    True




```python
2 + 2 == 4 and 1 > 2
```




    False




```python
not 2 + 2 == 4
```




    False



As in math, parentheses are not always necessary, but they can help make our program clearer to read.


```python
(2 + 2 == 4) or (1 > 2)
```




    True




```python
not (2 + 2 == 4)
```




    False



Python provides an abbreviation for `not` together with `==`. The symbols `!=` stand for 'is not equal to'.


```python
2 + 2 != 4
```




    False



### Conversion to boolean

That covers the very basics of logical statements in Python. Before we see how to turn logical statements into conditions for carrying out a part of a our program, let's take a brief detour to consider a slight quirk in the way Python handles the boolean data type.

We have learned that some data types can be converted into others, using [built-in](extras/glossary.md#builtin) functions that have the same names as the type we wish to convert to (for example `int()` for converting to integer, and `str()` for converting to string). Initially, it may seem strange to allow converting other types into booleans, since booleans are always just `True` or `False`. Is the integer `42` on its own a 'true' number or a 'false' number? What about a string like `'JavaScript is a terrible programming language.'`? (Of course, some strings may contain true statements, but Python can't be expected to work this out.)

Nonetheless, Python does allow us to convert other data types to boolean. How does it decide whether numbers or strings are 'true' or not? If you feel like a challenge, you might like to head to the Spyder console now and try converting a few strings and numbers to boolean (the type conversion function is `bool()`) to see whether you can discover the pattern.

The answer follows after this block of text:


```python
print('SPOILER ALERT ' * 100)
```

    SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT 


Let's try a string first:


```python
bool('JavaScript is a terrible programming language.')
```




    True



That seems like a sensible answer. But what about other strings?


```python
bool('JavaScript is an excellent programming language.')
```




    True



No! That's not right.

In fact, Python treats any string as `True`, with just one exception: an empty string with no characters in it at all:


```python
bool('')
```




    False



This principle generalizes to the other data types. 'Empty' things are `False`, and all other things are `True`. An empty list `[]`, for example, is treated as `False`, but a list that has any contents at all is treated as `True`.


```python
bool([])
```




    False




```python
bool(['eggs', 'bacon', 'black pudding'])
```




    True



For numbers, `0` is the only 'empty number', and all others are treated as `True`.


```python
bool(0)
```




    False




```python
bool(42)
```




    True




```python
bool(-1)
```




    True



This may seem slightly weird. But this convention of treating non-empty things as being somehow 'true' is common to many programming languages. As we will see later, it is important to be aware of this behavior.

## if

Now that we know how to express conditions in Python, we just need to know how to apply them to certain commands, so that those commands are only carried out if the condition is true. The [keyword](extras/glossary.md#keyword) that we need for this is `if`, which has essentially the same meaning in Python as in English.

This is how it is used, applied to the very first condition in our target program:


```python
user_name = input('What is your name and surname? ')

if user_name == 'David Hasselhoff':
    print('Are you THE Hoff?')
```

    What is your name and surname? David Hasselhoff
    Are you THE Hoff?


Because the user entered the exact string `'David Hasselhoff'`, the condition following the `if` keyword [evaluated](extras/glossary.md#evaluate) to `True` and so the `print()` command just below it was executed.

We should always test our conditions with both the positive and negative case to check that we have got them right. So let's try it again, this time entering a name that should not trigger the `print()` command:


```python
user_name = input('What is your name and surname? ')

if user_name == 'David Hasselhoff':
    print('Are you THE Hoff?')
```

    What is your name and surname? Mildred Bonk


Good. This time we did not see the printed output.

So here is the general [syntax](extras/glossary.md#syntax) for an `if` statement:

* write `if`
* then write your condition
  * this should be something that results in a boolean `True` or `False`
* then write a colon `:`
* underneath all this, write the command (or multiple commands) that should be executed if your condition is true
  * these must be [indented](extras/glossary.md#indentation) (i.e. they should be preceded by spaces to move them rightwards)

### Indentation

That last rule is important. It is the indentation in our example above that marks the `print()` line as 'belonging to' the `if` statement. Let's see what happens if we forget the indentation:


```python
user_name = input('What is your name and surname? ')

if user_name == 'David Hasselhoff':
print('Are you THE Hoff?')
```


      File "<ipython-input-26-fdc1d519ea77>", line 4
        print('Are you THE Hoff?')
            ^
    IndentationError: expected an indented block



The content of this error message is fairly clear: Python was expecting some indentation after the `if` statement.

This use of indentation to mark lines of a program as belonging to a [control statement](extras/glossary.md#control) is specific to Python, and is not a feature of most other programming languages. It is one of Python's most controversial features, and also one of the more challenging things for beginners to get used to.

So let's look at a few more variants of the `if` statement above, to check your understanding of the role of indentation. First of all, an example with more than one indented line after the `if`:


```python
user_name = input('What is your name and surname? ')

if user_name == 'David Hasselhoff':
    print('Are you THE Hoff?')
    print('The really real Hoff?')
```

    What is your name and surname? David Hasselhoff
    Are you THE Hoff?
    The really real Hoff?


Because both of these lines are indented, they both belong to the `if` statement, and so both of them will be run if the condition is true.

Where we have multiple indented lines that all belong together, they must all be indented to the same extent. Varying indentation doesn't just look untidy, it also prevents Python from interpreting our program correctly:


```python
user_name = input('What is your name and surname? ')

if user_name == 'David Hasselhoff':
    print('Are you THE Hoff?')
   print('The really real Hoff?')
```


      File "<tokenize>", line 5
        print('The really real Hoff?')
        ^
    IndentationError: unindent does not match any outer indentation level



If you have written an `if` statement followed by multiple indented lines, you may find it helpful to hold up a ruler to your computer screen to check that the indentation is consistent throughout. This is a technique that even expert Python programmers have to resort to at some point.

![](images/indentation.png)

Now consider what happens in the variation below:


```python
user_name = input('What is your name and surname? ')

if user_name == 'David Hasselhoff':
    print('Are you THE Hoff?')
print('The really real Hoff?')
```

    What is your name and surname? Mildred Bonk
    The really real Hoff?


This one does not result in an error. It is [syntactically](extras/glossary.md#syntax) valid, but it does something a bit different from what we want.

Notice that the user typed in a name that did not make the `if` condition true. So the first `print()` line was not run. But the second `print()` line *was* run. This is because it was not indented. As we learned above, indentation tells Python which lines belong to a control statement. If a line is not indented, it is not influenced by the preceding control statement, and so is always run, just like any normal line of the program. The first 'unindented' line after a block of indented lines marks the end of a control statement's influence, and a return to the normal linear structure of a Python program, where every line is always run.

For the sake of clarity, it is a good idea to also place blank lines before and after a block of indented lines, to mark them out clearly from the rest of the program.

### Debugging

If you are trying to write an `if` statement and you keep encountering [errors](extras/glossary.md#error), here are some of the most common mistakes to check for:

* Have you forgotten the colon `:` at the end of the if statement?
* Have you used `=` where you meant to use `==`?
* Have you forgotten to indent, or indented inconsistently?

## if elif else

We now have the main ingredient of our target program: conditional statements. Most of the rest of what we will learn in this lesson is elaborating on this basic ingredient.

The English-language description of our target program is structured as a series of conditions. The first begins with 'if', subsequent ones begin with 'else if', and the last begins simply with 'else'. That is, we want to keep checking a series of conditions until we find one that is true, and have a final 'last resort' condition that only applies if none of the others was true. This is fairly easy to put together, so long as we remember the basic syntax for a conditional statement. We just need to introduce new [keywords](extras/glossary.md#keyword).

Python abbreviates 'else if' to `elif`. The `elif` keyword checks a new condition, but only if none of the preceding conditions was true.

'Else' is the same in Python as it is in English. The `else` keyword does not require any condition, since it merely specifies what to do if none of the preceding conditions was true. But like all [control statements](extras/glossary.md#control) it does still require a colon.

Let's see an `if` ... `elif` ... `else` structure in action, using a simplified version of our target program:


```python
user_name = input('What is your name and surname? ')

# Get the separate names and initials.
user_names = user_name.split()
user_firstname = user_names[0]
user_surname = user_names[1]
user_initials = user_firstname[0] + user_surname[0]

if user_name == 'David Hasselhoff':
    print('Are you THE Hoff?')
elif user_surname == 'Hasselhoff':
    print('Any relation to David Hasselhoff?')
elif user_initials == 'DH':
    print('You have the same initials as David Hasselhoff!')
else:
    print("Never mind, I suppose you could change it to something more interesting, like 'David Hasselhoff'.")
```

    What is your name and surname? Dafydd Hasselhoff
    Any relation to David Hasselhoff?


(If you are wondering about that bit where we extract the user's two names and initials, go to the Spyder console and explore the string [method](extras/glossary.md#method) `split()` and also look back at [indexing](extras/glossary.md#index).)

The user entered 'Dafydd Hasselhoff', and this triggered the first `elif` statement, on line 11 above. Notice that the condition for the second `elif` statement is also true, since Dafydd Hasselhoff's initials are also 'DH', but this second `elif` was not triggered; an `elif` statement is only applied if none of the preceding conditions was true.

Notice also the pattern of indentation. The additional [control statements](extras/glossary.md#control) with `elif` and `else` are not themselves indented, but the `print()` commands that belong to them are.

## Nested conditions

We need one more major insight into Python's [syntax](extras/glossary.md#syntax) for conditionals before we are ready to write a complete version of our target program. For the first two conditions in our program (whether the full name is 'David Hasselhoff' or the surname is 'Hasselhoff'), we need to ask a follow up question and then apply another condition to the answer to that follow-up question. We can almost achieve this already using the techniquess we have just learned, if we add a little leap of imagination.

Remember that Python uses [indentation](extras/glossary.md#indentation) to mark lines of a program as belonging to a preceding control statement. If we have one control statement inside another (for example one condition that only needs to be checked once another has been found to be true), then the lines that belong to the 'inner' control statement must be indented yet further, to indicate that they belong to that inner control statement and not to the 'outer' one.

This is easiest to understand by just looking at an example. So here is the first condition of our program, with the additional follow-up question added:


```python
user_name = input('What is your name and surname? ')

if user_name == 'David Hasselhoff':
    is_hoff = input('Are you THE Hoff? ')
    if is_hoff == 'yes':
        print('Wow!')
        print("That's amazing!")
```

    What is your name and surname? David Hasselhoff
    Are you THE Hoff? no


The user answered 'no' to the second question we posed, so the 'inner' `if` statement was not triggered, and the indented lines that followed it were not run.

And note that if the first `if` statement is not triggered, none of the rest is run:


```python
user_name = input('What is your name and surname? ')

if user_name == 'David Hasselhoff':
    is_hoff = input('Are you THE Hoff? ')
    if is_hoff == 'yes':
        print('Wow!')
        print("That's amazing!")
```

    What is your name and surname? Mildred Bonk


Again, to really firm up our understanding of the role of indentation, let's consider a variation that behaves differently:


```python
user_name = input('What is your name and surname? ')

if user_name == 'David Hasselhoff':
    is_hoff = input('Are you THE Hoff? ')
    if is_hoff == 'yes':
        print('Wow!')
    print("That's amazing!")
```

    What is your name and surname? David Hasselhoff
    Are you THE Hoff? no
    That's amazing!


This time, the second `print()` was indented, but only to the same extent as the other lines that follow the 'outer' `if` statement. This marks it as belonging to the outer `if` statement, so it is run if the outer `if` condition is true, regardless of whether the 'inner' one is also true.

You can think of the role of indentation in Python as similar to its role in a series of nested bullet points in an ordinary document:

* This is a bullet point.
  * This is a sub-point related to the first.
  * So is this.
    * And this is a sub-sub-point related to the one just above.
  * But this is back to being a sub-point related to the very first one.
* And this finally is just yet another bullet point in the main list of bullet points.

## More debugging

We haven't yet attempted the last condition in our target program, which checks whether the user's first name is one of a few variants of 'David'. Let's give it a try. We will for now skip the preceding conditions, and also ask only for the user's first name, just to keep the example clear and simple.

We learned earlier that we can combine conditions using the `or` [keyword](extras/glossary.md#keyword), and that this keyword seems to have more or less the same meaning as it does in English. So how about this:


```python
user_firstname = input('What is your name? ')

if user_firstname == 'Dave' or 'Dafydd':
    print("Your name is a bit like 'David', as in 'David Hasselhoff'.")
```

    What is your name? Dafydd
    Your name is a bit like 'David', as in 'David Hasselhoff'.


That looks right. But we should always test our conditions with both the positive and the negative case:


```python
user_firstname = input('What is your name? ')

if user_firstname == 'Dave' or 'Dafydd':
    print("Your name is a bit like 'David', as in 'David Hasselhoff'.")
```

    What is your name? Mildred
    Your name is a bit like 'David', as in 'David Hasselhoff'.


What just happened? The user entered 'Mildred', which shouldn't trigger the `if` statement. But it did. Our program did not work as expected. We did not get an [error](extras/glossary.md#error), it is just that the program's behavior is wrong. This can be the hardest kind of problem to diagnose.

Let's check a few things step by step. First of all, did the `input()` function really correctly store what the user entered?


```python
print(user_firstname)
```

    Mildred


Ok. Does the first bit of the `if` condition somehow not work properly?


```python
if user_firstname == 'Dave':
    print('triggered')
else:
    print('not triggered')
```

    not triggered


That still seems right. So is it the full condition that is the problem?


```python
if user_firstname == 'Dave' or 'Dafydd':
    print('triggered')
else:
    print('not triggered')
```

    triggered


Aha! So it seems to be the inclusion of `or` that is the problem. Let's confirm with another example, using some other string than the user's name:


```python
if 'Ishmael' == 'Dave' or 'Dafydd':
    print('triggered')
else:
    print('not triggered')
```

    triggered


So what was going on in the statements above?

In everyday English, the word 'or' can be used to join a set of possible alternatives, as in 'Dave, or Davy, or Dafydd'. In logic, and in Python, 'or' has a more specific meaning. It means:

* Look to the left of the 'or', and find out whether the statement written there is true.
* Independently of whatever is to the left, look to the right of the 'or', and find out whether the statement written there is true.
* If at least one of the two statements is true, the whole statement is true.

So `or` expects to find a fully-formed logical statement on either side of itself. This was the case in our earlier example of `or`, in which either side of the `or` was a complete statement on its own:


```python
2 + 2 == 4
```




    True




```python
1 > 2
```




    False




```python
(2 + 2 == 4) or (1 > 2)
```




    True



If `or` expects to find a fully-formed logical statement on either side of itself, why did our condition for the user's name not simply result in an error? After all, `'Dafydd'` is not a fully-formed logical statement on his own.

Remember the slightly weird convention that all non-empty things are `True` when converted to [boolean](extras/glossary.md#boolean). So for the purposes of logical conditions, `'Dafydd'` is `True`, as is any non-empty string. This means that the statement `user_firstname == 'Dave' or 'Dafydd'` is always `True`, regardless of what the contents of the `user_firstname` variable are, because at least one of the two things either side of the `or` is `True`.

So here is the correct way to use `or` in our example. Each side of the `or` must be a statement involving the `user_firstname` variable:


```python
user_firstname = input('What is your name? ')

if user_firstname == 'Dave' or user_firstname == 'Dafydd':
    print("Your name is a bit like 'David', as in 'David Hasselhoff'.")
```

    What is your name? Mildred


## in

Using `or` to join up multiple statements that all check the same variable quickly gets tedious and difficult to read. For example if we want to check three variants of 'David' rather than just two, the condition would be:


```python
user_firstname == 'Dave' or user_firstname == 'Davy' or user_firstname == 'Dafydd'
```




    False



There is a better option in such cases. If we want to check whether a variable has one of several possible values, we can ask whether that variable's value is 'in' a [list](extras/glossary.md#list) of possibilities, using the `in` [keyword](extras/glossary.md#keyword).

For example:


```python
user_firstname in ['Dave', 'Davy', 'Dafydd']
```




    False



So if you ever find yourself checking multiple possible values of a variable using `or`, consider using `in` instead.

That concludes the techniques necessary to write a basic version of our target program. You can take a look at the finished version [hoff.py](examples/hoff.py). This program looks quite complex, but it is made of the building blocks we wrote above, with some very small refinements. Some extra blank lines have been added to clearly separate the multiple conditions that are checked.

## Handling errors

Let's conclude by learning about another kind of control statement. To keep things simple, we won't incorporate it into **hoff.py**, though it could be useful there too.

We have met [errors](extras/glossary.md#error) before. Some errors are just fatal for our program, and will always stop it from running. For example, there is nothing that Python can do about a `SyntaxError`; if we have written something that it just does not understand, then Python has to give up:


```python
Python, please do some amazing machine learning.
```


      File "<ipython-input-47-925621985029>", line 1
        Python, please do some amazing machine learning.
                        ^
    SyntaxError: invalid syntax



Other errors, however, are not necessarily fatal for our program.

Consider an abbreviated version of one of our earlier programs, [age_next_year.py](examples/age_next_year.py), and see what happens if the user misunderstands what is required of them, and enters some input that our program cannot handle:


```python
age = input('How old are you? ')

age_next_year = int(age) + 1
print(age_next_year)
```

    How old are you? fifty-two



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-48-3266fdc533a9> in <module>
          1 age = input('How old are you? ')
          2 
    ----> 3 age_next_year = int(age) + 1
          4 print(age_next_year)


    ValueError: invalid literal for int() with base 10: 'fifty-two'


It is pretty clear what has gone wrong, but in case we aren't sure, the error message identifies the conversion of the string `'fifty-two'` to integer as the problem.

This error is not a `SyntaxError`; our program is entirely [syntactically valid](extras/glossary.md#syntax). Instead, it is a `ValueError`. We have asked Python to do something with a variable, and the thing that we have asked for might be totally ok, it is just that the specific [value](extras/glossary.md#value) of the variable turns out not to be suitable for what we asked for. Here, for example, we have asked for conversion from string to integer, but the string variable does not contain a suitable number.

Problems like this one can be dealt with without stopping our program, because they don't make it impossible for Python to understand what we want. A non-fatal error (i.e. one that does not completely flummox Python) is termed an '[exception](extras/glossary.md#exception)'. When an exception occurs, we have the option of dealing with it in some way, and it is only if we do not deal with it that it becomes an [error](extras/glossary.md#error) and stops the program. (Though in practice you will hear many people use the terms 'exception' and 'error' as synonyms.)

If we wish, we can instruct Python to 'try' to do something, but then to do something else if doing the first thing results in an exception. This concept is very similar to an `if` condition, but the condition is 'if the following actions result in an exception'. To apply this, we need to specify two things. We need to say what actions we want to 'try', and what actions we want to carry out if an exception occurs while trying those actions. There are new [keywords](extras/glossary.md#keyword) `try` and `except` for each of these, respectively.

Let's see an example:


```python
age = input('How old are you? ')

try:
    age_next_year = int(age) + 1
    print(age_next_year)
except ValueError:
    print('That is not a valid age.')
```

    How old are you? fifty-two
    That is not a valid age.


The general [syntax](extras/glossary.md#syntax) for this kind of statement is:

* write `try`, followed by a colon `:`
* then write the actions you want to try
  * these should be [indented](extras/glossary.md#indentation)
* write `except`
* then write the name of the type of exception/error that might occur
* then write a colon `:`
* then write the alternative actions
  * these too should be indented

There are some similarities with the syntax for the `if` ... `else` statement, namely the colon and the indentation. Both of these things are part of the general syntax for all [control statements](extras/glossary.md#control), and we will encounter them again in later lessons.

Let's see another example, this time to handle the possibility that the user asks for a list item that is beyond the length of the list:


```python
shopping_list = ['eggs', 'bacon', 'black pudding']

item_number = input('What item of shopping would you like to see? ')
item_number = int(item_number) - 1

try:
    print(shopping_list[item_number])
except IndexError:
    print("There aren't that many items of shopping.")
```

    What item of shopping would you like to see? 9000
    There aren't that many items of shopping.


How did I know that the exception to watch out for was `IndexError`? In a long career filled with silly programming mistakes I have seen a lot of error messages, and so I just know what a lot of the common exceptions will be. But if you are building a program and you want to write a `try` ... `except` to deal with an expected problem, then the first thing you should do is to go to the console and deliberately provoke that expected problem to see what type of exception it is. The type of exception is printed at the bottom of the error message.


```python
shopping_list[9000]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-51-4a4ff19f7982> in <module>
    ----> 1 shopping_list[9000]
    

    IndexError: list index out of range


The glossary entry on [exceptions](extras/glossary.md#exception) lists some of the most common types of exception that you might encounter.

It is important not to get carried away with `try` ... `except` and attempt to cover all possible problems so that your program is 'foolproof'. If something occurs that your program is just not supposed to deal with, then your program should stop, and this is ok. Error messages can be very informative; if you try to suppress them all, you won't be warned when your program fails or be told why it failed. Use `try` ... `except` to deal with specific, anticipated problems.

## Exercises

### 1

Take a look at the finished [hoff.py](examples/hoff.py) program. One thing that is not so good about this program is that it is not very easily modifiable. If we later changed our minds and wanted to adapt this program so that 'Barbra Streisand' is the interesting name instead of 'David Hasselhoff', then we would need to change the name in at least 8 different places. And we would need to go quite far down in our program to find the list of names similar to 'David' and change that.

Re-write this program so that the string `'David Hasselhoff'` only appears once at the very beginning of the program, and the list of variants of 'David' also appears once at the beginning of the program. Once you have improved the program in this way, check that it still works as it did before. Then check that you only need to change these two initial lines so that the whole program uses a different interesting name. For example, you can try 'Barbra Streisand', with 'Barbara', 'Barb', and 'Barbie' as the variants of 'Barbra'.

(Improving a program but without changing its basic functionality is called [refactoring](extras/glossary.md#refactor) the program.)

### 2

Write a new program. The program asks the user for the answers to three questions:

* How old are they?
* How tall are they (in meters)?
* Do they have their parents' permission to ride rollercoasters?

Then tell the user whether they are allowed to ride the rollercoaster at the theme park. The rules are:

* They must be at least 10 years old.
* They must be at least 1 meter and 30 centimeters tall.
* They cannot be taller than 2 meters.
* If they are younger than 14 years old, they must have their parents' permission.

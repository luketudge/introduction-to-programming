<h1>Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Objective" data-toc-modified-id="Objective-1">Objective</a></span></li><li><span><a href="#Loops" data-toc-modified-id="Loops-2">Loops</a></span></li><li><span><a href="#Iterables" data-toc-modified-id="Iterables-3">Iterables</a></span><ul class="toc-item"><li><span><a href="#range" data-toc-modified-id="range-3.1">range</a></span></li><li><span><a href="#Dictionaries" data-toc-modified-id="Dictionaries-3.2">Dictionaries</a></span></li></ul></li><li><span><a href="#Indentation-again" data-toc-modified-id="Indentation-again-4">Indentation again</a></span></li><li><span><a href="#while-loops" data-toc-modified-id="while-loops-5">while loops</a></span><ul class="toc-item"><li><span><a href="#Debugging" data-toc-modified-id="Debugging-5.1">Debugging</a></span></li></ul></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-6">Exercises</a></span><ul class="toc-item"><li><span><a href="#1" data-toc-modified-id="1-6.1">1</a></span><ul class="toc-item"><li><span><a href="#a)" data-toc-modified-id="a)-6.1.1">a)</a></span></li><li><span><a href="#b)" data-toc-modified-id="b)-6.1.2">b)</a></span></li><li><span><a href="#c)" data-toc-modified-id="c)-6.1.3">c)</a></span></li></ul></li><li><span><a href="#2" data-toc-modified-id="2-6.2">2</a></span></li></ul></li></ul></div>

# Iteration

In the [previous lesson](conditions.md) we learned about [control statements](extras/glossary.md#control): lines of our program that do not themselves accomplish any action, but instead control something about when other lines of our program are run. That is, they determine the 'flow' of the program. We focused on 'conditional' control statements, which set a condition according to which further lines of the program are either run or not.

There are other ways in which we might want to control the flow of our program. For example, we might want to run a certain line more than once, maybe many times, or even indefinitely until a certain goal is achieved. Repeating lines of our program is sometimes termed '[iteration](extras/glossary.md#iterable)'. This is what we will learn about now.

## Objective

As before, let's structure our learning by working towards a simple toy program.

**guess_the_animal.py**

* Make the computer 'think' of an animal (i.e. store the name of an animal in a variable).
* Present the user with a series of six hints about the animal's identity.
* For each hint, print it out and then ask the user to guess the animal.
  * Allow them to give up by typing 'q'.
  * If they just enter nothing, ask them again.
  * If they get the answer right, stop the game and congratulate them
  * If they get the answer wrong, continue to the next hint.

There is some branching in this program too, so we will need to use the techniques from the previous lesson. The novel aspect is the fact that there is some repetition; we need to get and process user input at least six times. Of course, for just six repetitions, we could achieve this by just copying and pasting the same lines into our program six times over. But achieving repetition by literally writing the same lines over an over is a bad idea, for a few reasons:

* **Clarity**. It makes our program unnecessarily long and difficult for others to read.
* **Robustness**. We can easily make small mistakes while copying, pasting, and modifying the repeated lines. This may break our program.
* **Flexibility**. If we later decide that we would like to change some aspect of the repeated actions, we must change it in multiple places in our program. This is laborious, and may again introduce mistakes if we forget to make the change in one of the repetitions.

In programming, we should try to avoid repeating ourselves. This principle is so fundamental that there is a commonly-used acronym [DRY](https://en.wikipedia.org/wiki/Don't_repeat_yourself) (**D**on't **R**epeat **Y**ourself) that people use to remind each other of it. The opposite of a 'DRY' programming style is sometimes pejoratively termed a 'WET' programming style (variously either '**W**rite **E**verything **T**wice' or '**W**e **E**njoy **T**yping').

## Loops

One way of achieving repetition is to use a [sequence](extras/glossary.md#sequence). Remember that sequences are [data types](extras/glossary.md#type) that store multiple values in order, such as [tuples](extras/glossary.md#sequence) and [lists](extras/glossary.md#list). We have in fact already seen one way of performing an action repeatedly for each item in a sequence. Remember that list [comprehensions](extras/glossary.md#comprehension) create a new list by systematically applying the same action to all the items in another list, in order.

Here again is one of the example comprehensions that we saw in the [lesson on sequences](sequences_mappings.md):


```python
shopping_list = ['eggs', 'bacon', 'black pudding']

shopping_notes = [item[:2].upper() for item in shopping_list]

shopping_notes
```




    ['EG', 'BA', 'BL']



Comprehensions are great for applying single short commands to every item in a sequence. But in our target program we would like to go through the sequence of animal clues and do not just one but lots of things for each hint, including printing it out, getting user input, applying conditions, and even asking the user repeatedly for input if they fail to enter something. For such cases, we need to group all the repeated actions together under a [control statement](extras/glossary.md#control) that instructs Python to repeat all of them. This pattern is known as a [loop](extras/glossary.md#loop). Here is a short example:


```python
for item in shopping_list:
    print('Next item of shopping:')
    print(item)
print('Finished.')
```

    Next item of shopping:
    eggs
    Next item of shopping:
    bacon
    Next item of shopping:
    black pudding
    Finished.


By now the general syntax for control statements should be familiar. We end the control statement with a colon `:`, and we indent the lines that belong to the control statement. Make sure again that you have understood the role of [indentation](extras/glossary.md#indentation) in Python. Consider for example what happens if we also indent the final line in the example above:


```python
for item in shopping_list:
    print('Next item of shopping:')
    print(item)
    print('Finished.')
```

    Next item of shopping:
    eggs
    Finished.
    Next item of shopping:
    bacon
    Finished.
    Next item of shopping:
    black pudding
    Finished.


If the final `print()` line is indented, Python considers it to be part of the loop, and so it will be repeated along with the other lines.

Perhaps the only truly novel and potentially confusing aspect of the syntax for a loop is the role of the new variable that is defined after the `for` keyword (in this case `item`). This variable stands for each item in whatever list follows the `in` keyword (in this case `shopping_list`). As was the case for [comprehensions](extras/glossary.md#compehension), the variable that we define after `for` can have any valid variable name that we like. It does not have to be `item`. It matters only that we be consistent in referring to this same variable name wherever we mean 'the current item in the list'.

So for example we could define it as something arbitrary like `x`, and the effect would be the same so long as we also refer to `x` among the commands that are indented after the `for` statement:


```python
for x in shopping_list:
    print('Next item of shopping:')
    print(x)
```

    Next item of shopping:
    eggs
    Next item of shopping:
    bacon
    Next item of shopping:
    black pudding


## Iterables

A [data type](extras/glossary.md#type) containing items that can be 'worked through' one by one is called an '[iterable](extras/glossary.md#iterable)' type. [Lists](extras/glossary.md#list) are iterable, as are [tuples](extras/glossary.md#tuple).

[Strings](extras/glossary.md#string), too, are iterable. If we put a string variable in a `for` statement, the resulting loop will iterate through each character in the string. For example:


```python
name = 'Mildred'

for letter in name:
    print('Next letter in this name:')
    print(letter)
```

    Next letter in this name:
    M
    Next letter in this name:
    i
    Next letter in this name:
    l
    Next letter in this name:
    d
    Next letter in this name:
    r
    Next letter in this name:
    e
    Next letter in this name:
    d


Some [types](extras/glossary.md#type) are obviously not iterable. We can't iterate with a single number, as there are no multiple values to go through. The resulting [error message](extras/glossary.md#error) is pretty clear.


```python
for x in 42:
    print(x)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-3bceb7bd5fef> in <module>
    ----> 1 for x in 42:
          2     print(x)


    TypeError: 'int' object is not iterable


### range

The curious 'range' type that we learned about in the [lesson on sequences](sequences_mappings.md) is iterable. Iteration with `range()` iterates through the integers in the specified range (remember, up to *but not including* the specified end of the range):


```python
for x in range(1, 11):
    print(x, 'squared is', x**2)
```

    1 squared is 1
    2 squared is 4
    3 squared is 9
    4 squared is 16
    5 squared is 25
    6 squared is 36
    7 squared is 49
    8 squared is 64
    9 squared is 81
    10 squared is 100


### Dictionaries

And [dictionaries](extras/glossary.md#dictionary) are iterable as well. By default, a loop through a dictionary iterates through the [keys](extras/glossary.md#key) in the dictionary, not the values stored under those keys:


```python
info = {'name':'Mildred Bonk', 'age':22, 'location':'USA'}

for x in info:
    print(x)
```

    name
    age
    location


If we want instead to iterate through the values, then we can use the dictionary [method](extras/glossary.md#method) `values()`, which gets only the values from the dictionary (remember the '`.`' syntax for using methods):


```python
for x in info.values():
    print(x)
```

    Mildred Bonk
    22
    USA


More often, if we use a dictionary in a loop we would like to go through both the keys and the values. The dictionary method `items()` gives us each entire *item* in the dictionary, and each of these items is a pair consisting of a key together with the value associated with that key. To make use of more than one variable in our loop, we must separate the two with a comma:


```python
for key, value in info.items():
    print(key, ':', value)
```

    name : Mildred Bonk
    age : 22
    location : USA


The syntax here starts to look a bit more complex. So let's consider another example in which we have more than one variable following the `for`.

The Python [built-in](extras/glossary.md#builtin) function `enumerate()` is like an equivalent of `items()` but for lists (or other [iterables](extras/glossary.md#iterable)) instead of just for dictionaries. If we iterate with `enumerate()`, then the pairs that we get consist of the integer index in the list (i.e. the numbers `0`, `1`, `2`, and so on) together with the corresponding item in the list:


```python
for index, item in enumerate(shopping_list):
    print(index+1, ':', item)
```

    1 : eggs
    2 : bacon
    3 : black pudding


## Indentation again

To once again test our understanding of the role of [indentation](extras/glossary.md#indentation) in Python [syntax](extras/glossary.md#syntax), let's look at an example of a *loop within a loop*. This is similar in structure to the example program [hoff.py](examples/hoff.py) from the [previous lesson](conditions.md), in which we saw some conditions 'nested' inside other conditions.

Here it is:


```python
spelling_bee = ['Mississippi', 'isosceles', 'cosecant']

for word in spelling_bee:
    print("The letters in '{}' are:".format(word))
    for index, letter in enumerate(word):
        print(index+1, ':', letter)
    print('')

print('End of the spelling bee.')
```

    The letters in 'Mississippi' are:
    1 : M
    2 : i
    3 : s
    4 : s
    5 : i
    6 : s
    7 : s
    8 : i
    9 : p
    10 : p
    11 : i
    
    The letters in 'isosceles' are:
    1 : i
    2 : s
    3 : o
    4 : s
    5 : c
    6 : e
    7 : l
    8 : e
    9 : s
    
    The letters in 'cosecant' are:
    1 : c
    2 : o
    3 : s
    4 : e
    5 : c
    6 : a
    7 : n
    8 : t
    
    End of the spelling bee.


The outer loop goes through all the items in the list `spelling_bee`. The lines that are indented to mark them as belonging to the outer loop include one line that itself begins a new loop, going through each letter in the string `word`. The single line that is associated with this inner loop (line 6) is indented yet further, to indicate that it should be repeated for every single letter, not just for every single item. The `print()` statement on line 7 (which serves simply to introduce a blank line in the output, for the sake of neatness) is back at the outer loop's level of indentation, so it is repeated only for each word. Were line 7 to be indented as far as line 6, there would be a blank line in the output after every single letter.

So, armed with this knowledge, we are ready to have a first stab at writing a basic version of our target program. We begin by defining the name of the secret animal and the list of hints (we won't write all six hints yet, to keep the example short). Then we use a loop to go through the hints, ask for a guess after each one, then check the guess and print out an appropriate message depending on whether it was correct or not.


```python
correct_answer = 'african swallow'

hints = ['weighs five ounces',
         'beats its wings 43 times per second',
         'is not migratory']

print("I'm thinking of an animal.")

for h in hints:

    print('Hint: It {}.'.format(h))
    guess = input('What is it? ')
    
    if guess == correct_answer:
        print('Correct!')
    else:
        print("No, that's not it.")

print('The end.')
```

    I'm thinking of an animal.
    Hint: It weighs five ounces.
    What is it? gerbil
    No, that's not it.
    Hint: It beats its wings 43 times per second.
    What is it? african swallow
    Correct!
    Hint: It is not migratory.
    What is it? But I got it right already!
    No, that's not it.
    The end.


This initial version of our target program doesn't work quite as we want, as we can see from the example run above. Here, the user guessed the animal correctly already after the second hint. Nonetheless, our program continued iterating through the remaining hints. This is only to be expected. There is no instruction in our program that says 'stop' if the user guesses correctly, so Python obligingly finishes the loop that we asked for.

The `break` [keyword](extras/glossary.md#keyword) 'breaks out' of the current loop, even if not all of the requested items have yet been processed.

So to fix this bug, we just need to add a `break` in the right place in our program (line 10 below):


```python
print("I'm thinking of an animal.")

for h in hints:

    print('Hint: It {}.'.format(h))
    guess = input('What is it? ')
    
    if guess == correct_answer:
        print('Correct!')
        break
    else:
        print("No, that's not it.")

print('The end.')
```

    I'm thinking of an animal.
    Hint: It weighs five ounces.
    What is it? african swallow
    Correct!
    The end.


Great!

You might already be able to see how we can use `if` and `break` in much the same way to implement the 'quit' option that we wanted to include in the program. If you would like to test your understanding, open yourself a new text file in the Spyder editor, copy in the program so far from the sections above, and then see whether you can add in the quit option. Remember to test your attempt carefully by running it a few times and entering different user input when prompted in the console.

## while loops

There is one major ingredient still missing from our program so far. We said that if the user fails to type anything at all (i.e. they just press 'return' in the console), then we want to keep asking them for a guess until they at least type something.

First of all, let's check for ourselves what even happens to the `guess` variable if the user enters nothing at all after the `input()` prompt:


```python
guess = input('What is it? ')

guess
```

    What is it? 





    ''




```python
type(guess)
```




    str



We see that the [return value](extras/glossary.md#return) of `input()` is still a [string](extras/glossary.md#string), even if the user does not enter any characters. It is just an 'empty' string: `''`. So the condition that we need to check in order to decide to ask the user again is whether their guess is an empty string:


```python
guess == ''
```




    True



There are in fact a few functionally equivalent ways in which we could check this. For example, we could also ask whether the length of the `guess` string is `0`:


```python
len(guess) == 0
```




    True



Or if you were paying attention when we learned about the conventions by which other [types](extras/glossary.md#type) are converted to [boolean](extras/glossary.md#boolean) `True` and `False` values, you may remember that empty strings are treated as being 'false'. So in fact we can just apply logical negation to the `guess` string itself to find out if it is empty:


```python
not guess
```




    True



That last way of doing it is a bit unintuitive though. And `len(guess) == 0` doesn't make it absolutely clear that we are dealing with an empty *string*. All else being equal, it is better to be explicit about our intentions and expectations when we write a program. If we want to check whether the user's input was an empty string, then let's check explicitly for exactly that.

So here is a snippet of our program to test out just the part where we re-ask the user for a guess if they didn't enter one:


```python
guess = input('What is it? ')

if guess == '':
    guess = input('Enter the name of an animal: ')

guess
```

    What is it? 
    Enter the name of an animal: gerbil





    'gerbil'



That works out ok. But the problem we have is that a standard `if` statement only checks the condition *once*. If the user has fallen asleep with excitement and is resting their forehead against the return key on their keyboard, then the program will still accept their second empty guess:


```python
guess = input('What is it? ')

if guess == '':
    guess = input('Enter the name of an animal: ')

guess
```

    What is it? 
    Enter the name of an animal: 





    ''



This bug can be fixed with yet another new [keyword](extras/glossary.md#keyword). The `while` keyword creates a new kind of [loop](extras/glossary.md#loop) a bit like the `for` loop that we learned about above. But instead of repeating the indented lines once for every item in a list (or other [iterable](extras/glossary.md#iterable), a `while` loop repeats the lines for as long as a given condition is true. In this sense, a `while` loop is a combination of a loop and an `if` statement. The syntax is exactly the same as for an `if` statement, only with `while` in place of `if`.

Let's see this applied to our snippet:


```python
guess = input('What is it? ')

while guess == '':
    guess = input('Enter the name of an animal: ')

guess
```

    What is it? 
    Enter the name of an animal: 
    Enter the name of an animal: 
    Enter the name of an animal: gerbil





    'gerbil'



### Debugging

Be careful with `while`. Because it repeats certain lines of our program indefinitely, we can get stuck running those lines *forever* if we forget to put something into the indented text of the `while` loop that could stop it. When you write a `while` loop, check that among the indented lines below it there is something that can stop the loop, either a `break`, or a command that can make the condition in the `while` control statement false.

If you run your program and you discover that you have made a mistake and it wants to run until the end of the universe, remember that you can stop a running program either by clicking the red stop square at the top of the console, or by pressing the key combination *ctrl* + *c*.

That's it, we now know everything we need to know in order to write our target program. At least in principle. If you feel like a challenge, you might like to have a go at finishing off the program yourself before you take a look at the finished example, [guess_the_animal.py](examples/guess_the_animal.py).

If you want to add some extra hints about African swallows, you can find some facts about them [here](http://montypython.50webs.com/scripts/Holy_Grail/Scene1.htm).

## Exercises

### 1

Open up our example program [guess_the_animal.py](examples/guess_the_animal.py) in the Spyder editor. Or, if you already wrote your own version of the program and you have made it work correctly, open that. Modify the program to add the following new features:

#### a)

Before each hint is printed, print a heading that announces which round of the game the user is currently on. So for example the printout for the first round should look like:

```
Round 1 ...
Hint: It weighs five ounces.

What is it (or type 'q' to quit)?
```

#### b)

After each guess, tell the user how many hints remain. So for example after the first guess the printout should look like:

```
What is it (or type 'q' to quit)? gerbil
No, that's not it.
4 hints remaining.
```

#### c)

At the end of the game, tell the user how many guesses they needed before getting the correct answer. Omit this if the user did not guess correctly at all. So for example if they got it right already on the second round, the printout at the end should look like:

```
Correct!
It was the african swallow.
You got it after 2 guesses.
```

For all of these modifications, the program should continue to work correctly if you later add more hints to the `hints` list at the top of the file.

### 2

Write a new program. The program helps the user to remember their multiplication tables. Ask the user to enter a number. Then print out for them a helpful text telling them all the multiples of that number, from 1 up to and including 12.

So for example the program might look like this when run in the console:

```
Enter a number to revise your multiplication tables: 7

1 times 7 is: 7
2 times 7 is: 14
3 times 7 is: 21
4 times 7 is: 28
5 times 7 is: 35
6 times 7 is: 42
7 times 7 is: 49
8 times 7 is: 56
9 times 7 is: 63
10 times 7 is: 70
11 times 7 is: 77
12 times 7 is: 84
```

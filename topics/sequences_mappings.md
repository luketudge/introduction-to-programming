# Sequences and mappings

In the [previous lesson](types.md), we learned about some of the different data [types](extras/glossary.md#type) that Python recognizes, and we saw that Python treats each of them differently. In this lesson we will continue learning about types, but we will focus on a few particular types that are especially useful for many programming tasks, and whose behavior it is worth considering in more detail.

## Sequences

We have already met both [tuples](extras/glossary.md#tuple) and [lists](extras/glossary.md#list).


```python
shopping_list = ['eggs', 'bacon', 'black pudding', 'sausages', 'bread', 'Mazola', 'gravy mix']
shopping_tuple = ('eggs', 'bacon', 'black pudding', 'sausages', 'bread', 'Mazola', 'gravy mix')
```

Tuples and lists are both [sequences](extras/glossary.md#sequence). That is, they can contain more than one value, and the values are arranged in order. It is the order of the values that allows us to pick them out individually, using positions in the tuple or list as [indices](extras/glossary.md#index). (Don't forget Python's zero-based indexing system.)


```python
shopping_list[0]
```




    'eggs'



### Indexing

Let's begin by looking at a few more ways of using indices to get items from a sequence. We will take a list as our example, but bear in mind that the examples work for tuples as well (you can create yourself a tuple in the Spyder console and check if you like).

As well as literal numbers, we can use [variables](extras/glossary.md#variable) as indices. In this case, the value of the variable is used as the index.


```python
item_num = 1

shopping_list[item_num]
```




    'bacon'



Indices must be [integers](extras/glossary.md#integer). This makes sense; it is unclear what contents would be stored in 'entry two-and-a-half'.


```python
item_num = 2.5

shopping_list[item_num]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-0f7724690886> in <module>
          1 item_num = 2.5
          2 
    ----> 3 shopping_list[item_num]
    

    TypeError: list indices must be integers or slices, not float


Note the content of the error message above. Python does not accept [float](extras/glossary.md#float) values as indices. This is the case even if the float represents a whole number.


```python
item_num = 2.0

shopping_list[item_num]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-47a72c75adcf> in <module>
          1 item_num = 2.0
          2 
    ----> 3 shopping_list[item_num]
    

    TypeError: list indices must be integers or slices, not float


We saw in the last lesson that for basic arithmetic it often doesn't matter whether we represent numbers as integers or as floats; Python will convert them as necessary. But indexing is a situation in which we definitely need integers.

So if for some reason we end up with a float variable, but we want to use it as an index, we must first convert it to an integer.


```python
item_num = 2.0
item_num = int(item_num)

shopping_list[item_num]
```




    'black pudding'



When might we end up with a float value while working with indices? One semi-common case in which this can occur is if we want to get entries that are part way through the sequence, for example half way. In order to find the halfway point, we can divide the length of the sequence by two. But this will result in a non-whole number if the sequence has an odd number of items (and in fact, as we have seen, the result of division is always a float even if the result is a whole number).


```python
n_items = len(shopping_list)
halfway = n_items / 2

print(halfway)

type(halfway)
```

    3.5





    float



So we must convert the result back into an integer in order to use it as an index. This also 'rounds down' the number to its whole part.


```python
halfway = int(halfway)

print(halfway)

shopping_list[halfway]
```

    3





    'sausages'



Using negative numbers, we can get entries counting from the end of a sequence rather than from the beginning. So entry `-1` is the last entry, `-2` is the second from last entry, and so on.


```python
shopping_list[-1]
```




    'gravy mix'



What if we use an index that goes beyond the length of the sequence? As with many such questions, the best response is to try it out and see. Then we will know what to look out for if we suspect we have made this mistake in one of our programs. The content of the error message is pretty clear:


```python
shopping_list[9000]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-10-4a4ff19f7982> in <module>
    ----> 1 shopping_list[9000]
    

    IndexError: list index out of range


### Slicing

We can also get multiple entries from a sequence. This is known as taking a '[slice](extras/glossary.md#slice)' of the sequence. We use the same square parentheses we always use for indexing, but this time they contain a range of indices, where the beginning and end of the range are separated by the colon character `:`.

So to get entries `1` and `2` (in the zero-based numbering system):


```python
shopping_list[1:3]
```




    ['bacon', 'black pudding']



Wait a moment! You might have been expecting `[1:3]` to give you entries `1` to `3`, inclusive. If so, you are a normal, healthy person and your worldview is entirely valid. However, Python understands the end of a slice as meaning 'up-to-but-not-including'. So `[1:3]` means 'starting from `1` up to (but not including) `3`'.

If you are still reeling from the shock of the zero-based numbering system, this new quirk may seem like a slap in the face with a wet kipper. However, there is a logic to it that you may eventually come to love, and that can be explained with the help of the fancy infographic below.

![](images/slicing.png)

The indices in Python's indexing system can be understood as referring to the 'dividing' tick marks on a ruler. Indices refer not to the items in a sequence themselves but to the 'boundaries' between the items. So when we ask for slice `[1:3]` we get the items between tick mark `1` and tick mark `3` on the ruler. As you can see in the image above, this gets us the second and third items.

Single indices can be understood in a similar way. When we ask for item `0` in a sequence, we get the item that immediately *follows* that tick mark on the ruler, which is the first item. The second item comes after tick mark `1`, and so on. This is similar to the way that the floors of a building are numbered (at least in most countries). A floor is the part of the building immediately *above* the actual physical platform that divides the building into vertical sections. So the '1st floor' is the space above the first dividing platform. Below that is the 'ground floor', so called because it is located immediately above the ground. (We could also call the ground floor the '[zeroth](https://en.wikipedia.org/wiki/0th)' floor).


```python
floors = ['ground', '1st', '2nd', '3rd']

floors[0:2]
```




    ['ground', '1st']



If the beginning of our desired slice is the beginning of the whole sequence, we can omit the beginning index before the colon. So `[:3]` means simply 'up to but not including `3`'.


```python
shopping_list[:3]
```




    ['eggs', 'bacon', 'black pudding']



And similarly if the end of our desired slice is the end of the sequence.


```python
shopping_list[3:]
```




    ['sausages', 'bread', 'Mazola', 'gravy mix']



Note that in the two last examples above, we were able to use the same index (`3`) both to end one slice and to begin another one, without the two slices 'overlapping' (i.e. both containing item `3`). This is one of the subtle advantages of Python's interpretation of indices as 'dividing lines'.

### Comprehensions

We have seen that the square parentheses can be used to create a list. The items in the list are separated by commas. Often, we will want to create a list without having to write out every individual item explicitly. If there is some regular pattern to the items in our desired list, we can generate them based on that pattern. For example, the pattern might be that the items in our desired list are all related to the items in another list in some consistent way.

We might want to know the length of each item in our shopping list, and to store those lengths in a new list. One way to do this would be to apply the `len()` function to each item separately:


```python
item_lengths = [len(shopping_list[0]), len(shopping_list[1]), len(shopping_list[2])] # ... and so on
```

But this quickly gets tedious (as you can see I couldn't even be bothered to finish the full example above). We are also liable to make small mistakes such as missing out one item or putting them in the wrong order. Python provides an alternative. Take a look at the command below:


```python
item_lengths = [len(x) for x in shopping_list]

item_lengths
```




    [4, 5, 13, 8, 5, 6, 9]



This way of constructing a list is known as a 'list [comprehension](extras/glossary.md#comprehension)'. Instead of writing out each item explicitly, we give a sort of 'formula' for creating the items. The basic [syntax](extras/glossary.md#syntax) for a list comprehension is as follows:

* pick a variable name, any variable name (for example `x`)
* write:
  * `for`
  * then your chosen variable name
  * then `in`
  * then the name of the existing list that your new list is based on (for example our `shopping_list`)
* to the left of this, write your chosen variable name again
* do to this variable whatever it is that creates an item in your new list (for example apply the `len()` function)
* enclose the whole thing in square parentheses

This sort of formula is almost human-readable, if you are a particular kind of human. Our example above says: 'For every item in the shopping list, give me the length of that item (and put all these lengths in a new list)'. We can (and should) make our programs a bit more human-readable by picking more descriptive variable names than `x`. For example:


```python
item_lengths = [len(item) for item in shopping_list]

item_lengths
```




    [4, 5, 13, 8, 5, 6, 9]



List comprehensions can be an extremely useful tool for manipulating data. So here is another example for you to check your comprehension of comprehensions:


```python
item_initials = [item[0] for item in shopping_list]

item_initials
```




    ['e', 'b', 'b', 's', 'b', 'M', 'g']



Though we may choose the name of the variable in a list comprehension (for example `x` or `item`), the roles of the words `for` and `in` are fixed. These are [keywords](extras/glossary.md#keyword) for Python; each has a particular effect on the workings of our program, and we must use that specific word if we want that effect. We will learn more about keywords in later lessons.

### Range

Before we leave sequences behind, let's consider one more data type, a new one this time. Python provides a [built-in](extras/glossary.md#builtin) function `range()` that generates a sequence of integers over a given range. The two [arguments](extras/glossary.md#argument) to `range()` are the start and end of the desired sequence of integers.

For example:


```python
ten_numbers = range(0, 10)
```

Intuitively, we might expect the [return value](extras/glossary.md#return) of `range()` to be a tuple or list containing the requested integers. Unfortunately, it is instead yet another new [data type](extras/glossary.md#type), the `range` type.


```python
type(ten_numbers)
```




    range



We don't need to worry too much about this. Behind the scenes in the bowels of our computer, the `range` data type 'prepares' the requested integers for use, but it doesn't actually put them into a list or give us any of them until we ask it to do so.

We can see this if we try to print out the range variable. We aren't shown all the integers. Instead, we just see that we have a 'range'.


```python
print(ten_numbers)
```

    range(0, 10)


We only get the integers once we request a specific one:


```python
ten_numbers[3]
```




    3



Understanding the reason for this behavior takes us into some of the details of how computers work. When we create a list (or a tuple), it takes up some space in our computer's memory. Although a decent modern computer usually has squigabytes upon squigabytes of memory, the amount is still limited, and not all of that memory will be accessible for Python, as it will be in use by other programs (or by the many viruses that have infected your computer). So if we are working with an extremely large sequence of numbers, for example in a big data analysis, we might prefer to generate each of those numbers one by one, process them, then discard them, rather than first storing them all in memory.

However, for small sequences, the behavior of `range()` can be a bit of an annoyance. We can demand the full list of integers by just converting a range into a list:


```python
ten_numbers = list(ten_numbers)

ten_numbers
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



Notice that the end of a range is interpreted in the same way as the end index of a slice, which we learned about above. `range(5, 10)` means 'the integers from `5` up to *but not including* `10`. Also like slices, we can omit the starting number if we want to start from `0`. So `range(10)` is a shorthand for `range(0, 10)`.

Ranges are often useful for creating a new list that contains some mathematical sequence. For example we can get a list of square numbers by requesting '`x` squared' for every `x` in a range:


```python
squares = [x*x for x in range(1, 11)]

squares
```




    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



#### Aside: Python 2

Back in Python 2, the `range()` function did the more intuitive thing and just returned a full list of the requested integers. This was good for the simplicity and clarity of Python programs, but bad for efficient use of the computer's memory, so it was changed in Python 3.

## Mappings

Consider the list below. It contains someone's name, age, and location.


```python
info = ['Mildred Bonk', 22, 'USA']
```

A list isn't such a great way of storing this information, for a few reasons.

* This list mixes data types (strings and integers). Python allows a list to store items of different types, but it usually isn't a good idea. We can make our programs clearer and less error-prone by storing only one type of data in each list we create.
* The order of the items is somewhat arbitrary. It makes some sense to begin with the name, but there is no particular reason to have age before location or the other way around.
* There is nothing in the list that tells us what each of the items refers to in the real world. We just have to remember that `info[0]` is the name, `info[1]` the age, and so on. For another programmer reading our work, `info[1]` could well be Mildred's shoe size instead.

If we find ourselves wanting to gather together data of different [types](extras/glossary.md#type), and we would like each piece of data to have an informative name, then we need to move on from sequences. We need a 'mapping' instead.

A 'mapping' stores multiple values, just as a sequence does, but instead of storing the values in order and accessing them by their position, it stores them under labels and accesses them by those labels. You may be wondering why this way of storing data is called a 'mapping'. This is because we say that the labels are 'mapped' to the values that they represent. Just as the symbols on an everyday map can be converted into features of the real world, so the labels in a mapping can be converted into the values that they store.

### Dictionaries

As it turns out, there is really only one commonly-used mapping data type in Python. So from here on we will discard the pedantic technical computing term 'mapping' and talk about just this data type. It is called a [dictionary](extras/glossary.md#dictionary).

Let's learn the [syntax](extras/glossary.md#syntax) for creating a dictionary. Then we can create one and see how it works. To create a dictionary, we use a new set of parentheses `{}`, often called 'curly braces'. Just as for a list, we place the individual items of the dictionary inside these parentheses, separated by commas. However, each item in a dictionary needs both a label and a value, so things get slightly more complex. For each item, we write its label first, then its value, and separate the two with a colon `:`.

So here is how we would create a dictionary for our data above:


```python
info = {'name':'Mildred Bonk', 'age':22, 'location':'USA'}

type(info)
```




    dict



We can see that Python abbreviates the term 'dictionary' to 'dict'. We should learn one other important piece of Python vocabulary for dictionaries. Python calls the labels under which a dictionary's values are stored the dictionary's [keys](extras/glossary.md#key).

We can retrieve the values in the dictionary by using the keys as [indices](extras/glossary.md#index). This works using the same square parentheses as for indexing items in a list or tuple:


```python
info['age']
```




    22



If we ask for a key that is not in the dictionary, the result is an error message mentioning a `KeyError`:


```python
info['shoe size']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-28-4f6f7f8b880a> in <module>
    ----> 1 info['shoe size']
    

    KeyError: 'shoe size'


Note that the roles of keys and values are distinct. We use the key to get the value. We cannot use the values to get the keys:


```python
info['USA']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-29-bf82e9f85f00> in <module>
    ----> 1 info['USA']
    

    KeyError: 'USA'


Note also that the items in a dictionary do not have a defined order as they do in a list or tuple. We cannot use integers as indices in order to ask for e.g. the first or second item:


```python
info[0]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-30-cfc788aff63d> in <module>
    ----> 1 info[0]
    

    KeyError: 0


However, a dictionary does have a length, which as we would expect is just the number of items in the dictionary.


```python
len(info)
```




    3



(If you were expecting to see `6` for the length of our dictionary, remember that each *item* consists of a key and value pair; the keys and values are not separate items.)

#### Mutability again

Earlier, we learned that most basic data types, such as [strings](extras/glossary.md#string), are [immutable](extras/glossary.md#mutability); they cannot be changed unless we overwrite them completely with a new [assignment](extras/glossary.md#assignment). And we learned that lists, on the other hand, are mutable. We can change single values in a list, and list [methods](extras/glossary.md#method) change the list without our having to re-[assign](extras/glossary.md#assignment) the result back into the list variable.

Are dictionaries mutable? If a question like this occurs to you while learning about programming, the best thing to do is to ask yourself: What can I try in order to find out? If you are feeling adventurous, you can head to the Spyder console now and try to find out. Create for yourself a short dictionary (for example by copying and pasting the command above that created our `info` dictionary), then see if you can enter some more commands that will test for you whether dictionaries are mutable or immutable.

(I have helpfully generated a block of filler text just below to prevent your eye from wandering down to the answer before you have tried it out.)


```python
print('SPOILER ALERT ' * 100)
```

    SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT SPOILER ALERT 


You might have found various ways of checking whether dictionaries are mutable. But here is one simple one. Remember that one of the features that illustrated the mutability of lists compared to the immutability of tuples was the possibility of changing just one item in the list without re-assigning the whole list:


```python
shopping_tuple[1] = 'organic vegan bacon'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-33-49481c46064b> in <module>
    ----> 1 shopping_tuple[1] = 'organic vegan bacon'
    

    TypeError: 'tuple' object does not support item assignment



```python
shopping_list[1] = 'organic vegan bacon'

shopping_list
```




    ['eggs',
     'organic vegan bacon',
     'black pudding',
     'sausages',
     'bread',
     'Mazola',
     'gravy mix']



So can we change just one item in our dictionary without having to re-assign the whole thing?


```python
info['location'] = 'Canada'

info
```




    {'name': 'Mildred Bonk', 'age': 22, 'location': 'Canada'}



Yes! Dictionaries are mutable.

#### Dictionary methods

Another question we might ask when we encounter a new data type is: What [methods](extras/glossary.md#method) are available for variables of this data type? Remember that we can find this out using the `dir()` function.


```python
dir(info)
```




    ['__class__',
     '__contains__',
     '__delattr__',
     '__delitem__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__setitem__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'clear',
     'copy',
     'fromkeys',
     'get',
     'items',
     'keys',
     'pop',
     'popitem',
     'setdefault',
     'update',
     'values']



There are not so many methods available for dictionaries (ignore the methods enclosed in double underscores `__ __`). There is a method for finding out what keys a dictionary contains, and one for finding out what values it contains (remember the syntax for using a variable's methods):


```python
info.keys()
```




    dict_keys(['name', 'age', 'location'])




```python
info.values()
```




    dict_values(['Mildred Bonk', 22, 'Canada'])



And the `update()` method updates a dictionary's contents with the contents of another dictionary:


```python
new_info = {'height':1.96, 'political affiliation':'unknown'}

info.update(new_info)

info
```




    {'name': 'Mildred Bonk',
     'age': 22,
     'location': 'Canada',
     'height': 1.96,
     'political affiliation': 'unknown'}



The example just above with `update()` demonstrates again the mutability of dictionaries. We used a dictionary method, and this was enough to change the contents of the dictionary. We did not have to write `info = info.update(new_info)`.

We will see dictionaries in several example programs later on. That is enough about them for now.

## Choosing a data representation

Now that we know about sequences and dictionaries, we have quite a few options when it comes to deciding how to represent data in our programs. For example, if we have some data about customers, we could hold them in a tuple, in a list, in a dictionary that maps customer IDs to their information, or in some combination of these types, such as a list containing multiple dictionaries, or vice versa.

Let's look at some basic guidelines when choosing how to represent data.

### Tuple or list?

Lists are [mutable](extras/glossary.md#mutability), whereas tuples are not. For basic purposes, this is really the only important consideration when choosing between these two types. If we want to represent a sequence of values that is defined only once in our program and is then set in stone, then we should choose a tuple. If the values will need to be changed, reordered, or added to, then we should choose a list.

You might wonder why we should ever bother with tuples at all. If a list is like a tuple but can be changed more easily, why not just keep our options open and always choose lists over tuples? Never underestimate your own (and your collaborators') capacity to make small mistakes. If you need to define a sequence of values in your program and you know that those values should not change during one run of your program, then you can play it safe and store them in a tuple. This makes it less likely that some command that you put into your program inadvertently changes the tuple without your being aware of it. It also signals to other people reading your program that these values are not intended to change during the program's execution.

Examples of such 'fixed parameters' might include:

* The (*x*, *y*) dimensions of a static image or dialog window.
* A small collection of known valid words.
* The (*width*, *height*, *depth*) of items of mahogany furniture.

### List or dictionary?

We saw above that a dictionary has [keys](extras/glossary.md#key), which allow us to retrieve the stored values using a name instead of a position. So we should choose a dictionary to represent a collection of items of information each of which has a meaning or label. For example, demographic information about a single user. On the other hand, we should choose a list if all the items in a collection represent instances of the same thing without unique labels. For example multiple user names.

There are also differences in how fast a computer can carry out certain operations on a list or a dictionary. This may become an important consideration in big programs that have to process a lot of data quickly. But this is a topic for later.

## Nested data representations

So far, all our examples of tuples, lists, and dictionaries have contained strings or numbers. But they can also contain other tuples, lists, and dictionaries. For example, we might have a dictionary of lists, in which each [key](extras/glossary.md#key) is a description of a piece of information about customers, and each value is a list storing that piece of information for all customers in the same order.

(Note that for a long statement like this one, Python allows breaking it up into separate lines if the line breaks come after the commas):


```python
customers = {'name':['Mildred', 'Ishmael', 'Sherlock'],
             'age':[22, 19, 39],
             'location':['USA', 'USA', 'GB']}

customers
```




    {'name': ['Mildred', 'Ishmael', 'Sherlock'],
     'age': [22, 19, 39],
     'location': ['USA', 'USA', 'GB']}



We can then get a single item from one of the lists by first writing the [index](extras/glossary.md#index) for the 'outer' dictionary (its [key](extras/glossary.md#key)), then writing the index for the 'inner' list:


```python
customers['age'][0]
```




    22



Is a dictionary of lists a good choice of data representation for the example above?

Not really. The crucial problem is that we intend the values in each list to 'match up', so that e.g. the first value in the `'name'` list is from the same customer as the first value in the `'age'` list, and so on. The dictionary has no way of 'knowing' that this is what we intend, and once we start adding to or sorting the lists, it will not keep this constraint in force.

For example if we change the order of one of the lists, Python does not read our mind and obligingly change the others so that they match up:


```python
customers['name'].reverse()

customers
```




    {'name': ['Sherlock', 'Ishmael', 'Mildred'],
     'age': [22, 19, 39],
     'location': ['USA', 'USA', 'GB']}



A list of dictionaries would be better for this example. Each dictionary keeps one customer's various pieces of information together. We can then sort or add to the 'outer' list without worrying that different customers' information is getting mixed up.


```python
customers = [{'name':'Mildred', 'age':22, 'location':'USA'},
             {'name':'Ishmael', 'age':19, 'location':'USA'},
             {'name':'Sherlock', 'age':39, 'location':'GB'}]

customers
```




    [{'name': 'Mildred', 'age': 22, 'location': 'USA'},
     {'name': 'Ishmael', 'age': 19, 'location': 'USA'},
     {'name': 'Sherlock', 'age': 39, 'location': 'GB'}]




```python
customers.reverse()

customers
```




    [{'name': 'Sherlock', 'age': 39, 'location': 'GB'},
     {'name': 'Ishmael', 'age': 19, 'location': 'USA'},
     {'name': 'Mildred', 'age': 22, 'location': 'USA'}]



Dictionaries of lists still have their uses when the items in different lists are not linked to each other, and so can be manipulated independently. For example:


```python
todos = {'shopping':['eggs', 'bacon', 'black pudding'],
         'chores':['washing up', 'polish silver'],
         'reading':['Moby Dick', 'The Hound of the Baskervilles', 'Python for Everybody']}

todos
```




    {'shopping': ['eggs', 'bacon', 'black pudding'],
     'chores': ['washing up', 'polish silver'],
     'reading': ['Moby Dick',
      'The Hound of the Baskervilles',
      'Python for Everybody']}




```python
todos['reading'].reverse()

todos
```




    {'shopping': ['eggs', 'bacon', 'black pudding'],
     'chores': ['washing up', 'polish silver'],
     'reading': ['Python for Everybody',
      'The Hound of the Baskervilles',
      'Moby Dick']}



As a general helpful guideline: Choose a data representation that makes it hard to do the things that you don't want to happen.

That's all for now. Try some exercises.

## Exercises

### 1

What is the result of the following short Python programs? Try to reason it out first, and then check your answer by typing the commands into the Spyder console.

#### a)

```python
shopping_list = ['eggs', 'bacon', 'black pudding']
shopping_notes = [item[:2].upper() for item in shopping_list]
print(shopping_notes)
```

#### b)

```python
shopping_dict = ['eggs':8, 'bacon':6, 'black pudding':4]
item = 'eggs'
print(shopping_dict[item])
```

#### c)

```python
shopping_dict = ['eggs':'free-range', 'bacon':'danish', 'black pudding':'organic']
print(shopping_dict['bacon'].capitalize())
```

### 2

The Python command below defines a list that contains the top 5 bestselling non-fiction books in the US at the time of writing:

```python
books = ["'Inside Out' by Demi Moore",
         "'The United States of Trump' by Bill O'Reilly",
         "'Talking to Strangers' by Malcolm Gladwell",
         "'Over the Top' by Jonathan Van Ness",
         "'Know My Name' by Chanel Miller"]
```

Copy this command into a new program and then write the rest of the program so that it accomplishes the following:

* Tell the user that you have stored a list of the top 5 bestselling books.
* Ask the user how many of the top 5 they would like to see.
* Print for them those top books.

So for example, the user could choose to view only the top 2 books. Then the program would look like this when run:

```
I have a list of the top 5 bestselling non-fiction books.
How many of the top books would you like to see? 2
The top 2 are:
["'Inside Out' by Demi Moore", "'The United States of Trump' by Bill O'Reilly"]
```

Make sure that your program fulfills one additional requirement. It should still work correctly if you later come back and add more books to the list. You shouldn't need to change the rest of the program if you change the list of books.

# -*- coding: utf-8 -*-
"""
Search texts for violations of prescriptive grammar rules.
"""

import nltk


## A helper function used by all the checking functions.

def tokenize_tag(sentence):
    """Tokenize a sentence and tag with POS tags.
    
    Arguments:
        sentence: A string

    Returns:
        List of (token, tag) tuples.
    """
    
    tokens = nltk.word_tokenize(sentence)
    
    return nltk.pos_tag(tokens, tagset='universal')


## The checking functions.

def endswith_preposition(sentence):
    """Check whether a sentence ends with a preposition.

    Examples:
        >>> endswith_preposition('Who did you go with?')
        True
        >>> endswith_preposition('With whom did you go?')
        False
    
    Arguments:
        sentence: A string

    Returns:
        Boolean.
    """
    
    pos = tokenize_tag(sentence)
    
    for x in reversed(pos):
        if x[1] != '.':
            return x[1] == 'ADP'
        
    return False


def split_infinitive(sentence):
    """Check whether a sentence contains a split infinitive.

    Examples:
        >>> split_infinitive('To boldly go.')
        True
        >>> split_infinitive('To go boldly.')
        True
    
    Arguments:
        sentence: A string

    Returns:
        Boolean.
    """
    
    pos = tokenize_tag(sentence)

    for i in range(len(pos) - 2):
        if pos[i][0].lower() == 'to':
            if pos[i+1][1] == 'ADV':
                if pos[i+2][1] == 'VERB':
                    return True
    
    return False


def startswith_conjunction(sentence):
    """Check whether a sentence starts with a conjunction.

    Examples:
        >>> startswith_conjunction('And it was all a dream.')
        True
        >>> startswith_conjunction('It was all a dream.')
        False
    
    Arguments:
        sentence: A string

    Returns:
        Boolean.
    """
    
    pos = tokenize_tag(sentence)
    
    for x in pos:
        if x[1] != '.':
            return x[1] == 'CONJ'
        
    return False


## An overall function that applies all the checking functions.

VIOLATION_LABELS = {
    'final preposition': endswith_preposition,
    'split infinitive': split_infinitive,
    'initial conjunction': startswith_conjunction,
}


def check_text(text):
    """Check a text for sentences that violate one of the three rules.
    
    Example:
        >>> check_text('And who would you like to boldly go with?')
        ('And who would you like to boldly go with?',
         ['final preposition', 'split infinitive', 'initial conjunction'])

    Arguments:
        text: A string

    Returns:
        Iterator of tuples of (sentence, [violations]).
    """
    
    for s in nltk.sent_tokenize(text):
        violations = [l for l, f in VIOLATION_LABELS.items() if f(s)]
        if violations:
            yield (s, violations)


## A demo showing violations of the rules in an example dialogue.

if __name__ == '__main__':
    
    text = """
    Hello, have you boldly been anywhere lately?
    Why would I want to boldly go anywhere?
    You might have someone special to boldly go with.
    But I don't.
    I have boldly been somewhere, ask me about it.
    Where have you boldly been then?
    To space, the final frontier.
    Did you boldly go with anyone?
    No, but I'd like to.
    And who would you like to boldly go with?
    Captain Kirk, he's a total dreamboat.
    """
    
    for s, violations in check_text(text):
        print(s, violations, '\n')

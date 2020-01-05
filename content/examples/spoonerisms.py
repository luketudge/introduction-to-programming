# -*- coding: utf-8 -*-
"""
Spoonerize word pairs.
"""


VOWELS = 'aieou'


def find_first_vowel(word):
    """Find the first vowel in a word.

    Example:
        >>> find_first_vowel('smart')
        2

    Arguments:
        word: A string

    Returns:
        An integer giving the index of the first vowel.
    """

    for index, letter in enumerate(word):
        if letter.lower() in VOWELS:
            return index


def spoonerize(wordpair):
    """Spoonerize a word pair.

    A spoonerism switches the initial consonant clusters of words.

    Example:
        >>> spoonerize('smart fella')
        'fart smella'

    Argument:
        wordpair: A string containing exactly two words.

    Returns:
        A string containing the spoonerized phrase.

    Raises ValueError:
        If wordpair does not contain exactly two words.
    """

    words = wordpair.split()

    nwords = len(words)
    if nwords != 2:
        error_msg = '{} contains {} words but 2 expected.'
        raise ValueError(error_msg.format(words, nwords))

    word1 = words[0]
    word2 = words[1]

    split1 = find_first_vowel(word1)
    split2 = find_first_vowel(word2)

    head1 = word1[:split1]
    body1 = word1[split1:]
    head2 = word2[:split2]
    body2 = word2[split2:]

    return head2 + body1 + ' ' + head1 + body2


if __name__ == '__main__':

    print(spoonerize('smart fella'))

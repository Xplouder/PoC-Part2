"""
Student code for Word Wrangler game
"""

import urllib2

try:
    import codeskulptor
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    :param list1:
    """
    distinct_list = []
    for element in list1:
        if not (element in distinct_list):
            distinct_list.append(element)
    return distinct_list


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    :param list2:
    :param list1:
    """
    intersection_list = []
    for element in list1:
        if element in list2 and not (element in intersection_list):
            intersection_list.append(element)
    return intersection_list


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    :param list2:
    :param list1:
    """
    if not list1:
        return list2
    elif not list2:
        return list1
    else:
        if list1[0] < list2[0]:
            return [list1[0]] + merge(list1[1:], list2)
        else:
            return [list2[0]] + merge(list1, list2[1:])


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    :param list1:
    """
    if len(list1) < 2:
        return list1
    else:
        mid = len(list1) // 2
        return merge(merge_sort(list1[:mid]), merge_sort(list1[mid:]))


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    :param word:
    """

    if len(word) == 0:
        return ['']

    all_strings = []
    first = word[0]
    rest_strings = gen_all_strings(word[1:])
    all_strings.extend(rest_strings)

    for string in rest_strings:
        size = len(string) + 1
        aux = [string[:idx] + first + string[idx:] for idx in range(size)]
        all_strings.extend(aux)

    return all_strings


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    :param filename:
    """
    file_url = urllib2.urlopen(codeskulptor.file2url(filename))
    return list(file_url.readlines())


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

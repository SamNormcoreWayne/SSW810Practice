# @author: Ziyu Zhang
# HW07 for SSW 810

from collections import Counter
from collections import defaultdict
import unittest


def anagrams(str_1, str_2):
    return sorted(str_1) == sorted(str_2)


class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        '''Test for anagrams()'''
        self.assertFalse(anagrams('story', 'stand'))
        self.assertTrue(anagrams('dormitory', 'dirtyroom'))


def anagram_dd(str_1, str_2):
    dd = defaultdict(int)
    for item in str_1:
        dd[item] += 1
    for item in str_2:
        dd[item] -= 1

    return not any(dd.values())


class TestAnagramDD(unittest.TestCase):
    def test_anagram_dd(self):
        '''Test for anagrams_dd()'''
        self.assertFalse(anagram_dd('story', 'stand'))
        self.assertTrue(anagram_dd('dormitory', 'dirtyroom'))


def anagram_counters(str_1, str_2):
    return Counter(str_1) == Counter(str_2)


class TestAnagramCounters(unittest.TestCase):
    def test_anagram_counters(self):
        '''Test for anagrams_counters()'''
        self.assertFalse(anagram_counters('story', 'stand'))
        self.assertTrue(anagram_counters('dormitory', 'dirtyroom'))


def covers_alphabet(setence):
    alphabet = set()
    tmp = set()
    for i in range(97, 123):
        alphabet.add(chr(i))
    for item in setence:
        tmp.add(item.lower())
    # I did take care of other characters
    return tmp.intersection(alphabet) == alphabet


class TestCoversAlphabet(unittest.TestCase):
    def test_cover_alphabet(self):
        '''Test for covers_alphabet()'''

        self.assertTrue(covers_alphabet('The quick brown, fox; jump.s ov;er th/e lazy dog'))
        self.assertTrue(covers_alphabet('The quic@#!$%@!#k brown, fox; jump.s ov;er th/e lazy dog'))
        self.assertTrue(covers_alphabet('We promptly judged antique ivory buckles for the next prize'))
        self.assertFalse(covers_alphabet('FalseTest'))


def book_index(words):
    """
    words_dict = defaultdict(list)
    for tuples in words:
        words_dict[tuples[0]] += [tuples[1]]
        words_dict[tuples[0]] = sorted(list(set(words_dict[tuples[0]])))
        # words_dict[tuples[0]] = sorted({}.fromkeys(words_dict[tuples[0]).keys())

    key_list = list(words_dict)
    key_list.sort()
    for item in key_list:
        yield [item, words_dict[item]]
    """
    words_dict = defaultdict(set)
    for tuples in words:
        words_dict[tuples[0]].add(tuples[1])
    for word in sorted(words_dict.keys()):
        yield [word, sorted(words_dict[word])]


class TestBookIndex(unittest.TestCase):
    def test_book_index(self):
        '''Test for book_index()'''
        words = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
        self.assertEqual(list(book_index(words)), [['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]], ['much', [3]], ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]])


def main():
    print('In main()')
    str_1 = 'dormitory'
    str_2 = 'dirtyroom'
    words = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
    print(anagrams(str_1, str_2))
    print(anagram_dd(str_1, str_2))
    print(anagram_counters(str_1, str_2))
    print(covers_alphabet('The quick brown, fox; jump.s ov;er th/e lazy dog'))
    words_list = list(book_index(words))
    print(words_list)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()

import unittest


def Search(target, string):
    # actually there are many nice search algotithms
    # but firstly i will use brute-force method because it is ez.
    # and considering of the scale of inputs, there is no need to use a O(log(n)) algorithm.
    # however I will upload the advanced version after I finished all the parts.
    tmp = string.lower()
    # Alright, you want the largest index, so I will start with the last one.
    for index in range(len(string) - 1, -1, -1):
        if target == tmp[index]:
            return index
    return 'end'


class TestSearch(unittest.TestCase):
    def test_search(self):
        '''A test for search()'''
        self.assertEqual(Search('o', 'honorificabilitudinitatibus'), 3)
        self.assertEqual(Search('u', 'honorificabilitudinitatibus'), len('honorificabilitudinitatibus') - 2)
        self.assertEqual(Search('i', 'HONOrificabilitudinitatibus'), len('honorificabilitudinitatibus') - 4)


def main():
    string = 'apple'
    print('in main() \n')
    print(Search('p', string))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()

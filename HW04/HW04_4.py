# @author: Ziyu Zhang
# Actually I think it is impossible to implement
# because, you see, it is very hard to return 2 variables for a user function.
# but, generator is a nice stuff, and python is so magical, I tried generator and succeeded.
import unittest


def my_enumerate(string):
    for i in range(len(string)):
        yield i, string[i]


class TestMyEnumerator(unittest.TestCase):
    def test_my_enumerator(self):
        self.assertEqual(list(my_enumerate('honorificabilitudinitatibus')), list(enumerate('honorificabilitudinitatibus')))


def main():
    print("in main()")
    print(list(my_enumerate("hi!")))
    for a, b in my_enumerate("hi!"):
        print(a, b)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()

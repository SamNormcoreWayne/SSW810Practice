import unittest
import os
from HW08_ZiyuZhang import scanning_dir_file


class TestScanningDirFile(unittest.TestCase):
    def test_scanning_dir_file(self):
        dirt = os.getcwd()
        dirt = os.path.join(dirt, 'TestCase')
        set_file = {('file1.py', 2, 4, 25, 270), ('0_defs_in_this_file.py', 0, 0, 3, 57)}
        self.assertEquals(scanning_dir_file(dirt), set_file)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

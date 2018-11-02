import sys
import os
# from HW08.HW08_ZiyuZhang import csv_reader

print(os.getcwd())
def gen():
    lst = [1, 2, 3, 4]
    yield

print(list(gen()))
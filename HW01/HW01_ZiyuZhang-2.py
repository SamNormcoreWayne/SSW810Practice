# This is coded Python by 3.7.0
# Copyright of Ziyu Zhang Universal Company;p
# No one can copy this codes.

from random import choice
# I guess this is how inheritance works in python because I know random is a class

def get_answer():
    answer = choice(['R', 'P', 'S'])
    return answer

def main():
    outcoming = {'R': {'R': 'Tie: both Rock', 'S': 'Win: R defeats S', 'P': 'Lose: P defeats R'},
    'P': {'P': 'Tie: both Paper', 'R': 'Win: P defeats R', 'S': 'Lose: S defeats P'},
    'S': {'S': 'Tie: both Scissors', 'P': 'Win: S defeats P', 'R': 'Lose: R defeats S'}}

    while True:
        human = input("Please choose 'R', 'P', 'S' or 'Q' to quit:")
        computer = get_answer()
        if ord(human) > 96:
            human = chr(ord(human) - 32)
# In convenience, whether I input upper case or lower acae, program will execute successfully.
        if human == 'Q':
            print('Thx for playing, bye. \n')
            break
        else:
            print(outcoming[human][computer], '\n')

if __name__ == '__main__':
    main()
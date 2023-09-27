# This is a sample Python script.
import random
import string

rand_strings = []
shift_num = 0

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def gen_direct_num():
    global shift_num
    random.randint(0, 1)

def gen_shift_num():
    global shift_num
    random.randint(1, 10)


def create_strings():
    global rand_strings
    while len(rand_strings) < 50:
        new_string = ''.join(random.choices(string.ascii_letters, k=5))
        rand_strings.append(new_string)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_strings()
    gen_direct_num()
    gen_shift_num()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

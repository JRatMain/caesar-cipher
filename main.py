# This is a sample Python script.
import random
import string
import random_string as rand

rand_strings = []
enc_strings = []
shift_num = 0
direct_num = 0


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def print_strings():
    print('stub')


def encrypt():
    global direct_num, shift_num, rand_strings, enc_strings


def gen_direct_num():
    global direct_num
    direct_num = random.randint(0, 1)
    return direct_num

def gen_shift_num():
    global shift_num
    shift_num = random.randint(1, 10)
    return shift_num


def create_strings():
    global rand_strings, direct_num, shift_num
    while len(rand_strings) < 50:
        direct_num = gen_direct_num()
        shift_num = gen_shift_num()
        new_string = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        new_rand = rand(new_string, direct_num, shift_num)
        rand_strings.append(new_rand)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_strings()
    gen_direct_num()
    gen_shift_num()
    encrypt()
    print_strings()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

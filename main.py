import random
import string
import random_string as rand

rand_strings = []
enc_strings = []
shift_num = 0
direct_num = 0


def print_strings():
    print('stub')


def encrypt():
    global direct_num, shift_num, rand_strings, enc_strings
    for i in range(len(rand_strings)):

        r_string = str(rand.__getattribute__())
        shift_num = rand.__getattribute__()
        direct_num = rand_strings[i].__getitem__(direct_num)
        print(direct_num)
        print(shift_num)
        print(r_string)
        encrypted_text = ""


"""
        for char in range(len(r_string)):
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()  # Convert to lowercase for easier manipulation
                char_code = ord(char)

                if direct_num == 0:
                    encrypted_char_code = ((char_code - ord('a') + shift_num) % 26) + ord('a')
                elif direct_num == 1:
                    encrypted_char_code = ((char_code - ord('a') - shift_num) % 26) + ord('a')

                encrypted_char = chr(encrypted_char_code)

                if is_upper:
                    encrypted_char = encrypted_char.upper()  # Preserve uppercase
                encrypted_text += encrypted_char
            else:
                encrypted_text += char  # Preserve non-alphabet characters

            enc_strings.append(encrypted_text)

"""


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
        new_rand = rand.RandomString(new_string, direct_num, shift_num)
        rand_strings.append(new_rand)


if __name__ == '__main__':
    create_strings()
    encrypt()
    print_strings()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

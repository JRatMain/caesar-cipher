# Random module imported to randomize strings, shift and direction numbers.
import random
# Imports the string module to manipulate characters.
import string

# imports the random string file for generating random string objects.
import random_string as rand

# Global variables. One list stores random string objects and the other stores the encrypted strings.
# shift_num and direct_num indicate the amount of letters to shift through
# and the direction of the shift respectively.
rand_strings = []
enc_strings = []
shift_num = 0
direct_num = 0


# Prints the strings of the original list and the encrypted strings.
def print_strings():
    global direct_num, shift_num, rand_strings, enc_strings
    print('=============================================')
    for i in range(len(rand_strings)):
        print('============================================')
        print('')
        data = rand_strings[i]
        shift_dir = data.__getattribute__('shift_dir')

        if shift_dir == 0:
            shift_dir_str = 'right (0)'
        elif shift_dir == 1:
            shift_dir_str = 'left (1)'
        else:
            shift_dir_str = 'Unknown'
        print('Original string: ' + data.__getattribute__('rand_string'))
        print('Shift Number: ' + str(data.__getattribute__('shift_num')))
        print('Direction: ' + shift_dir_str)
        print('Encrypted String: ' + enc_strings[i])

    print('==========================================')


# Encrypts each string and adds it to a different list of encrypted strings.
def encrypt():
    global direct_num, shift_num, rand_strings, enc_strings
    for i in range(len(rand_strings)):
        # Data uses the object from the current index of the list to supply variables from
        # the random string class.
        data = rand_strings[i]
        r_string = data.__getattribute__('rand_string')
        shift_num = int(data.__getattribute__('shift_num'))
        direct_num = data.__getattribute__('shift_dir')
        encrypted_text = ''
        for char in r_string:

            if char.isalpha():
                is_upper = bool(char.isupper())
                char = char.lower()  # Converting to lowercase for easier manipulation
                char_code = ord(char)

                if direct_num == 0:
                    encrypted_char_code = ((char_code - ord('a') + shift_num) % 26) + ord('a')  # Encrypts the character
                    # Specifically, it shifts the value using the character's Unicode code point with the cipher
                    # formula.
                elif direct_num == 1:
                    encrypted_char_code = ((char_code - ord('a') - shift_num) % 26) + ord(
                        'a')  # Encrypts the character.
                    # It uses the Unicode code point of that character and encrypts it using the Caesar cipher formula.

                encrypted_char = chr(encrypted_char_code)

                if is_upper:
                    encrypted_char = encrypted_char.upper()  # Preserve uppercase letters.
                encrypted_text += encrypted_char

            elif char.isdigit():
                char_code = ord(char)

                if direct_num == 0:
                    encrypted_char_code = ((char_code - ord('0') + shift_num) % 10) + ord('0')  # Encrypts the character
                    # Specifically, it shifts the value using the character's ASCII code point with the cipher
                    # formula.
                elif direct_num == 1:
                    encrypted_char_code = ((char_code - ord('0') - shift_num) % 10) + ord(
                        '0')  # Encrypts the character.
                    # It uses the ASCII code point of that character and encrypts it using the Caesar cipher formula.
                encrypted_char = chr(encrypted_char_code)

                encrypted_text += encrypted_char
            else:
                encrypted_text += char  # Preserve non-alphabet characters

        enc_strings.append(encrypted_text)


# Generates the direction number and returns it.
def gen_direct_num():
    global direct_num
    direct_num = random.randint(0, 1)
    return direct_num


# Generates the shift number and returns it.
def gen_shift_num():
    global shift_num
    shift_num = random.randint(1, 10)
    return shift_num


# Creates each randomized string, creates a random_string object,
# and adds it to the random string list.
def create_strings():
    global rand_strings, direct_num, shift_num
    while len(rand_strings) < 50:
        direct_num = gen_direct_num()
        shift_num = gen_shift_num()
        new_string = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        new_rand = rand.RandomString(new_string, direct_num, shift_num)
        rand_strings.append(new_rand)


# Main function.
if __name__ == '__main__':
    create_strings()
    encrypt()
    print_strings()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

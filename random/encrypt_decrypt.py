# We want to be able to encrypt and decrypt messages.
# Original messages to be encrypted do not contain numbers.
# We encrypt by a simple protocol that is based on character mapping as shown below.
# Encryption and decryption happens by replacing vowels by numbers and viceversa
#
# example: codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
#
# Your tasks are:
#   - based on the criteria explained above, write a function that encrypt/decrypt messages.
#   - provide some tests to verify that the function works as expected.
#   - mention any assumption you make to solve the problem.
#
# examples of input/output:
# input = "t3s 3s 1 m2ss1g2."
# output = "this is a message."
#
# input = "another message here!"
# output = "1n4th2r m2ss1g2 h2r2!"

codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5, 'y': 6}


def encrypt(input_param: str) -> str:
    result = str()
    for c in input_param:
        try:
            result += str(codes[c])
        except KeyError:
            result += c
    return result


def decrypt(input_param: str) -> str:
    result = str()
    codes_swapped = {str(v): k for k, v in codes.items()}
    for c in input_param:
        try:
            result += codes_swapped[c]
        except KeyError:
            result += c
    return result


print(encrypt("another message here!"))
print(decrypt("1n4th2r m2ss1g2 h2r2!"))

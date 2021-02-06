strings = 'abcde'

# brute force
def rev(s):
    str = ""
    for i in s:
        str = i + str
    return str

print(rev(strings))

# recursion
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

print(reverse(strings))

# using list
output = []
for s in strings:
    output.insert(0, s)
output = ''.join(output)

print(output)


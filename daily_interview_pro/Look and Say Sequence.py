# A look-and-say sequence is defined as the integer sequence beginning with a single digit
# in which the next term is obtained by describing the previous term. An example is easier to understand:
# Each consecutive value describes the prior value.
#
# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.
#
# Your task is, return the nth term of this sequence.

def countAndSay(n):
    # Base cases
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"

    # Find n'th term by generating
    # all terms from 3 to n-1.
    # Every term is generated using
    # previous term

    # Initialize previous term
    s = "11"
    for i in range(3, n + 1):

        # In below for loop,
        # previous character is
        # processed in current
        # iteration. That is why
        # a dummy character is
        # added to make sure that
        # loop runs one extra iteration.
        s += '$'
        l = len(s)

        cnt = 1  # Initialize count
        # of matching chars
        tmp = ""  # Initialize i'th
        # term in series

        # Process previous term to
        # find the next term
        for j in range(1, l):

            # If current character
            # doesn't match
            if (s[j] != s[j - 1]):

                # Append count of
                # str[j-1] to temp
                tmp += str(cnt + 0)

                # Append str[j-1]
                tmp += s[j - 1]

                # Reset count
                cnt = 1

            # If matches, then increment
            # count of matching characters
            else:
                cnt += 1

        # Update str
        s = tmp
    return s


print(countAndSay(10))

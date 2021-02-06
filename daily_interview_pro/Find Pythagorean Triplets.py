# Given a list of numbers, find if there exists a pythagorean triplet in that list.
# A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2
#
# Example:

# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 5**2 + 12**2 = 13**2.

def findPythagoreanTriplets(nums):
    # Fill this in.
    nums_power = [x ** 2 for x in nums]
    result = [(a, b) for a in nums_power for b in nums_power if a != b and a + b in nums_power]
    if result:
        return True
    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True

# Given a string with the initial condition of dominoes, where:
# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side
#
# Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends,
# the force cancels out and that domino remains upright.
# Example:
# Input:  ..R...L..R.
# Output: ..RR.LL..RR
# Here is your starting point:

class Solution(object):
    def __init__(self):
        self.n = 0

    @staticmethod
    def get_opposite_domino(domino):
        if domino == "R":
            return "L"
        elif domino == "L":
            return "R"
        return

    def pushDominoes(self, dominoes):
        # Fill this in.
        if not dominoes:
            return
        dominoes_list = list(dominoes)
        while self.n <= len(dominoes_list):
            if dominoes_list[self.n] == ".":
                pass

            if dominoes_list[self.n + 1] == self.get_opposite_domino(dominoes_list[self.n - 1]):
                pass

            if dominoes_list[self.n] == "R":
                dominoes_list[self.n + 1] = "R"
                self.n += 2

            elif dominoes_list[self.n] == "L":
                dominoes_list[self.n - 1] = "L"

            self.n += 1
        return ''.join(dominoes_list)


print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR

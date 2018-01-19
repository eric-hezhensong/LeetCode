# coding: utf-8


class Solution(object):
    """
    Palindrome Number
    """

    @staticmethod
    def is_palindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    solution = Solution()

    a = 232
    print(solution.is_palindrome(a))

    a = 245
    print(solution.is_palindrome(a))

# coding: utf-8


class Solution(object):
    """
    Valid Palindrome
    """

    @staticmethod
    def is_palindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True

        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i].isalnum() is False:
                i += 1
            while j > i and s[j].isalnum() is False:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    solution = Solution()

    a = "A man, a plan, a canal: Panama"
    print(solution.is_palindrome(a))

    a = "abcad"
    print(solution.is_palindrome(a))

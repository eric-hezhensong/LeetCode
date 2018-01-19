# coding: utf-8


class Solution(object):
    """
    Valid Palindrome II
    """

    @staticmethod
    def valid_palindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        string = '#%s#' % s
        length = len(string)
        i = 0
        j = length - 1

        while i < j:
            if string[i] == string[j]:
                i += 1
                j -= 1
                continue
            else:
                left = Solution.palindrome(string[i + 1:j + 1])
                right = Solution.palindrome(string[i:j])

                if left or right:
                    return True
                else:
                    return False
        return True

    @staticmethod
    def palindrome(s):
        length = len(s)
        i, j = 0, length - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    solution = Solution()

    a = "aba"
    print(solution.valid_palindrome(a))

    a = "abcad"
    print(solution.valid_palindrome(a))

    a = "ebcbbececabbacecbbcbe"
    print(solution.valid_palindrome(a))

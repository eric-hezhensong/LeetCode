# coding: utf-8


class Solution(object):
    """
    Longest Palindromic Substring
    Manacher算法：O(n)
    """

    @staticmethod
    def longest_palindrome(s):
        # 判空
        length = len(s)
        if s is None or length == 0:
            return ''

        # 补成奇数长度
        string = '#%s#' % '#'.join(s)
        length = len(string)

        max_radius = 0  # 最大回文半径
        max_center = 0  # 最大回文中心
        max_temp = [0, 0]  # [temp_max_center, temp_max_radius]
        radius = [0] * length  # 每个点回文半径

        for i in range(length):
            if max_radius > i:
                radius[i] = min(radius[2 * max_center - i], max_radius - i)

            else:
                radius[i] = 1

            while i - radius[i] >= 0 and \
                    i + radius[i] < length and \
                    string[i - radius[i]] == string[i + radius[i]]:
                radius[i] += 1

            if max_radius < radius[i] + i:
                max_radius = radius[i] + i
                max_center = i
                if max_radius - max_center > max_temp[1] - max_temp[0]:
                    max_temp = [max_center, max_radius]

            i += 1

        begin = 2 * max_temp[0] - max_temp[1] + 1
        end = max_temp[1]
        return string[begin:end].replace('#', '')


if __name__ == '__main__':
    solution = Solution()

    a = "babad"
    print(solution.longest_palindrome(a))

    a = "aaa"
    print(solution.longest_palindrome(a))

    a = "cbbd"
    print(solution.longest_palindrome(a))

    a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(len(a))
    print(solution.longest_palindrome(a))

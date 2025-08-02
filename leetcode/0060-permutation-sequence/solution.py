class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial

        numbers = list(range(1, n + 1))
        k -= 1  # 0-based indexing
        result = ""

        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            result += str(numbers[index])
            numbers.pop(index)
            k %= fact

        return result


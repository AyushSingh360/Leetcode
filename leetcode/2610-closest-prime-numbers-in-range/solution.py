class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # Sieve of Eratosthenes to find all primes up to right
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(right**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        # Collect all primes in the range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime[i]]

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        ans = [-1, -1]

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i - 1], primes[i]]
                if diff == 1:  # Can't get better than this
                    break

        return ans


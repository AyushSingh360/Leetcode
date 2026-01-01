class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Traverse from the last digit backwards
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # if digit is 9, it becomes 0 and carry continues
            digits[i] = 0
        
        # If all digits were 9, we need an extra leading 1
        return [1] + digits


class Solution(object):
    def numberOfSubstrings(self, s):
        last_seen = {"a": -1, "b": -1, "c": -1}
        result = 0

        for i, char in enumerate(s):
            last_seen[char] = i
            if -1 not in last_seen.values():
                # The smallest index of the three
                min_index = min(last_seen.values())
                result += min_index + 1
        return result

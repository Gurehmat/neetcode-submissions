class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = {}                 # number -> how many times we've seen it

        for n in nums:
            if n in seen:         # already saw this number before?
                return True       # that's a duplicate, done
            seen[n] = 1           # first time seeing it, record it

        return False              # got through everything, no repeats
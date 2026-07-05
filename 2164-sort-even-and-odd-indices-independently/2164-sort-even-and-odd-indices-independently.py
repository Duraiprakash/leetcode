class Solution:
    def sortEvenOdd(self, nums):
        even = sorted(nums[::2])                 # Even indices ascending
        odd = sorted(nums[1::2], reverse=True)  # Odd indices descending

        nums[::2] = even
        nums[1::2] = odd

        return nums
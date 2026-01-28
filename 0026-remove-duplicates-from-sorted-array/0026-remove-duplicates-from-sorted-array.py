class Solution:
    def removeDuplicates(self, nums):
        # if array is empty
        if len(nums) == 0:
            return 0

        slow = 0  # points to last unique number

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1

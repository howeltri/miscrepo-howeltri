class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        popped = 0
        for i in nums:
            search = target - i
            del nums[0]
            popped+=1
            if search in nums:
                return [popped -1, nums.index(search)+popped]
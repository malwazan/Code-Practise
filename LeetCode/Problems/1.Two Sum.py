#Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i,n in enumerate(nums):
            temp = target - n
            if temp in result:
                return[result[temp],i]
            else:
                result[n]=i

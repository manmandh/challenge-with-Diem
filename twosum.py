class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i] + nums[j]== target):
        #            return [i, j]
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 18
    result = s.twoSum(nums, target)
    print("Result:", result)

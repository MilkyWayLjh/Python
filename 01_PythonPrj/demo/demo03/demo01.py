# nums = input('输入num，用空格隔开:').split()
# nums.sort()
# for i in nums:
#     print(i, end=' ')
"""
nums = input('输入一串数字:')
li = []
for i in nums:
    li.append(i)
li.sort()
print(''.join(li))
"""


# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# Round 1：先取元素 2，根据 9-2=7，下一步寻找7是否在剩下的元素中，若在则返回下标，此时答案为 `[0, 1]`
# Round 2：先取元素 7，根据 9-7=2，下一步寻找2是否在剩下的元素中，若在则返回下标，此时答案为 `[1, 0]`
# ······
# Round 4：先取元素 11，9-11=-2，-2 不在数组 `nums` 中，故排除此种情况
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i+1:]:
                return [i, nums[i+1:].index(res)+i+1]

s = Solution()
print(s.twoSum([2, 3, 5, 7], 8))


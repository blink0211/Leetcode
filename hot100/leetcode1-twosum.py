# 不能重复使用同样的元素两次
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtbl = {}
        for i,num in enumerate(nums):
            if target - num in hashtbl:
                return [hashtbl[target-num] , i]
            hashtbl[num] = i #如果这个写在前面，就可以使用同样的元素两次
        return []
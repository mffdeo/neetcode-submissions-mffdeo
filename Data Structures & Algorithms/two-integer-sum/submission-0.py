class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      lista = []
      for i, n in enumerate(nums):
        for j, m in enumerate(nums):
          if((nums[i] + nums[j])==target and i!=j):
            lista.append(i)
      return lista       
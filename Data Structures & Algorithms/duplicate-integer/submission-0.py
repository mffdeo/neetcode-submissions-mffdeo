class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)#converte a lista para um conjunto
        return len(nums) != len(nums_set)#compara o tamanho da lista com o tamanho do conjunto
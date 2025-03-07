'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

#brutal force - passa por todo o array, e compara os valores até achar o target. 
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []


# One-pass Hash table - usa um dicionario que guarda o indice do array e o valor na chave, durante a a iteração do array
# calcula o numero complementar de cada numero do indice.
# verifica se o numero complementar existe no dicionario. se sim, retorna o indice. Se não o numero apena é adiconado no dicionario

class Solution2(object):
    def twoSumHash(self, nums, target):
        numMap = { }
        for i, num in enumerate(nums):
            complementNumber = target - num
            if complementNumber in numMap:
                return [numMap[complementNumber], i]
            numMap[num] = i
        return []
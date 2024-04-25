class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #creating the Hashmap to store Key:Value data as: Index:Value
        hashMap = {}


        #Iterate through the HashMap, checking if difference between target and current value
        #exist in a hashmap, otherwise add this value and index to the hashmap
        for index, value in enumerate (nums):
            difference = target - value
            if difference in hashMap:
                return [hashMap[difference], index]
            else:






                hashMap[value] = index
        return
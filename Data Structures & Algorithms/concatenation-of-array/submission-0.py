class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] #initialized empty array
        for i in range(2): #master loop is executed exactly twice
            for n in nums: #iterates sequentially through every element in the nums array
                ans.append(n) #appends current element n to the end of the ans rray
        return ans
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr) -1 ): #go through every position except the last (-1)
 
           arr[i] = max(arr[i + 1:]) #arr[i + 1:] is a slice, everything to the right of position i, max() is the biggest number of that group. which is assigned to the i position in the array

        arr[- 1] = - 1 #update last value to -1
        return arr
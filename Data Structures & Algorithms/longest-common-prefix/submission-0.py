class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #check if list is empty
        if not strs:
            return ""
        
        strs.sort() #sort alphabetically

        #get first and last words
        first_word = strs[0]
        last_word = strs[-1]

        #empty string for answer
        common_prefix = ""

        #compare letters 1-by-1
        for i in range(min(len(first_word), len(last_word))):
            if first_word[i] == last_word[i]:
                common_prefix += first_word[i] #adds matching letter
            else:
                break
            
        return common_prefix
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sorted_strs = []
        dict_strs = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dict_strs:
                dict_strs[sorted_word] = [word]
            else:
                dict_strs[sorted_word].append(word)
        
        #res_lst = []
        return list(dict_strs.values())
        
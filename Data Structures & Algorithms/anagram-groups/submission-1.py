class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = dict()
        for s in strs:
            sorted_s = "".join(sorted(s)) 
            if sorted_s not in dict_:
                dict_[sorted_s] = [s]
            else:
                dict_[sorted_s].append(s)
        return list(dict_.values())
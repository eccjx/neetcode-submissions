class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
        #print(sorted(num_dict.items(), key = lambda x:x[1], reverse = True))
        sorted_lst = sorted(num_dict.items(), key = lambda x:x[1], reverse = True)[:k]
        res = [x[0] for x in sorted_lst]
        return res
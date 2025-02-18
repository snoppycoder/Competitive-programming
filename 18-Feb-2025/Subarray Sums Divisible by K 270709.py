# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, arr: List[int], k: int) -> int:
        ps = [0] *(len(arr)+1)
        ds = defaultdict(int)
        ds[0] = 1 
        res = 0
        for i in range(1, len(ps)):
            ps[i] = arr[i-1] + ps[i-1]
    
        for i in range(1, len(ps)):
            if ps[i] % k in ds:
                res += ds[ps[i]%k]
            ds[ps[i] % k] +=1
        return res

        

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        presum=0
        cnt=0
        hm={}
        hm[0]=1

        for n in nums:
            presum+=n

            rem=presum%k
            if rem in hm:
                cnt+=hm[rem]
            if rem in hm:
                hm[rem]+=1
            else:
                hm[rem]=1
        return cnt
        
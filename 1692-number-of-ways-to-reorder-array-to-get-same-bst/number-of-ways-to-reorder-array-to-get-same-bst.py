class Solution:
    def numOfWays(self, l: List[int]) -> int:
        mod=int(1e9+7)
        n=len(l)
        com=[[1]*(i+1) for i in range(len(l)+1)]
        for i in range(2,n+1):
            for j in range(1,i):
                com[i][j]=(com[i-1][j-1]+com[i-1][j])%mod
        def solve(nums):
            m=len(nums)

            if m<3:
                return 1
            root=nums[0]
            left = [num for num in nums[1:] if num<root]
            right=[num for num in nums[1:] if num>=root]
            leftans=solve(left)%mod
            rightans=solve(right)%mod

            return ((leftans*rightans)%mod)*com[m-1][len(left)]%mod
        return (solve(l)-1)%mod

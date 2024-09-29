import bisect
class Solution:
    def jobScheduling(self, st: List[int], et: List[int], profit: List[int]) -> int:

        emp=sorted(zip(st,et,profit))
        st.sort()
        dp={}
        def h(ind):

            if ind>=len(profit):return 0
            if ind in dp:return dp[ind]

            nottake=h(ind+1)
            c_start,c_end,c_profit=emp[ind]
            nextt=bisect.bisect_left(st,c_end)
            take=c_profit+h(nextt)
            dp[ind]=max(take,nottake)
            return dp[ind]
        return h(0)



        
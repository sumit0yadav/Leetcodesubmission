class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        if(bills[0]!=5):return  False
        if len(bills)==1:return True
        dp={}
        dp[5]=1
        dp[10]=0
        dp[20]=0
        for i in range(1,len(bills)):
            if bills[i]==5:
                dp[5]+=1
            else:
                if bills[i]==10:
                    if dp[5]>=1:
                        dp[5]-=1
                        dp[10]+=1
                    else:
                        return False
                if bills[i]==20:
                    if (dp[10]>=1 and dp[5]>=1):
                        dp[10]-=1
                        dp[5]-=1
                        dp[20]+=1
                    elif dp[5]>=3:
                        dp[5]-=3
                        dp[20]+=1
                    
                    else:
                        return False


                    

                
        return True

        
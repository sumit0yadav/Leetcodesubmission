class Solution:
    def minSideJumps(self, obs: List[int]) -> int:
        
        road=[]
        for i in range(len(obs)):
            
            stop=[0,0,0]
            if obs[i]!=0:
                stop[obs[i]-1]=1
            road.append(stop)
            

        # print(road)
        dp={}
        def h(ind,pos):
            
            if road[ind][pos]==1:
                return 1e9
            if ind==len(road)-1:
                return 0
            if (ind,pos) in dp:
                return dp[(ind,pos)]
            mini=1e9
            for i in range(3):
                
                if i!=pos:
                    if road[ind][i]==0:
                        mini=min(mini,1+h(ind+1,i))
                    

                else:
                    mini=min(mini,h(ind+1,i))                    
                
            dp[(ind,pos)]= mini
            return mini

        # print(1+h(1,0),h(1,1),1+h(1,2))
        return min(1+h(1,0),h(1,1),1+h(1,2))

        
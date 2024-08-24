class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], k: int) -> List[int]:

        potions.sort()
        l=[]
        
        for i in range(len(spells)):
            sp=spells[i]
            if potions[-1]*sp<k:
                l.append(0)
            else:
                # potions.sort()
            
            
                left,right=0,len(potions)-1
                # sp=spells[i]
                while left<=right:
                    mid= left+(right-left)//2
                    pro=sp*potions[mid]
                    if pro<k:
                        left=mid+1
                    else:
                        right=mid-1
                res=len(potions)-left
                l.append(res)
        return l


        
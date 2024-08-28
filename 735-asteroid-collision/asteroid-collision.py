class Solution:
    def asteroidCollision(self, l: List[int]) -> List[int]:
        st=[]
        i=0
        while i<len(l):

            if not st:
                st.append(l[i])
                
            else:
                    # i+=1
                if st[-1]*l[i]>0:
                    st.append(l[i])
                elif st[-1]*l[i]<0:
                    # print('lkk',l[i],st)
                    while st and st[-1]>0 and st[-1]<=abs(l[i]):
                        if st[-1]==-l[i]:
                            st.pop()
                            break
                        else:
                            st.pop()
                    
                    else:
                        if not st or st[-1]<0:
                            st.append(l[i])
                # else:
                #     st.append(l[i])
            i+=1
        # print(st,'llll')
        return st
# from collections import defaultdict
# class Solution:
#     def minJumps(self, arr: List[int]) -> int:
#         if len(arr)==1:
#             return 0
        
#         hm=defaultdict(list)
#         for i in range(len(arr)):
#             hm[arr[i]].append(i)
#         q=deque()
#         vis=set()
#         q.append(0)

#         step=0
#         while q:
            
#             size=len(q)
#             step+=1


#             for i in range(size):
#                 curr=q.popleft()
#                 vis.add(curr)
#                 if curr==len(arr)-1:
#                     return step-1
#                 if -1<curr-1 and curr-1 not in vis:
#                     q.append(curr-1)
#                 if curr+1<len(arr) and curr+1 not in vis:
#                     q.append(curr+1)
#                 for ele in hm[arr[curr]]:
#                     if 0<=ele<len(arr) and ele not in vis and ele!=curr:
#                         q.append(ele)
#         return step



from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        # Create a hashmap where the keys are values from the array
        # and the values are lists of indices with those values.
        hm = defaultdict(list)
        for i in range(len(arr)):
            hm[arr[i]].append(i)

        # BFS initialization
        q = deque([0])  # Start from index 0
        vis = set([0])  # Mark index 0 as visited
        step = 0

        # BFS loop
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                
                # If we reach the last index, return the number of steps.
                if curr == len(arr) - 1:
                    return step

                # Explore neighbors: curr-1 and curr+1
                if curr - 1 >= 0 and curr - 1 not in vis:
                    vis.add(curr - 1)
                    q.append(curr - 1)
                
                if curr + 1 < len(arr) and curr + 1 not in vis:
                    vis.add(curr + 1)
                    q.append(curr + 1)

                # Explore all other indices with the same value as arr[curr]
                for ele in hm[arr[curr]]:
                    if ele not in vis:
                        vis.add(ele)
                        q.append(ele)
                
                # Clear the list for arr[curr] to prevent revisiting
                hm[arr[curr]].clear()

            # Increment step after processing all nodes at the current level
            step += 1

        # If we exit the while loop without having found the last index
        return step




        
class Solution:
    def medianSlidingWindow(self, l: List[int], k: int) -> List[float]:
        import bisect
        # l=[1,3,-1,-3,5,3,6,7]
        # k=3
        arr=l[:k]
        arr.sort()
        if k%2==0:
            res=arr[k//2-1]+arr[k//2]
            ans=[res/2]
        else:
            ans=[arr[k//2]]
        for i in range(k,len(l)):
            arr.remove(l[i-k])
            bisect.insort(arr,l[i])
            # print(arr[k//2])
            if k%2==0:
                res=arr[k//2-1]+arr[k//2]
                ans.append(res/2)
            else:
                ans.append(arr[k//2])



        return ans
        


        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        import bisect
        def h(matrix,target):
            l=[x[-1] for x in matrix]
            # print(l)
            ind=bisect.bisect_left(l,target)
            # print(ind)
            if ind>=len(matrix):
                return(False)

            find=matrix[ind]
            if target<find[0]:
                return(False)
            elif target>find[-1]:
                return(False)
            else:
                ind2=bisect.bisect_left(find,target)
                if find[ind2]==target:
                    return True
                return False
        return (h(matrix,target))
        
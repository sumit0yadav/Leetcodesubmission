import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        hp=[]
        currtime=0
        for ele in courses:
            duration,deadline=ele[0],ele[1]
            heapq.heappush(hp,-duration)

            currtime+=duration

            if currtime>deadline:
                x=heapq.heappop(hp)
                currtime+=x
        return len(hp)

        
        
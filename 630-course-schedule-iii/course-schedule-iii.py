import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Sort the courses by their deadline (second element of each sublist)
        courses.sort(key=lambda x: x[1])

        # A max-heap to keep track of the courses we've taken (use negative durations)
        max_heap = []
        current_time = 0

        for course in courses:
            duration, last_day = course

            # Add the current course to the heap
            heapq.heappush(max_heap, -duration)
            current_time += duration

            # If the current time exceeds the last day of the current course,
            # remove the longest duration course from the heap
            if current_time > last_day:
                longest_duration = -heapq.heappop(max_heap)
                current_time -= longest_duration

        # The size of the heap represents the maximum number of courses we can take
        return len(max_heap)

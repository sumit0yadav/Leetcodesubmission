from sortedcontainers import SortedList
class Solution:
    def getNextServer(self, index , sortedAvailableServers):
        nextIndexToRightOfServer = sortedAvailableServers.bisect_left(index)
        # Since We need to find next server availble greater than this index
        if nextIndexToRightOfServer != len(sortedAvailableServers):
            return sortedAvailableServers[nextIndexToRightOfServer]
        # No server greater than index found , means move in cycle and find the lowest avaiable server now
        lowestIdServerAvailable = sortedAvailableServers.bisect_left(0)
        return sortedAvailableServers[lowestIdServerAvailable]
                
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        heap = [] 
        # This heap will be use to make servers as free , the first server to become free will be top element of heap
        
        sortedAvailableServers = SortedList([i for i in range(k)])      
        # This sorted available server list will be used to assign the load to new server , more comment in function 
        
        count = collections.defaultdict(int)
        # This count dictionary will be used to record the count of request each server has handled, will be used in calculating result
        
        for i in range(len(arrival)):
            arrivalTime,loadTime = arrival[i], load[i]
            # ArrivalTime and loadTime , SimpleStuff
            
            # Check if any server has become free now, since top of heap will contain the first server which will get free
            # we just compare top server free time with currentTime and mark the server as free if possible
            while len(heap) > 0 and heap[0][0] <= arrivalTime:
                _,serverId = heapq.heappop(heap)
                # after marker this server free add it to list of free Servers
                sortedAvailableServers.add(serverId)

            #Check for any server Available
            if len(sortedAvailableServers) == 0:
                # Drop this Request because no server available
                continue
            
            # Get the assigned serverId for this Request
            assignedServer = self.getNextServer(i%k,sortedAvailableServers)
            
            count[assignedServer] += 1 # increase requestcount of this server by 1
            sortedAvailableServers.remove(assignedServer) # remove this server from list of free server
            heapq.heappush(heap,(arrivalTime+loadTime,assignedServer)) # insert this server in heap with free time as arrivalTime+loadTime
        
        # get the max request servered by any server
        maxRequestServedCount = max(count.values())
        result = []
        
        #iterate and pick all servers which servered maxRequest
        for serverId in count:
            if count[serverId] == maxRequestServedCount:
                result.append(serverId)

        return result
        
                
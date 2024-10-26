import java.util.*;

class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        // Sort the trips based on the drop-off point
        Arrays.sort(trips, Comparator.comparingInt(a -> a[2]));

        // Find the minimum start point and maximum end point
        int start = Integer.MAX_VALUE;
        int end = Integer.MIN_VALUE;

        for (int[] trip : trips) {
            start = Math.min(start, trip[1]);
            end = Math.max(end, trip[2]);
        }

        // Create a list to track the number of passengers at each point
        int[] passengerCount = new int[end + 1];

        // Update the passenger counts for each trip
        for (int[] trip : trips) {
            int val = trip[0]; // Number of passengers
            int x = trip[1];   // Start location
            int y = trip[2];   // End location
            passengerCount[x] += val; // Add passengers at start location
            if (y < end + 1) {
                passengerCount[y] -= val; // Remove passengers at end location
            }
        }

        // Calculate the prefix sum and check against capacity
        int presum = 0;
        int maxsum = 0;

        for (int count : passengerCount) {
            presum += count;
            maxsum = Math.max(presum, maxsum);
        }

        // Return true if the max number of passengers never exceeds capacity
        return maxsum <= capacity;
    }
}

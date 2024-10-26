import java.util.*;
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        Arrays.sort(trips,Comparator.comparingInt(a -> a[2]));
        int start=Integer.MAX_VALUE;
        int end=Integer.MIN_VALUE;

        for(int[] t: trips){
            start=Math.min(start,t[1]);
            end=Math.max(end,t[2]);


        }
        int[] pass = new int[end+1];

        for(int[] trip:trips){
            int val=trip[0];
            int x=trip[1];
            int y=trip[2];
            pass[x]=pass[x]+val;
            if (y<end+1){
                pass[y]=pass[y]-val;
            }

        }
        int pre=0;
        int maxi=0;
        for(int i=0;i<pass.length;i++){
            pre+=pass[i];
            maxi=Math.max(maxi,pre);
            
        }
        if (maxi<=capacity){
            return true;
        }
        return false;



        
    }
}
import java.util.*;
class Solution {
    public int minDistance(String word1, String word2) {
        HashMap<String,Integer> hm = new HashMap<>();
        return h(word1,word2,word1.length()-1,word2.length()-1,hm);
        
    }


        private int h(String w1,String w2, int i,int j,HashMap<String,Integer> hm){

            if(i<0 && j<0){
                return 0;
            }
            if(i<0){
                return j+1;
            }
            if(j<0){
                return i+1;
            
            }
            String key = i+","+j;
            int ans=0;
            if(hm.containsKey(key)){
                return hm.get(key);
            }
            if (w1.charAt(i)==w2.charAt(j)){
                ans= h(w1,w2,i-1,j-1,hm);
            }
            else{

            int insert=1+h(w1,w2,i,j-1,hm);
            int delete=1+h(w1,w2,i-1,j,hm);
            int replace=1+h(w1,w2,i-1,j-1,hm);
            ans =Math.min(insert,Math.min(delete,replace));


            }
            
            hm.put(key,ans);
            return ans;
        



        }
        
}
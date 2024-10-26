import java.util.HashMap;

class Solution {
    public int minDistance(String word1, String word2) {
        HashMap<String, Integer> hm = new HashMap<>();
        return h(word1, word2, word1.length() - 1, word2.length() - 1, hm);
    }

    private int h(String w1, String w2, int i, int j, HashMap<String, Integer> hm) {
        // Base cases
        if (i < 0 && j < 0) {
            return 0;
        }
        if (i < 0) {
            return j + 1;
        }
        if (j < 0) {
            return i + 1;
        }

        // Create a unique key for the current indices (i, j)
        String key = i + "," + j;

        // Check if the result is already computed and stored in the HashMap
        if (hm.containsKey(key)) {
            return hm.get(key);
        }

        // If characters are equal, move to the next characters in both strings
        if (w1.charAt(i) == w2.charAt(j)) {
            return h(w1, w2, i - 1, j - 1, hm);
        }

        // Calculate insert, delete, and replace costs
        int insert = 1 + h(w1, w2, i, j - 1, hm);
        int delete = 1 + h(w1, w2, i - 1, j, hm);
        int replace = 1 + h(w1, w2, i - 1, j - 1, hm);

        // Find the minimum of the three operations
        int ans = Math.min(insert, Math.min(delete, replace));

        // Store the result in the HashMap
        hm.put(key, ans);

        return ans;
    }
}

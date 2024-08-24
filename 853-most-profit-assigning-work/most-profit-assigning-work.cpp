#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        vector<pair<int, int>> jobs;
        int n = difficulty.size();
        
        // Creating a list of pairs with difficulty and corresponding profit
        for (int i = 0; i < n; i++) {
            jobs.push_back({difficulty[i], profit[i]});
        }
        
        // Sort jobs by profit (ascending)
        sort(jobs.begin(), jobs.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;
        });
        
        int totalProfit = 0;
        
        // Assigning the best possible jobs to workers
        for (int i = 0; i < worker.size(); i++) {
            int j = n - 1;
            
            // Find the best job that the worker can handle
            while (j >= 0 && worker[i] < jobs[j].first) {
                j--;
            }
            
            // If a suitable job is found, add its profit to the total profit
            if (j != -1) {
                totalProfit += jobs[j].second;
            }
        }
        
        return totalProfit;
    }
};

// Using recursion
class Solution {
public:
    int lcs(string text1, string text2, int index1, int index2, vector<vector<int>>& dp){
        
        if(index1 == 0 || index2 == 0){
            
            dp[index1][index2] = 0;
            return dp[index1][index2];
        }
        if(text1[index1-1] == text2[index2-1]){
            if(dp[index1][index2] == -1){
                int res = 1+ lcs(text1, text2, index1 -1, index2 -1, dp);
                dp[index1][index2] = res;
            }
            return dp[index1][index2];
        }

        if(dp[index1-1][index2] == -1){
            dp[index1 -1][index2] = lcs(text1, text2, index1 -1, index2, dp);
        }
        
        if(dp[index1][index2 -1] == -1){
            dp[index1][index2 -1] = lcs(text1, text2, index1, index2 -1, dp);
        }
        return max(dp[index1 -1][index2], dp[index1][index2-1]);
    }
    int longestCommonSubsequence(string text1, string text2) {
        int length1 = text1.size();
        int length2 = text2.size();
        vector<vector<int>> dp(length1 +1, vector<int> (length2+1, -1));
        dp[length1][length2] = lcs(text1, text2, length1, length2, dp);
        return dp[length1][length2];
    }
};
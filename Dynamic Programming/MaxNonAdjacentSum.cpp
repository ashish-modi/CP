#include <bits/stdc++.h>
#include<vector>
using namespace std;

int fun(int n, vector<int> &nums, vector<int> &dp)
{
//    cout << endl << "Entering fun " << n << endl;
    if(n == 0 || n == 1) 
    { 
        dp[n] = nums[n];
        return dp[n];
    }

    if(dp[n] == -1)
    {
        int a = 0;
        int b = 0;
        if (n - 2 >= 0) 
        {
            if (dp[n - 2] == -1)
                a = fun(n - 2, nums, dp);
            else
                a = dp[n-2];
        }
        if (n - 3 >= 0) 
        {
            if (dp[n - 3] == -1)
                b = fun(n - 3, nums, dp);
            else
                b = dp[n-3];
        }
      //  cout << " A : "  << a << " B : " << b << endl;
        dp[n] = max(a,b) + nums[n];
    //    cout << endl << " After completion of N : " << n << " DP is : " << endl;
//        for(auto it : dp)
  //          cout << it << "  " ;
    }
    return dp[n]; 
}


int main()
{
    int T;
    cin >> T;
    for(int z = 0 ; z < T; z++)
    {
        int N;
        cin >> N;

        vector<int> nums(N);
        for(int i = 0; i < N; i++)
            cin >> nums[i];
        vector<int> dp(N,-1);
        N-=1;
        fun(N,nums,dp);
        fun(N-1,nums,dp);
    
        cout<< endl;
        for(auto it: dp)
            cout <<  it << "  ";
    }
    return 0;
}
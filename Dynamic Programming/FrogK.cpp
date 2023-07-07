#include<iostream>
#include<vector>
#include<bits/stdc++.h>

using namespace std;

int func(int N, int K, vector<int> &height, vector<int> &dp)
{
    if(N == 1)
    {
        dp[N] = 0;
        return dp[N];
    }

    int a, absolute_value ;

    if(dp[N] == 1e9)
    {
        for(int i= 1 ; i <= K ; i++ )
        {
            if(N - i >= 1)
            {
        
                if(height[N] > height[N - i])
                    absolute_value = height[N] - height[N - i];
                else
                    absolute_value = height[N - i] - height[N];

                a = func(N - i, K, height, dp) + absolute_value; 

                if( a < dp[N])
                    dp[N] = a;
            }
            else
                break;
        }
    }
    return dp[N];
}

int main()
{
    int N,K;
    cin >> N >> K;
    vector<int> height(N+1), dp(N + 1, 1e9);
    dp[0] = 0;

    for(int i = 1 ; i <= N; i++) cin >> height[i];

    cout << func(N, K, height,dp);
    
    return 0;
}
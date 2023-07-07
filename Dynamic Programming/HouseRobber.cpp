#include<iostream>
#include<vector>

using namespace std;

int fun(int N, vector<int> &arr, vector<int> &dp, int &flag)
{
    if(dp[N] == 0)
    {
        if( N == 0)
        {   
            if(!flag)
            {
                dp[N] = arr[N];
                return dp[N];
            }
            return 0;
        }
        if( N == 1)
        {
            dp[N] = arr[N];
            return dp[N];
        }
        

        int a = 0;
        int b = 0;

        if(N - 2 >= 0)
        {   if(dp[N-2] == 0)
                a = fun(N - 2, arr, dp, flag);
            else
                a = dp[N-2];
        }
        if(N-3 >=0)
        {
            if(dp[N-3] == 0)
                b = fun(N - 3, arr, dp, flag);
            else
                b = dp[N-3];
        }
        dp[N] = max(a,b) + arr[N];
    }
    return dp[N];
}

int main()
{
    int T; 
    cin >> T;
    for(int z = 0 ; z < T; z++)
    {
        int N,a1,a2;
        cin >> N;

        vector<int> arr(N), dp(N,0);

        for(int i = 0; i< N ; i++)
            cin >> arr[i];
        
        N-=1;
        int flag = 1;
        a1 = fun(N, arr, dp, flag);
        flag = 0;
        a2 = fun(N-1, arr, dp, flag);
        return max(a1,a2);
    }
    return 0;
}
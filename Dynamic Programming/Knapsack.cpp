#include<iostream>
#include<vector>

using namespace std;

int fun(int index, vector<int> &weights, vector<int> &values, int req_W, vector<vector<int>> &dp)
{
    if(dp[index][req_W] == -1) 
    {   
        if(index == 0 || req_W == 0)
        {
            dp[index][req_W] = 0;
            return dp[index][req_W];
        }
        else
        {
            int a = 0, b = 0;
            if(req_W >= weights[index - 1])
                a = fun(index - 1, weights, values, req_W - weights[index - 1],dp) + values[index - 1];
            b = fun(index - 1, weights, values, req_W, dp);

            dp[index][req_W] = max(a,b);
        }
    }
    return dp[index][req_W];
}


int main()
{
    int T;
    cin >> T;

    for(int z= 0 ; z < T; z++)
    {
        int N, max_W;
        cin >> N;

        vector<int> weights(N), values(N);
        vector<vector<int>> dp(N+1, vector<int>(max_W+1,-1));

        for(int i = 0 ; i < N ; i++)
            cin >> weights[i];
        for(int i = 0 ; i < N ; i++)
            cin >> values[i];
        cin >> max_W;

        cout << fun(N, weights, values, max_W, dp);
    }
}
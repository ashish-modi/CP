#include<bits/stdc++.h>
#include<iostream>
#include<vector>

using namespace std;

int fun(int index, int target, vector<int> &nums)
{ 
    if(target == 0)
        return 0;
    else if(index == 0)
    {
        if(target % nums[index] != 0 )
            return 1e9;
        else
            return target / nums[index];
    }
    else
    {
        int a = INT_MAX, b = INT_MAX ;
        if(target >= nums[index])
            b = fun(index, target - nums[index], nums) + 1;
        a = fun(index - 1, target, nums);

        return min(a,b);
    }
}


int main()
{
    int T;
    cin >> T;
    for( int z= 0 ; z < T ; z++)
    {
        int N, target;
        cin >> N >> target;

        vector<int> nums(N);

        for( int i = 0 ; i < N; i++)
            cin>> nums[i];
        
        cout << fun(N-1, target, nums);
    }
    return 0;
}
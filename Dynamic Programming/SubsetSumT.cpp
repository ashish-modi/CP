#include<iostream>
#include<vector>

using namespace std;

bool fun(int index, int target, vector<int> &arr)
{
    if(index == 0)
    {
        if(arr[index] == target)
        return 1;
        else 
        return 0;
    }
    else
    {
        bool a = false, b = false;

        if(target > arr[index])
            a = fun(index - 1, target - arr[index], arr);
        b = fun(index - 1, target, arr);
        return a || b;
    }
}


int main()
{
    int T;
    cin >> T;
    for(int z = 0 ; z < T; z++)
    {
        int N, sum = 0;
        bool ans;
        cin >> N;

        vector<int> arr(N);

        for(int i = 0 ; i < N; i++)
        {
            cin >> arr[i];
            sum += arr[i];
        }        
        ans = fun(N-1,sum / 2, arr);
        cout << ans;
    }
    return 0;
}
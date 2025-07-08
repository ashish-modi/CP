#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> vec = {
        {1, 2, 4},
        {3, 4, 3},
        {2, 3, 1}
    };

    bool compareFirstCol(const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    }
    // Sort by the first column (index 0)
    // 1st arg : beginning of the vector to be sorted
    // 2nd arg : end of the vector to be sorted
    // 3rd arg : lambda function (can also write compareFirstCol)
    
    sort(vec.begin(), vec.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });

    for (const auto& row : vec) {
        for (int val : row)
            cout << val << " ";
        cout << endl;
    }
}

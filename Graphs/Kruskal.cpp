class Solution {
  public:
    // Function to find sum of weights of edges of the Minimum Spanning Tree.
//     struct CompareByWeight {
//     bool operator()(const pair<int, int>& a, const pair<int, int>& b) {
//         return a.second > b.second; // min-heap by .second (weight)
//     }
// };


struct Edge {
    int n1, n2, wt;
};

struct myComparator {
    bool operator()(const Edge &a, const Edge &b) {
        return a.wt > b.wt; // min-heap by weight
    }
};

// Disjoint Set Union (Union-Find)
vector<int> parent, rankR;

int find(int u) {
    if (parent[u] != u)
        parent[u] = find(parent[u]);
    return parent[u];
}

void unite(int u, int v) {
    int pu = find(u);
    int pv = find(v);
    if (pu != pv) {
        if (rankR[pu] < rankR[pv])
            parent[pu] = pv;
        else if (rankR[pu] > rankR[pv])
            parent[pv] = pu;
        else {
            parent[pv] = pu;
            rankR[pu]++;
        }
    }
}

int spanningTree(int V, vector<vector<int>> adj[]) {
    parent.resize(V);
    rankR.resize(V, 0);
    for (int i = 0; i < V; ++i) parent[i] = i;

    priority_queue<Edge, vector<Edge>, myComparator> pq;

    for (int i = 0; i < V; i++) {
        for (auto &pair : adj[i]) {
            int n1 = i;
            int n2 = pair[0];
            int wt = pair[1];
            pq.push({n1, n2, wt});
        }
    }

    int cost = 0;
    int edgesUsed = 0;

    while (!pq.empty() && edgesUsed < V - 1) {
        Edge e1 = pq.top(); pq.pop();

        int pu = find(e1.n1);
        int pv = find(e1.n2);

        if (pu != pv) {
            unite(e1.n1, e1.n2);
            cost += e1.wt;
            edgesUsed++;
        }
    }

    return cost;
}

    
};


// prim_heap_fast.cpp
#include <bits/stdc++.h>
using namespace std;

struct Graph {
    int num_v;
    vector<vector<pair<int,int>>> adj;
    vector<int> key;
    vector<char> out_cut;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> queue;

    Graph(int num_v) : num_v(num_v),
                       adj(num_v + 1),
                       key(num_v + 1, INT_MAX),
                       out_cut(num_v + 1, 1) {}

    void add_edge(int u, int v, int w_u_v) {
        adj[u].emplace_back(w_u_v, v);
        adj[v].emplace_back(w_u_v, u);
    }

    long long run_mst(int start_vertex) {
        key[start_vertex] = 0;
        queue.push({0, start_vertex});

        long long total_cost = 0;
        int visited_count = 0;

        while (!queue.empty()) {
            auto [cost_u, current_vertex] = queue.top();
            queue.pop();

            if (!out_cut[current_vertex]) continue;

            out_cut[current_vertex] = 0;
            total_cost += cost_u;
            visited_count++;

            for (const auto& [neigh_cost, neighbor] : adj[current_vertex]) {
                if (out_cut[neighbor] && neigh_cost < key[neighbor]) {
                    key[neighbor] = neigh_cost;
                    queue.push({neigh_cost, neighbor});
                }
            }
        }

        return (visited_count == num_v) ? total_cost : -1LL;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int num_v, num_e;
    while ( (cin >> num_v >> num_e) ) {
        Graph graph(num_v);
        for (int i = 0; i < num_e; ++i) {
            int u, v, c;
            cin >> u >> v >> c;
            graph.add_edge(u, v, c);
        }
        long long ans = graph.run_mst(1);
        if (ans < 0) {
            cout << "impossivel\n";
        } else {
            cout << ans << "\n";
        }
    }
    return 0;
}

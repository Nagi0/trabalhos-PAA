// O Código foi baseado em uma implementação feita em Python.
// Contudo, como a execução no Python estava demorando mais do que aceito pela plataforma, foi feita uma tradução para C++.
// A lógica do algoritmo permanece a mesma, a única mudança foi a linguagem implementada, aparentemente o Python não conseguiu comportar o limite de 2s.

// import sys
// import heapq
// from collections import defaultdict


// class Graph:
//     def __init__(self, num_v):
//         self.num_v = num_v
//         self.adj = defaultdict(lambda: defaultdict(int))
//         self.key = {}
//         self.out_cut = {}
//         self.queue = []

//     def add_edge(self, u, v, w_u_v):
//         if u not in self.adj.keys():
//             self.key[u] = float("inf")
//         if v not in self.adj.keys():
//             self.key[v] = float("inf")
//         self.adj[u][v] = w_u_v
//         self.adj[v][u] = w_u_v
//         self.out_cut[u] = True
//         self.out_cut[v] = True

//     def run_mst(self, start_vertex):
//         total_cost = 0
//         num_visited_v = 0

//         self.key[start_vertex] = 0
//         heapq.heappush(self.queue, (0, start_vertex))
//         self.key[start_vertex] = 0
//         self.out_cut[start_vertex] = False

//         while self.queue:
//             min_element = heapq.heappop(self.queue)
//             current_vertex_coast, current_vertex = min_element
//             total_cost += current_vertex_coast
//             num_visited_v += 1

//             self.out_cut[current_vertex] = False
//             neighbors_list = self.adj[current_vertex].keys()

//             for neighbor in neighbors_list:
//                 neigh_cost = self.adj[current_vertex][neighbor]
//                 if self.out_cut[neighbor] and self.key[neighbor] > neigh_cost:
//                     self.key[neighbor] = self.adj[current_vertex][neighbor]
//                     heapq.heappush(self.queue, (neigh_cost, neighbor))

//         if True in self.out_cut.values() or num_visited_v < self.num_v:
//             total_cost = "impossivel"
//         return total_cost


// if __name__ == "__main__":
//     data = sys.stdin.read().splitlines()
//     iterator = iter(data)

//     while True:
//         try:
//             info = next(iterator)
//         except:
//             break

//         num_v, num_e = info.split(" ")
//         graph = Graph(int(num_v))
//         for edge_idx in range(int(num_e)):
//             field_info = next(iterator)
//             vertex_u, vertex_v, cost = field_info.split(" ")
//             graph.add_edge(int(vertex_u), int(vertex_v), int(cost))

//         result = graph.run_mst(1)
//         print(result)

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

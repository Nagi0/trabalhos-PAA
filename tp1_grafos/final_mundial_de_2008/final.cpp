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
//         self.distances = {}
//         self.unvisited = set()
//         self.pi = {}
//         self.queue = []

//     def add_edge(self, u, v, w_u_v):
//         if u not in self.adj:
//             self.distances[u] = float("inf")
//             self.unvisited.add(u)
//         if v not in self.adj:
//             self.distances[v] = float("inf")
//             self.unvisited.add(v)

//         self.adj[u][v] = w_u_v

//     def reset_dijkstra(self):
//         self.pi.clear()
//         self.queue.clear()

//     def run_dijkstra(self, origin, destiny, t_allowed):
//         unvisited = self.unvisited.copy()
//         distances = self.distances.copy()
//         if origin == destiny:
//             return 0
//         elif t_allowed == 0:
//             if destiny in self.adj.get(origin, []):
//                 direct_connection = self.adj[origin][destiny]
//             else:
//                 direct_connection = -1

//             return direct_connection

//         distances[origin] = 0
//         heapq.heappush(self.queue, (0, origin))
//         distances[origin] = 0

//         while self.queue:
//             min_element = heapq.heappop(self.queue)
//             if min_element[1] not in unvisited:
//                 continue
//             current_vertex_coast, current_vertex = min_element
//             unvisited.remove(current_vertex)

//             if current_vertex == destiny:
//                 break

//             neighbors_list = self.adj[current_vertex].keys()

//             for neighbor in neighbors_list:
//                 if neighbor in unvisited and (neighbor <= t_allowed or neighbor == destiny):
//                     neigh_cost = self.adj[current_vertex][neighbor]
//                     neigh_total_coast = current_vertex_coast + neigh_cost
//                     if neigh_total_coast < distances[neighbor]:
//                         distances[neighbor] = neigh_total_coast
//                         self.pi[neighbor] = current_vertex
//                         heapq.heappush(self.queue, (neigh_total_coast, neighbor))

//         if distances[destiny] == float("inf"):
//             return -1
//         else:
//             return distances[destiny]


// if __name__ == "__main__":
//     data = sys.stdin.read().splitlines()
//     iterator = iter(data)
//     instance_counter = 1

//     while True:
//         try:
//             info = next(iterator)
//             sys.stdout.write(f"Instancia {instance_counter}\n")
//         except:
//             break

//         num_v, num_e = info.split(" ")
//         graph = Graph(int(num_v))
//         for edge_idx in range(int(num_e)):
//             field_info = next(iterator)
//             vertex_u, vertex_v, cost = list(map(int, field_info.split(" ")))
//             if vertex_v not in graph.adj.get(vertex_u, []):
//                 graph.add_edge(vertex_u, vertex_v, cost)
//             else:
//                 current_coast = graph.adj.get(vertex_u, {}).get(vertex_v, float("inf"))
//                 if cost < current_coast:
//                     graph.add_edge(vertex_u, vertex_v, cost)

//         eval_cases = int(next(iterator).strip())
//         for eval_c in range(eval_cases):
//             origin, destiny, t = next(iterator).split(" ")
//             result = graph.run_dijkstra(int(origin), int(destiny), int(t))
//             graph.reset_dijkstra()
//             sys.stdout.write(f"{result}\n")

//         sys.stdout.write("\n")
//         instance_counter += 1



#include <bits/stdc++.h>
using namespace std;

static constexpr long long INF = 1000000000000000LL; // 1e15

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    int instancia = 1;

    while ( (cin >> n >> m) ) {
        vector<vector<pair<int,int>>> adj(n+1);
        {
            vector<unordered_map<int,int>> tmp(n+1);
            for (int e = 0; e < m; ++e) {
                int u, v, w;
                cin >> u >> v >> w;
                auto it = tmp[u].find(v);
                if (it == tmp[u].end() || w < it->second) tmp[u][v] = w;
            }
            for (int u = 1; u <= n; ++u) {
                adj[u].reserve(tmp[u].size());
                for (auto &kv : tmp[u]) {
                    adj[u].push_back({kv.first, kv.second});
                }
            }
        }

        int q;
        cin >> q;

        cout << "Instancia " << instancia++ << "\n";

        for (int qi = 0; qi < q; ++qi) {
            int o, d, t;
            cin >> o >> d >> t;

            if (o == d) {
                cout << 0 << "\n";
                continue;
            }
            if (t == 0) {
                long long best = INF;
                for (auto [v, w] : adj[o]) if (v == d) best = min(best, (long long)w);
                cout << (best < INF ? best : -1) << "\n";
                continue;
            }

            vector<long long> dist(n+1, INF);
            vector<char> visited(n+1, 0);
            priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;

            auto can_enter = [&](int v) -> bool {
                return (v == d) || (v <= t);
            };

            dist[o] = 0;
            pq.push({0LL, o});

            while (!pq.empty()) {
                auto [du, u] = pq.top(); pq.pop();
                if (visited[u]) continue;
                visited[u] = 1;

                if (u == d) break;

                for (auto [v, w] : adj[u]) {
                    if (!can_enter(v)) continue;
                    long long nd = du + (long long)w;
                    if (nd < dist[v]) {
                        dist[v] = nd;
                        pq.push({nd, v});
                    }
                }
            }

            cout << (dist[d] < INF ? dist[d] : -1) << "\n";
        }
        cout << "\n";
    }
    return 0;
}

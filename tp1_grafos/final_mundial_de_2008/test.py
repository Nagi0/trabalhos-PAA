import sys

INF = 10**15


def readints():
    while True:
        line = open("tp1_grafos/final_mundial_de_2008/data.txt").readline()
        if not line:
            return None
        line = line.strip()
        if line:
            return list(map(int, line.split()))


def solve():
    inst = 1
    out = []
    while True:
        nm = readints()
        if nm is None:
            break
        n, m = nm

        # dist[i][j] = custo mínimo de i->j (sem intermediários ainda)
        dist = [[INF] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dist[i][i] = 0

        for _ in range(m):
            u, v, w = readints()
            if w < dist[u][v]:
                dist[u][v] = w  # manter a menor aresta entre dois nós

        c = readints()[0]
        queries = [tuple(readints()) for _ in range(c)]

        out.append(f"Instancia {inst}")

        # Agrupar consultas por t
        by_t = {}
        for idx, (o, d, t) in enumerate(queries):
            by_t.setdefault(t, []).append((idx, o, d))

        ans = [None] * c

        # t = 0: só voo direto (ou 0 se o==d)
        if 0 in by_t:
            for idx, o, d in by_t[0]:
                if o == d:
                    ans[idx] = 0
                else:
                    val = dist[o][d]
                    ans[idx] = val if val < INF else -1

        # Floyd–Warshall incremental: após k, só intermediários ≤ k
        for k in range(1, n + 1):
            dk = dist[k]
            for i in range(1, n + 1):
                ik = dist[i][k]
                if ik >= INF:
                    continue
                alt_row = ik
                di = dist[i]
                for j in range(1, n + 1):
                    v = alt_row + dk[j]
                    if v < di[j]:
                        di[j] = v

            # Responde consultas com t == k
            if k in by_t:
                for idx, o, d in by_t[k]:
                    if o == d:
                        ans[idx] = 0
                    else:
                        val = dist[o][d]
                        ans[idx] = val if val < INF else -1

        # Emite respostas na ordem
        for x in ans:
            out.append(str(x))
        out.append("")  # linha em branco após a instância
        inst += 1

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

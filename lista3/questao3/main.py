# DP for string concatenation with block costs (bottom-up)
#
# You can edit A, L or the cost function to experiment.
# The code will:
#  1) Precompute block costs C[t][j] and the argmin ArgB[t][j]
#  2) Run bottom-up DP to fill OPT, prev, piece, len
#  3) Produce detailed decision logs for each j (every candidate tried)
#  4) Reconstruct the optimal sequence of pieces
#  5) Save and display tables so you can inspect/debug
#
# Notation:
#  - A is 1-indexed in comments; Python uses 0-based indexes.
#  - t..j are inclusive positions on A (1-indexed).

from math import inf
import pandas as pd
from typing import List, Tuple, Dict, Optional


# ---------------------------
# Cost function (customizable)
# ---------------------------
def hamming_cost(A: str, t: int, j: int, B: str) -> float:
    """
    Hamming distance between A[t..j] and B if |B| == (j - t + 1).
    Return +inf if lengths don't match.
    Here t and j are 1-based and inclusive.
    """
    seg = A[t - 1 : j]  # Python slice is 0-based and exclusive on end
    if len(seg) != len(B):
        return inf
    return sum(1 for a, b in zip(seg, B) if a != b)


# ---------------------------
# Precompute block costs C[t][j]
# ---------------------------
def build_block_costs(A: str, L: List[str], n: int):
    """
    Build C[t][j] = min_B cost to align A[t..j] with some B in L (|B| == j-t+1)
    and ArgB[t][j] = that argmin B. Use 1-based indexing for t,j.
    """
    m = len(A)
    # Initialize (m+1) x (m+1) with +inf / None so indices 1..m are valid
    C = [[inf] * (m + 1) for _ in range(m + 1)]
    ArgB = [[None] * (m + 1) for _ in range(m + 1)]

    # Group pieces by length for quick access
    by_len: Dict[int, List[str]] = {}
    for B in L:
        by_len.setdefault(len(B), []).append(B)

    for t in range(1, m + 1):
        for j in range(t, min(m, t + n - 1) + 1):  # only lengths up to n
            ell = j - t + 1
            best = inf
            bestB = None
            for B in by_len.get(ell, []):
                cost = hamming_cost(A, t, j, B)
                if cost < best:
                    best = cost
                    bestB = B
            C[t][j] = best
            ArgB[t][j] = bestB
    return C, ArgB


# ---------------------------
# Bottom-up DP
# ---------------------------
def dp_concat(A: str, L: List[str], n: int, C, ArgB):
    """
    Bottom-up DP:
      OPT[j]   = min over ell=1..min(n,j) of OPT[j-ell] + C[j-ell+1][j]
      prev[j]  = j-ell*      (for chosen ell*)
      piece[j] = ArgB[j-ell*+1][j]
      length[j]= ell*
    Also returns a detailed decision log.
    """
    m = len(A)
    OPT = [inf] * (m + 1)
    prev = [-1] * (m + 1)
    piece = [None] * (m + 1)
    length = [0] * (m + 1)

    OPT[0] = 0.0
    prev[0] = -1

    decision_rows = []  # for a detailed log
    for j in range(1, m + 1):
        best_val = inf
        best_tuple = None  # (ell, t, B, total, opt_prev, block_cost)
        for ell in range(1, min(n, j) + 1):
            t = j - ell + 1
            block_cost = C[t][j]
            B = ArgB[t][j]
            opt_prev = OPT[t - 1]
            total = opt_prev + block_cost
            decision_rows.append(
                {
                    "j": j,
                    "ell (length)": ell,
                    "t (start)": t,
                    "A[t..j]": A[t - 1 : j],
                    "B (ArgB[t][j])": B,
                    "OPT[t-1]": opt_prev,
                    "C[t][j] (block cost)": block_cost,
                    "total = OPT[t-1] + C[t][j]": total,
                }
            )
            if total < best_val:
                best_val = total
                best_tuple = (ell, t, B, total, opt_prev, block_cost)

        # commit best for j
        OPT[j] = best_val
        if best_tuple is not None:
            ell, t, B, total, opt_prev, block_cost = best_tuple
            prev[j] = t - 1
            piece[j] = B
            length[j] = ell

    return OPT, prev, piece, length, decision_rows


# ---------------------------
# Reconstruction
# ---------------------------
def reconstruct_solution(A: str, prev, piece, length):
    j = len(A)
    seq = []
    while j > 0:
        ell = length[j]
        t = j - ell + 1
        seq.append((piece[j], t, j, A[t - 1 : j]))
        j = prev[j]
    seq.reverse()
    return seq


# ---------------------------
# Example run (you can edit this section)
# ---------------------------
A = "ababa"
L = ["a", "b", "ab", "ba", "aa"]
n = 2  # max piece length

# Build costs
C, ArgB = build_block_costs(A, L, n)

# Run DP
OPT, PREV, PIECE, LEN, log_rows = dp_concat(A, L, n, C, ArgB)
seq = reconstruct_solution(A, PREV, PIECE, LEN)

# ---------------------------
# Display / Save Tables
# ---------------------------
# 1) Block costs in long-format for easy viewing
rows = []
m = len(A)
for t in range(1, m + 1):
    for j in range(t, m + 1):
        val = C[t][j]
        rows.append(
            {
                "t": t,
                "j": j,
                "substring A[t..j]": A[t - 1 : j],
                "ArgB[t][j]": ArgB[t][j],
                "C[t][j]": val if val < inf else None,
            }
        )
df_C = pd.DataFrame(rows)

# 2) Decision log (all candidates for each j)
df_log = pd.DataFrame(log_rows)

# 3) DP summary (per j)
df_dp = pd.DataFrame({"j": list(range(0, m + 1)), "OPT[j]": OPT, "prev[j]": PREV, "piece[j]": PIECE, "len[j]": LEN})

# 4) Chosen sequence (reconstructed)
df_seq = pd.DataFrame([{"piece": p, "t": t, "j": j, "A[t..j]": seg} for (p, t, j, seg) in seq])

# Save to CSVs
df_C.to_csv("./lista3/questao3block_costs_C.csv", index=False)
df_log.to_csv("./lista3/questao3decision_log.csv", index=False)
df_dp.to_csv("./lista3/questao3dp_summary.csv", index=False)
df_seq.to_csv("./lista3/questao3solution_sequence.csv", index=False)

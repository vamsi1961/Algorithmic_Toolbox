





## KNAPSACK

    Greedy approach gives an optimal solution for Fractional Knapsack.

    If c[i, w] = c[i-1, w], then item i is not part of the solution, and we continue tracing with c[i-1, w]. Otherwise, item i is part of the solution, and we continue tracing with c [i-1, w-W].
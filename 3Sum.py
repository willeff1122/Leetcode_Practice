class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        solution = set()
        p, n, z = [], [], []

        for i in nums:
            if i < 0:
                n.append(i)
            elif i > 0:
                p.append(i)
            else:
                z.append(i)

        N, P = set(n), set(p)
        # The reason why we convert n and p into N, P is to save time.
        # Also, we can eliminate identical objects.
        # Below we can also use sorted instead of if and else statement.

        if len(z) > 0:
            for i in P:
                if -1 * i in N:
                    solution.add((-1 * i, 0, i))

        if len(z) >= 3:
            solution.add((0, 0, 0))

        for i in range(len(n) - 1):
            for j in range(i + 1, len(n)):
                if -1 * (n[i] + n[j]) in P:
                    if n[i] < n[j]:
                        solution.add((n[i], n[j], -1 * (n[i] + n[j])))
                    else:
                        solution.add((n[j], n[i], -1 * (n[i] + n[j])))

        for i in range(len(p) - 1):
            for j in range(i + 1, len(p)):
                if -1 * (p[i] + p[j]) in N:
                    if p[i] < p[j]:
                        solution.add((-1 * (p[i] + p[j]), p[i], p[j]))
                    else:
                        solution.add((-1 * (p[i] + p[j]), p[j], p[i]))


        return solution

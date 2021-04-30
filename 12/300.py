# --

class IntergalacticCake:
    def getSlices(S, n, m, h, v):
        r = b = s = 0
        l = 1
        if n - m:
            for H in h:
                s += ~m < H <= m
                l += 1
            a = s > 0
            s -= a
            l -= s
            r = l + s * 2
            for V in v:
                if ~m < V <= m:
                    r += b - s
                    b = 1 ^ a
                r += l + s
        return r

# --

print(IntergalacticCake().getSlices(5, 3, [-4], [4]))
print(IntergalacticCake().getSlices(5,
                                    3,
                                    [],
                                    []))
print(IntergalacticCake().getSlices(36,
                                    15,
                                    [],
                                    [19]))
# print(IntergalacticCake().getSlices(39,
                                    # 18,
                                    # [-22,38],
                                    # [-4,-10,-19,24,21,-15,18,4,22,37,-35,28,1,11,3,-27,12]))
print(IntergalacticCake().getSlices(37, 1, [], [-1,-33]))
print(IntergalacticCake().getSlices(5, 5, [-4, -4], [-1, 2, -2, 0]))

""" 353
class IntergalacticCake:
    def getSlices(S, n, m, h, v):
        r = b = s = 0
        l = 1
        if n - m:
            for H in h:
                s += ~m < H <= m
                l += 1
            a = s > 0
            s -= a
            l -= s
            r = l + s * 2
            for V in v:
                if ~m < V <= m:
                    r += b - s
                    b = 1 ^ a
                r += l + s
        return r
"""

""" 351
class IntergalacticCake:
    def getSlices(S, n, m, h, v):
        r = b = 0
        if n - m:
            A = sum(~m < H <= m for H in h)
            s = A - (A > 0)
            l = len(h) - s + 1
            r = l + s * 2
            for V in v:
                if ~m < V <= m:
                    r += b - s
                    b = A < 1
                r += l + s
        return r
"""


""" 353
class IntergalacticCake:
    def getSlices(S, n, m, h, v):
        r = a = b = s = 0
        l = 1
        if n - m:
            for H in h:
                if ~m < H <= m:
                    s += a
                    l -= a
                    a = 1
                l += 1
            r = l + s * 2
            for V in v:
                if ~m < V <= m:
                    r += b - s
                    b = 1 - a
                r += l + s
        return r
"""


""" 324
class IntergalacticCake:
    def getSlices(S, n, m, h, v):
        r = a = b = s = 0
        if n - m:
            l = 1
            for H in h:
                if -m <= H <= m:
                    a += 1
                    if a > 1:
                        s += 1
                    else:
                        l += 1
                else:
                    l += 1
            r = l + s * 2
            for V in v:
                if -m <= V <= m:
                    b += 1
                    r += (b > 1 > a) + l
                else:
                    r += l + s
        return r
"""


""" 208
class IntergalacticCake:
    def getSlices(self, n, m, h, v):
        r = range
        N = 2 * n
        R = r(n - m, n + m)
        L = r(N)
        p = {}
        k = 0

        for y in L:
            for x in L:
                F = 0
                S = [(x, y)]
                while S:
                    *S, c = S
                    i, j = c
                    if i in L and j in L and c not in p and not (i in R and j in R):
                        F = 1
                        p[c] = k
                        if i - n + 1 not in v:
                            S += (i + 1, j),
                        if i - n not in v:
                            S += (i - 1, j),
                        if j - n + 1 not in h:
                            S += (i, j + 1),
                        if j - n not in h:
                            S += (i, j - 1),
                k += F
        return k
"""

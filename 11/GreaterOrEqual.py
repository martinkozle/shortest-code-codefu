import bisect
import heapq


class GreaterOrEqual:
    def getMinimumX(s, t, k):
        a, *p = sorted([0] + t)[~k:]
        return -(a in p or ~a)


# class GreaterOrEqual:
#     def getMinimumX(s, t, k):
#         *_, a, b = [0] + heapq.nlargest(k + 1, [0] + t)
#         return -(b == a or ~b)

# class GreaterOrEqual:
#     def getMinimumX(s, t, k):
#         t += 0,
#         t.sort()
#         p = ~t[~k]
#         return -(~t[-k] >= p or p)

# class GreaterOrEqual:
#    def getMinimumX(s, t, k):
#        t += 0,
#        t.sort()
#        p = t[~k]
#        return -(p < t[-k]) & p + 1

# class GreaterOrEqual:
#     def getMinimumX(s, t, k):
#         t += 0,
#         t.sort()
#         p = t[~k]
#         return -(p > t[-k] or ~p)

# class GreaterOrEqual:
#     getMinimumX = lambda s, t, k: eval("-( ]== +1]or~ ])".replace(' ', "sorted([0] + t)[~k"))

# class GreaterOrEqual:
#     def getMinimumX(s, t, k):
#         t += 0,
#         t.sort()
#         a, b = t[~k], t[-k]
#         return -(a == b or ~a)

# class GreaterOrEqual:
#     getMinimumX = lambda s, t, k: -(t.append(0) or t.sort() or t[~k] == t[-k] or ~t[~k])

# class GreaterOrEqual:
#     getMinimumX = lambda s, t, k: (t.append(0) != t.sort()) | -(t[~k] == t[-k] or ~t[~k])

# class GreaterOrEqual:
#     def getMinimumX(s, t, k):
#         t.sort()
#         return -(([0] + t)[~k] == t[-k] or ~([0] + t)[~k])

# class GreaterOrEqual:
#     def getMinimumX(s, t, k):
#         t += 0,
#         t.sort()
#         n = t[~k]
#         return -(t.count(n) > 1 or ~n)

# f = lambda x, i: sorted([0] + x)[~i]
#
#


# class GreaterOrEqual:
#     getMinimumX = lambda s, t, k: -~next((x for x in [0] + t if sum(i > x for i in t) == k), -2)
# getMinimumX = lambda s, t, k: ([x for x in [0] + t if sum(i > x for i in t) == k] + [-2])[0] + 1

# getMinimumX = lambda s, t, k: sorted([0] + t)[-k-1] + 1
# getMinimumX = lambda s, t, k: ([i + 1 for i in t if len(t) - sorted(t).index(i) - 1 == k] + [len(t) == k or -1])[0]
# getMinimumX = lambda s, t, k: sorted(t)[max([8 - bisect.bisect(sorted(t), i + 1) for i in t + [0]])]
# getMinimumX = lambda s, t, k: (list(filter(lambda x: sum(i >= x for i in t) == k, range(1, 7**6))) + [-1])[0]


# getMinimumX = lambda s, t, k:  if len([i for i in t if i > k])

goe = GreaterOrEqual()
print(goe.getMinimumX([3, 8, 5, 1, 10, 3, 20, 24], 2))  # 11
print(goe.getMinimumX([71, 25, 69, 71, 68, 21, 39], 3))  # 69
print(goe.getMinimumX([87891, 9944], 2))  # 1
print(goe.getMinimumX(
    [105, 121, 136, 149, 125, 133, 134, 108, 147, 106, 105, 134, 137, 105, 135, 117, 132, 149, 140, 102, 147, 101, 123,
     145, 102, 113, 106, 112, 127, 121, 136, 128, 141, 126, 143, 124, 141, 149, 140, 147, 123, 143, 143, 135, 114, 119,
     101, 104, 138, 128, 146], 50))  # -1

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        t += 0,
        t.sort()
        p = t[~k]
        return -(p == t[-k] or ~p)
"""  # 417 SUBMITTED

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        t += 0,
        t.sort()
        p = t[~k]
        return -(p == t[-k]) | p + 1
"""  # 417

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        t += 0,
        t.sort()
        return -(t[~k] == t[-k] or ~t[~k])
"""  # 416

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        t += 0,
        t.sort()
        return -(t[~k] == t[-k]) | t[~k] + 1
"""  # 416 gospod znae kako raboti ova

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        t += 0,
        t.sort()
        p = ~t[~k]
        return -p ** (p != ~t[-k])
"""  # 416

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        t += 0,
        t.sort()
        return -(~t[~k], 1)[t[~k] == t[-k]]
"""  # 414

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        w = sorted([0] + t)
        return -(~w[~k], 1)[w[~k] == w[-k]]
"""  # 412

"""
class GreaterOrEqual:
    getMinimumX = lambda s, t, k: -~next((x for x in [0] + t if sum(i > x for i in t) == k), -2)
"""  # 411

"""
class GreaterOrEqual:
    getMinimumX = lambda s, t, k: -(t.append(0) == t.sort(), ~t[~k])[t[~k] != t[-k]]
"""  # 411

"""
class GreaterOrEqual:
    getMinimumX = lambda s, t, k: ([x + 1 for x in [0] + t if sum(i > x for i in t) == k] + [-1])[0]
"""  # 410

"""
class GreaterOrEqual:
    getMinimumX = lambda s, t, k: ([x + 1 for x in range(7**6) if sum(i > x for i in t) == k] + [-1])[0]
"""  # 404

"""
class GreaterOrEqual:
    getMinimumX = lambda s, t, k: (list(filter(lambda x: sum(1 for i in t if i > x) == k, range(max(t) + 1))) + [-2])[0] + 1
"""  # 385

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        t.sort()
        l = len(t)
        x = t[l - k - 1]
        r = t[l - 1]
        if k == l:
            r = 0 if t[0] else -2
        elif k:
            r = x if x < t[l - k] else -2
        return r + 1
"""  # 368

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        t.sort()
        l = len(t)
        if k == l:
            return 1 if t[0] else -1
        if k:
            x = t[l-k-1] + 1
            return x if x <= t[l-k] else -1
        return t[l-1] + 1
"""  # 362

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        t.sort()
        l = len(t)
        x = t[l - k - 1] + 1
        return (1 if t[0] else -1) if k == 1 else ((x if x <= t[l-k] else -1) if k else t[l-1] + 1)
"""  # 362

"""
class GreaterOrEqual:
    def getMinimumX(s, t, k):
        t.sort()
        l = len(t)
        return -1 if l == 0 or k > l else (1 if k == l else (t[-1] + 1 if k == 0 else (-1 if t[-k] == t[-k - 1] else (t[-k - 1] + 1))))
"""  # 352

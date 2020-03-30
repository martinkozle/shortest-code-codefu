e = enumerate


class Transform:
    minTransformations = lambda s, a, b: min(sum(abs(i - j) for i, j in zip(a, b[i:] + b)) + i for i in range(99))
    # def minTransformations(s, a, b):
    #     i = 0
    #     for x in a:
    #         min(sum(abs(i - j) for i, j in zip(a[-i:] + a, b)) + i
    #         i += 1
    #     return



# class Transform:
#     minTransformations = d = lambda s, a, b, r=0: r > 99 and 1e9 or min(sum(abs(i - j) for i, j in zip(a, b)) + r, s.d(a[-1:] + a[:-1], b, r+1))

# class Transform:
#     minTransformations = d = lambda s, a, b: min(sum(map(lambda x, y: abs(x - y), a[-i:] + a, b)) + i for i in range(99))
# minTransformations = lambda s, a, b: min(sum(abs(a[j-i] - p) for j, p in e(b)) + i for i, _ in e(a))
# def minTransformations(s, a, b, r=0):
#     print(a, b, r)
#     print(sum(abs(i - j) for i, j in zip(a, b)) + r)
#     return min(sum(abs(i - j) for i, j in zip(a, b)) + r, s.minTransformations(a[-1:] + a[:-1], b, r+1)) if r < 99 else 1e9


# d = min(sum(abs(a[j-i] - b[j]) for j in range(len(a))) + i for i in range(len(a)))
tr = Transform()
print(tr.minTransformations([8, 5, 1, 10, 5, 9, 9], [3, 5, 6, 6, 2, 8, 2]))

"""
class Transform:
    minTransformations = lambda s, a, b: min(sum(abs(i - j) for i, j in zip(a, b[i:] + b)) + i for i in range(99))
"""  # 397 SUBMITTED

"""
class Transform:
    minTransformations = lambda s, a, b: min(sum(abs(i - j) for i, j in zip(a[-i:] + a, b)) + i for i in range(99))
"""  # 396

"""
e = enumerate
class Transform:
    minTransformations = lambda s, a, b: min(sum(abs(a[j-i] - p) for j, p in e(b)) + i for i, _ in e(a))
"""  # 394 SUBMITTED

"""
class Transform:
    def minTransformations(s, a, b):
        r = range(len(a))
        return min(sum(abs(a[j-i] - b[j]) for j in r) + i for i in r)
"""  # 393

"""
class Transform:
    def minTransformations(s, a, b):
        l = len(a)
        r = range(l)
        return min(sum(abs((a[l - i:] + a)[j] - b[j]) for j in r) + i for i in r)
"""  # 382

"""
class Transform:
    def minTransformations(s, a, b):
        l = len(a)
        return min(sum(abs(k - j) for k, j in zip(a[i:] + a, b)) - i or l for i in range(l)) + l
"""  # 381

"""
l = len
r = range
class Transform:
    minTransformations = lambda s, a, b: min(sum(abs(a[(j - i) % l(a)] - b[j]) for j in r(l(a))) + i for i in r(l(a)))
"""  # 381

"""
class Transform:
    def minTransformations(s, a, b):
        l = len(a)
        return min(sum(abs(k - j) for k, j in zip(a[i:] + a[:i], b)) + (l - i) % l for i in range(l))
"""  # 376

"""
l = len
class Transform:
    minTransformations = lambda s, a, b: min(sum(abs(k - j) for k, j in zip(a[l(a) - i:] + a[:l(a) - i], b)) + i for i in range(l(a)))
"""  # 376

"""
class Transform:
    minTransformations = d = lambda s, a, b, r=0: min(sum(abs(i - j) for i, j in zip(a, b)) + r, s.d(a[-1:] + a[:-1], b, r+1)) if r < 99 else 1e9
"""  # 374 recursive

import re

class BeautifulString:
  remove = lambda _,a: min(a[i:].find(a[i],1) % 99 for i in range(len(a))) % 98 - 1

# e = enumerate
# class BeautifulString:
#     # remove = lambda s, t: min(abs(j - i) for j, k in e(t) for i, p in e(t) if k == p and j - i) - 1
#     remove = lambda s, t: min(min(map(len, t.split(i)[1:-1]), default=98) for i in t) + 1 % 99 - 1

# f=lambda s:set(s)and{s}|f(s[1:])|f(s[:-1])
# class BeautifulString:
#     remove = lambda s, t: min(len(i) - 2 for i in f(t) if i[0] == i[-1] and len(i) > 1)
    # remove = lambda s, t: min(len(next(sorted(t.split(i)[1:-1], key=len), '                                                                                                  ')) + 1 for i in t) % 99 - 1

# l = len
# class BeautifulString:
#     remove = lambda s, t: -(l(set(t)) == l(t) or -min(min([l(j) for j in t.split(i)[1:-1]] + [99]) for i in t))


bs = BeautifulString()
print(bs.remove("nfsloxcpfijv"))  # 6
print(bs.remove("fdcsaytrntdlrv"))  # 2
print(bs.remove("orbajcknlagsknjbrfhkoltdcyawnoku"))  # 5
print(bs.remove("omvxfdinaewlfvtdbiykvlxmghbkfpdnamruiwkhytjicgnvofdgwbtxjqlfybnxtsvucpyfrxsueglihadysfwxgjobwagdlipt"))  # 5

"""
class BeautifulString:
    remove = lambda s, t: min(min(map(len, ('                                                                                                  %s                                                                                                  ' % t).split(i))) + 1 for i in t) % 99 - 1
"""  # 412 SUBMITTED

"""
class BeautifulString:
    remove = lambda s, t: min(min(map(len, ('                                                                                                  ' + t + '                                                                                                  ').split(i))) + 1 for i in t) % 99 - 1
"""  # 411

"""
class BeautifulString:
    remove = lambda s, t: min(min([len(j) + 1 for j in t.split(i)][1:-1] + [99]) for i in t) % 99 - 1
"""  # 403

"""
class BeautifulString:
    def remove(s, t):
        return sorted([min([len(j) + 1 for j in t.split(i)][1:-1] + [99]) for i in t])[0] % 99 - 1
"""  # 397

"""
class BeautifulString:
    def remove(s, t):
        a = min(min([len(j) for j in t.split(i)][1:-1] + [99]) for i in t)
        return (-1, a)[a!=99]
"""  # 391

"""
class BeautifulString:
    def remove(s, t):
        l = len(t)
        r = range
        return min(min([j - i for j in r(i + 1, l) if t[i] == t[j]] + [l]) for i in r(l)) % l - 1
"""  # 384

"""
l = len
class BeautifulString:
    remove = lambda s, t: min([min([j - i for j in range(i + 1, l(t)) if t[i] == t[j]] + [l(t)]) for i in range(l(t))]) % l(t) - 1
"""  # 376

""" import re
class BeautifulString:
    remove = lambda s, t: min(len(re.search('(%s[^%s]*(%s|`))' % ((t[i],) * 3), t[i:] + '                                                                                                             ` ').group(0)) for i in range(len(t))) % 110 - 2
"""  # 373 regex solution

# --

class BlackBenduday:
    savings = lambda s, p, d, k: '%.2f' % sum(sorted(P * D / 100 for P, D in zip(p, d))[-k:])


# --

print(BlackBenduday().savings([100,205,310,205,100], [10,66,10,10,30], 3))

""" 411
class BlackBenduday:
    savings = lambda s, p, d, k: '%.2f' % sum(sorted(e * t / 100 for e, t in zip(p, d))[-k:])
"""
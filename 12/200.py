# --


_=0
class SpaceTravel:
    findTimestep = lambda s, a, _a: eval("a.index('Eset')-_" * 2) % len(a) + 1


# --

""" 418
_=0
class SpaceTravel:
    findTimestep = lambda s, a, _a: eval("a.index('Eset')-_" * 2) % len(a) + 1
"""

""" 418
e = 'Eset'
class SpaceTravel:
    findTimestep = lambda s, a, r: (a.index(e) - r.index(e)) % len(a) + 1
"""

""" 414
class SpaceTravel:
    findTimestep = lambda s, a, b: eval(".index('Eset')-".join('ab0')) % len(a) + 1
"""

""" 414
class SpaceTravel:
    def findTimestep(s, a, r):
        e = 'Eset'
        return (a.index(e) - r.index(e)) % len(a) + 1
"""

""" 399
class SpaceTravel:
    def findTimestep(s, a, r):
        e = 'Eset'
        i = a.index(e)
        j = r.index(e)
        while i < j:
            i += len(a)
        return i - j + 1
"""

""" 404
class SpaceTravel:
    def findTimestep(s, a, r):
        e = 'Eset'
        l = len(a)
        t = ~a.index(e) + r.index(e)
        return t // l * l - t + l
"""

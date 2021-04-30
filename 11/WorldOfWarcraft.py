# --

class WorldOfWarcraft:
    def getExperience(s, r, l, t):
        for i in t:
            r -= i
            if r < 0:
                return -r

# --

# class WorldOfWarcraft:
#     getExperience = d = lambda s, r, l, t: -r if r < 0 else s.d(r-t[l - len(t)], l + 1, t)


wow = WorldOfWarcraft()
print(wow.getExperience(521286, 8, [31058, 39932, 308600, 316250, 516273, 598129, 720219, 904635]))


"""
class WorldOfWarcraft:
    def getExperience(s, r, l, t):
        for i in t:
            r -= i
            if r < 0:
                return -r
"""  # 427 SUBMITTED

"""
class WorldOfWarcraft:
    def getExperience(s, r, l, t):
        for i in t:
            if r <= 0:
                break
            r -= i
        return -r
"""  # 421


"""
class WorldOfWarcraft:
    def getExperience(s, r, l, t):
        i = 0
        while r > 0:
            r -= t[i]
            i += 1
        return -r
"""  # 422

"""
class WorldOfWarcraft:
    getExperience = d = lambda s, r, l, t: -r if r < 0 else s.d(r-t[0], l, t[1:])
"""  # 419 fun recursive solution

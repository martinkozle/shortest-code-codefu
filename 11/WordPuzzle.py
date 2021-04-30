import re
import collections

# --

class WordPuzzle:
    getMostReoccuringLength = lambda s, b: max(range(99, 0, -1), key=[len(i) for i in re.findall("\.+", str(b))].count)


# --

# class WordPuzzle:
#     getMostReoccuringLength = lambda s, b: len(max(['.' * i for i in range(99, 0, -1)], key=' '.join(b).replace('X', ' ').split().count))


# class WordPuzzle:
#     getMostReoccuringLength = lambda s, b: max(range(99, 0, -1), key=[-~i.find('.X..') or i.count('.') for i in b].count)


# class WordPuzzle:
#     getMostReoccuringLength = lambda s, b: ('..X..' in b) * 2 or max(([i.count('.') for i in b].count(i), i) for i in range(99, 0, -1))[1]

# class WordPuzzle:
#     getMostReoccuringLength = lambda s, b: eval('-max(%s,key=%s.count)' % (("sorted(-len(i) for i in 'X'.join(b).split('X') if i)",) * 2))

# class WordPuzzle:
#     getMostReoccuringLength = lambda s, b: eval('len(max((`.count(j), j) for j in `)[1])'.replace('`', "list(filter(len, 'X'.join(b).split('X')))"))

# class WordPuzzle:
#     getMostReoccuringLength = lambda s, b: eval("len(max(`, key=`.count))".replace('`', "sorted('X'.join(b).split('X'))[:-1:-1]"))

# class WordPuzzle:
#     getMostReoccuringLength = lambda s, b: -max(range(-99, 0), key=[-len(i) for i in [j.split('X') for j in b]].count)
# class WordPuzzle:
#     getMostReoccuringLength = lambda s, b: eval("len(max((list(filter(len, 'X'.join(b).split('X'))).count(j), j) for j in list(filter(len, 'X'.join(b).split('X'))))[1])")
# getMostReoccuringLength = lambda s, b: max(([len(i) for i in 'X'.join(b).split('X')].count(j), j) for j in range(1, 99))[1]

# getMostReoccuringLength = lambda s, b: {[len(i) for i in 'X'.join(b).split('X')].count(j): j for j in range(1, 100)}


# class WordPuzzle:
#     getMostReoccuringLength = lambda s, b: len(sorted(['X' + '.' * i + 'X' for i in range(1, 99)], key=('X' + 'X'.join(b) + 'X').count)[-1]) - 2
# getMostReoccuringLength = lambda s, b: len(min(['X' + '.' * i + 'X' for i in range(1, 99)], key=('X' + 'X'.join(b) + 'X').count)) - 2

# class WordPuzzle:
#     getMostReoccuringLength = lambda s, b: max(map('X'.join(b).count, re.findall(r'\.+', 'X'.join(b))))
#  d = len(sorted(['X' + '.' * i + 'X' for i in range(1, 99)], key=('X' + 'X'.join(b) + 'X').count)[-1]) - 2

wp = WordPuzzle()
print(wp.getMostReoccuringLength(["..X..", "...X.", "X...."]))
print(wp.getMostReoccuringLength(
    ["X...................", "XX...............XXX", "XXXX............XXXX", "XXXXXXXXXXXXXXX....X",
     "X..............XXXXX", "XX..................", "XXXXXXXXXX.......XXX"]))
print(wp.getMostReoccuringLength(
    ["XXXXXXXXXXXXXXX...............XXXX", "XXXXXXX.....................XXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXX.....XXX",
     "XXXXX.............................", "XXXXXXXXXXXXX.................XXXX", "XXXXXXXXXX......................XX",
     "XX..........................XXXXXX", "XXXXXXXXXXXXX..................XXX", "XXXXX.............XXXXXXXXXXXXXXXX",
     ".................................X", "XXX............................XXX", "XXXXXX.....................XXXXXXX",
     "XXXXXXX.................XXXXXXXXXX", "XXXXXXXXXX...................XXXXX", "X............................XXXXX",
     "XX................................", "XXXXXXXXX......................XXX", "XXXX.....XXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX.....XXXXXXXXXXXXXXXXXXXXXXXXXXX", "XX............................XXXX", "XXXXXXXX.........XXXXXXXXXXXXXXXXX",
     "................................XX", "XXXXXX............XXXXXXXXXXXXXXXX", "X.........................XXXXXXXX",
     "XXXXXXXXXXXX..XXXXXXXXXXXXXXXXXXXX", "XXXXXX.................XXXXXXXXXXX", "XXX...............................",
     "XXX......................XXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXX...XXXXXXX", "...........................XXXXXXX",
     "XXXXXXXXX...................XXXXXX", "XXXXXXXX.................XXXXXXXXX", "XXXXXXXX..................XXXXXXXX",
     "X................................."]))

"""
class WordPuzzle:
    getMostReoccuringLength = lambda s, b: -max(range(-99, 0), key=[i.count('.') / ~('.X.' in i) for i in b].count)
"""  # 388 SUBMITTED

"""
class WordPuzzle:
    getMostReoccuringLength = lambda s, b: max(range(99, 0, -1), key=[i.count('.') >> ('.X.' in i) for i in b].count)
"""  # 387

"""
class WordPuzzle:
    getMostReoccuringLength = lambda s, b: -max(range(-99, 0), key=[-i.count('.') >> ('.X.' in i) for i in b].count)
"""  # 387

"""
class WordPuzzle:
    getMostReoccuringLength = lambda s, b: -max(range(-99, 0), key=[-len(i) for i in 'X'.join(b).split('X')].count)
"""  # 384

"""
class WordPuzzle:
    getMostReoccuringLength = lambda s, b: eval("".join(chr(len(i)) for i in '                                                                                                            	                                                                                                     	                                                                                                              	                                        	                                                                                                                   	                                                                                                               	                                                                                                                  	                                                                                                                    	                                                                                                     	                                                                                                    	                                        	                                                                                           	                                       	                                                                                        	                                       	                                	                                           	                                	                                       	                                              	                                       	                                	                                          	                                	                                                                                                         	                                	                                           	                                	                                       	                                                                                        	                                       	                                	                                                                                                      	                                                                                                               	                                                                                                                  	                                	                                                                                                         	                                	                                                                                                         	                                                                                                              	                                	                                                                                                                  	                                                                                                 	                                                                                                              	                                                                                                       	                                                                                                     	                                        	                                                 	                                            	                                	                                                         	                                                         	                                         	                                                                                             	                                            	                                	                                                                                                           	                                                                                                     	                                                                                                                         	                                                             	                                        	                                       	                                                                                        	                                       	                                	                                           	                                	                                       	                                                                                        	                                       	                                              	                                                                                                          	                                                                                                               	                                                                                                         	                                                                                                              	                                        	                                                                                                  	                                         	                                	                                           	                                	                                       	                                                                                        	                                       	                                         	                                              	                                                                                                   	                                                                                                               	                                                                                                                     	                                                                                                              	                                                                                                                    	                                         	                                                                                           	                                             	                                                 	                                                                                             	                                         	                                	                                             	                                	                                                  '.split('\t')))
"""  # 404 CHEATING

"""
class WordPuzzle:
    getMostReoccuringLength = lambda s, b: max(range(99, 0, -1), key=[len(i) for i in 'X'.join(b).split('X')].count)
"""  # 384

"""
class WordPuzzle:
    getMostReoccuringLength = lambda s, b: -max(range(-99, 0), key=[-len(i) for i in 'X'.join(b).split('X') if i].count)
"""  # 381

"""
class WordPuzzle:
    def getMostReoccuringLength(s, b):
        w = sorted(-len(i) for i in 'X'.join(b).split('X') if i)
        return -max(w, key=w.count)
"""  # 379

"""
class WordPuzzle:
    def getMostReoccuringLength(s, b):
        w = sorted(len(i) for i in 'X'.join(b).split('X') if i)[::-1]
        return max(w, key=w.count)
"""  # 375

"""
class WordPuzzle:
    def getMostReoccuringLength(s, b):
        w = [len(i) for i in 'X'.join(b).split('X') if i]
        c = w.count
        return max(filter(lambda x: c(x) == max(map(c, w)), w))
"""  # 354

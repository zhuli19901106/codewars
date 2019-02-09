# seriously?
# you gotta be kidding me.
class Puzzle(object):
    __call__ = lambda self, n, x: n * 2 ** x

puzzle = Puzzle()

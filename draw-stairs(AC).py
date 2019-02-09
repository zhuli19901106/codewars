def draw_stairs(n):
    return '\n'.join(map(lambda x: ''.join([' ' for i in range(0, x)]) + 'I', range(n)))

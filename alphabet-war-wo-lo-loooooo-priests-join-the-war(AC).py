SCORE_LEFT = {'w': 4, 'p': 3, 'b': 2, 's': 1}
SCORE_RIGHT = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
FLIP_LEFT = {'m': 'w', 'q': 'p', 'd': 'b', 'z': 's'}
FLIP_RIGHT = {'w': 'm', 'p': 'q', 'b': 'd', 's': 'z'}
MAGIC_LEFT = 't'
MAGIC_RIGHT = 'j'

def alphabet_war(fight):
    a = list(fight)
    n = len(a)
    score_left = 0
    score_right = 0
    for i in range(n):
        f = 0
        if a[i] == MAGIC_LEFT or a[i] == MAGIC_RIGHT:
            continue
        if (i > 0 and a[i - 1] == MAGIC_LEFT) or (i < n - 1 and a[i + 1] == MAGIC_LEFT):
            f |= 0x1
        if (i > 0 and a[i - 1] == MAGIC_RIGHT) or (i < n - 1 and a[i + 1] == MAGIC_RIGHT):
            f |= 0x2
        if f == 1 and a[i] in FLIP_LEFT:
            a[i] = FLIP_LEFT[a[i]]
        if f == 2 and a[i] in FLIP_RIGHT:
            a[i] = FLIP_RIGHT[a[i]]
        if a[i] in SCORE_LEFT:
            score_left += SCORE_LEFT[a[i]]
        if a[i] in SCORE_RIGHT:
            score_right += SCORE_RIGHT[a[i]]
    return 'Left side wins!' if score_left > score_right else 'Right side wins!' if score_left < score_right else 'Let\'s fight again!'

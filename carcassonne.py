import random

class tile:
    def __init__(self, side_a, side_b, side_c, side_d, sheild, monastary):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_d = side_d
        self.sheild = sheild
        self.monastary = monastary

t1 = tile('te', 'fx', 'fx', 'fx', False, False)
t2 = tile('te', 'te', 'fx', 'fx', False, False)
t3 = tile('te', 'fx', 'te', 'fx', False, False)
t4 = tile('tn', 'fx', 'tn', 'fx', False, False)
t5 = tile('tn', 'fx', 'tn', 'fx', True, False)
t6 = tile('tn', 'tn', 'fx', 'fx', False, False)
t7 = tile('tn', 'tn', 'fx', 'fx', True, False)
t8 = tile('tn', 'rn', 'rn', 'tn', False, False)
t9 = tile('tn', 'rn', 'rn', 'tn', True, False)
t10 = tile('tn', 'tn', 're', 'tn', False, False)
t11 = tile('tn', 'tn', 're', 'tn', True, False)
t12 = tile('tn', 'tn', 'fx', 'tn', True, False)
t13 = tile('tn', 'tn', 'fx', 'tn', False, False)
t14 = tile('fx', 're', 're', 're', False, False)
t15 = tile('te', 're', 're', 're', False, False)
t16 = tile('tn', 'tn', 'tn', 'tn', True, False)
t17 = tile('te', 'fx', 'rn', 'rn', False, False)
t18 = tile('te', 'rn', 'fx', 'rn', False, False)
t19 = tile('te', 'rn', 'rn', 'fx', False, False)
t20 = tile('re', 're', 're', 're', False, False)
t21 = tile('fx', 'fx', 're', 'fx', False, True)
t22 = tile('fx', 'fx', 'fx', 'fx', False, True)
t23 = tile('rn', 'fx', 'rn', 'fx', False, False)
t24 = tile('fx', 'fx', 'rn', 'rn', False, False)
starter_tile = t18
master_deck = [t1, t1, t1, t1, t1, t2, t2, t3, t3, t3, t4, t5, t5, t6, t6, t6, t7, t7, t8, t8, t8, t9, t9, t10, t11, t11, t12, t13, t13, t13, t14, t14, t14, t14, t15, t15, t15, t16, t17, t17, t17, t18, t18, t18, t19, t19, t19, t20, t21, t21, t22, t22, t22, t22, t23, t23, t23, t23, t23, t23, t23, t23, t24, t24, t24, t24, t24, t24, t24, t24, t24]
deck = master_deck.copy()

def draw_tile():
    tile = deck[random.randint(0,len(deck))]
    deck.remove(tile)
    return tile


def print_tile(tile):
    if tile.sheild == True:
        middle = 'Sx'
    elif tile.monastary == True:
        middle = 'Mx'
    else:
        middle = 'ox'

    print("+----------+")
    print('|    ' + tile.side_a + '    |')
    print('| ' + tile.side_d + ' ' + middle + ' ' + tile.side_b + ' |')
    print('|    ' + tile.side_c + '    |')
    print('+----------+')

test = draw_tile()
print_tile(test)

import random

class Tile:
    def __init__(self, side_a, side_b, side_c, side_d, sheild, monastary):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_d = side_d
        self.sheild = sheild
        self.monastary = monastary

t1 = Tile('te', 'fx', 'fx', 'fx', False, False)
t2 = Tile('te', 'te', 'fx', 'fx', False, False)
t3 = Tile('te', 'fx', 'te', 'fx', False, False)
t4 = Tile('tn', 'fx', 'tn', 'fx', False, False)
t5 = Tile('tn', 'fx', 'tn', 'fx', True, False)
t6 = Tile('tn', 'tn', 'fx', 'fx', False, False)
t7 = Tile('tn', 'tn', 'fx', 'fx', True, False)
t8 = Tile('tn', 'rn', 'rn', 'tn', False, False)
t9 = Tile('tn', 'rn', 'rn', 'tn', True, False)
t10 = Tile('tn', 'tn', 're', 'tn', False, False)
t11 = Tile('tn', 'tn', 're', 'tn', True, False)
t12 = Tile('tn', 'tn', 'fx', 'tn', True, False)
t13 = Tile('tn', 'tn', 'fx', 'tn', False, False)
t14 = Tile('fx', 're', 're', 're', False, False)
t15 = Tile('te', 're', 're', 're', False, False)
t16 = Tile('tn', 'tn', 'tn', 'tn', True, False)
t17 = Tile('te', 'fx', 'rn', 'rn', False, False)
t18 = Tile('te', 'rn', 'fx', 'rn', False, False)
t19 = Tile('te', 'rn', 'rn', 'fx', False, False)
t20 = Tile('re', 're', 're', 're', False, False)
t21 = Tile('fx', 'fx', 're', 'fx', False, True)
t22 = Tile('fx', 'fx', 'fx', 'fx', False, True)
t23 = Tile('rn', 'fx', 'rn', 'fx', False, False)
t24 = Tile('fx', 'fx', 'rn', 'rn', False, False)
starter_tile = t18
master_deck = [t1, t1, t1, t1, t1, t2, t2, t3, t3, t3, t4, t5, t5, t6, t6, t6, t7, t7, t8, t8, t8, t9, t9, t10, t11, t11, t12, t13, t13, t13, t14, t14, t14, t14, t15, t15, t15, t16, t17, t17, t17, t18, t18, t18, t19, t19, t19, t20, t21, t21, t22, t22, t22, t22, t23, t23, t23, t23, t23, t23, t23, t23, t24, t24, t24, t24, t24, t24, t24, t24, t24] #starter tile not included
deck = master_deck.copy()

def draw_tile():
    tile = deck[random.randint(0,len(deck))]
    deck.remove(tile)
    return tile

def print_tile(tile):
    if tile.sheild:
        middle = 'Sx'
    elif tile.monastary:
        middle = 'Mx'
    else:
        middle = 'ox'

    print("+----------+")
    print('|    ' + tile.side_a + '    |')
    print('| ' + tile.side_d + ' ' + middle + ' ' + tile.side_b + ' |')
    print('|    ' + tile.side_c + '    |')
    print('+----------+')

# test = draw_tile()
# print_tile(test)


class Board:
    def __init__(self):
        x_list = []
        for x in range(143):
            y_list = []
            for y in range(143):
                y_list.append(None)
            x_list.append(y_list)
        list = x_list[71]
        list[71] = starter_tile
        self.rows = x_list

    def print_board(self):
        for x in self.rows:
            for y in x:
                if y != None:
                    print_tile(y)

    def tile_at(self, x, y):
        pass

    def place_tile(self, tile, x, y):
        pass

    def extent(self):
        pass

board = Board()
board.print_board()

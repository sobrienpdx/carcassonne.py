import random

class Tile:
    def __init__(self, side_a, side_b, side_c, side_d, sheild, monastary):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_d = side_d
        self.sheild = sheild
        self.monastary = monastary

    def tile_guts(self):
        if self.sheild:
            middle = 'Sx'
        elif self.monastary:
            middle = 'Mx'
        else:
            middle = 'ox'
        line1 = '|    ' + self.side_a + '    '
        line2 = '| ' + self.side_d + ' ' + middle + ' ' + self.side_b + ' '
        line3 = '|    ' + self.side_c + '    '
        return line1, line2, line3


    def print(self):
        line1, line2, line3 = self.tile_guts()
        print("+----------+")
        print(line1 + '|')
        print(line2 + '|')
        print(line3 + '|')
        print('+----------+')


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

# def print_tile(tile):
#     line1, line2, line3 = tile.tile_guts()
#     # if tile.sheild:
#     #     middle = 'Sx'
#     # elif tile.monastary:
#     #     middle = 'Mx'
#     # else:
#     #     middle = 'ox'
#
#     print("+----------+")
#     print(line1)
#     print('| ' + tile.side_d + ' ' + middle + ' ' + tile.side_b + ' |')
#     print('|    ' + tile.side_c + '    |')
#     print('+----------+')



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
        self.min_x = 71
        self.max_x = 71
        self.min_y = 71
        self.max_y = 71


    def print_board(self):
        for row in self.rows[self.min_y :self.max_y +1]:
            string0 = ''
            string1 = ''
            string2 = ''
            string3 = ''
            for tile in row[self.min_x :self.max_x +1]:
                middle = 'xx'
                string0 += '+----------'
                if tile != None:
                    line1, line2, line3 = tile.tile_guts()
                    string1 += line1
                    string2 += line2
                    string3 += line3
                    # string1 += '|    ' + tile.side_a + '    '
                    # string2 += '| ' + tile.side_d + ' ' + middle + ' ' + tile.side_b + ' '
                    # string3 += '|    ' + tile.side_c + '    '
                else:
                    string1 += '|          '
                    string2 += '|          '
                    string3 += '|          '
            string0 += '+'
            string1 += '|'
            string2 += '|'
            string3 += '|'
            print(string0)
            print(string1)
            print(string2)
            print(string3)
        print(string0)


    def tile_at(self, x, y):
        pass

    def place_tile(self, tile, x, y):
        self.rows[y][x] = tile
        if x > self.max_x:
            self.max_x = x
        elif x < self.min_x:
            self.min_x = x
        if y > self.max_y:
            self.max_y = y
        elif y < self.min_y:
            self.min_y = y


    def extent(self):
        return self.min_x, self.max_x, self.min_y, self.max_y


board = Board()
board.place_tile(t1, 72, 71)
board.place_tile(t8, 71, 72)
board.place_tile(t8, 73, 71)
board.print_board()

import cocos
from cocos.director import director
from cocos.layer import *
import pyglet
from pyglet.window import key
import cocos.collision_model as cm
import cocos.euclid as eu


class Player(cocos.sprite.Sprite):
    def __init__(self):
        img = pyglet.image.load("res/player.png")
        img_grid = pyglet.image.ImageGrid(img, 1, 3)

        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1, loop=True)
        super().__init__(anim)
        x0 = -128 + self.width
        y0 = 0
        self.position = [x0, y0]
        self.player_x = 3
        self.player_y = 3

    def move_right(self):
        x_old, y_old = self.position
        self.position = [x_old + 64, y_old]
        self.player_y += 1

    def move_left(self):
        x_old, y_old = self.position
        self.position = [x_old - 64, y_old]
        self.player_y -= 1

    def move_up(self):
        x_old, y_old = self.position
        self.position = [x_old, y_old + 64]
        self.player_x -= 1

    def move_down(self):
        x_old, y_old = self.position
        self.position = [x_old, y_old - 64]
        self.player_x += 1

class Box(cocos.sprite.Sprite):
    def __init__(self):
        img = pyglet.image.load("res/CrateDark_Red.png")
        super().__init__(img)
        x0 = -64 + self.width/2
        y0 = 64
        self.box_x = 2
        self.box_y = 4
        self.position = [x0, y0]

    def move_right(self):
        x_old, y_old = self.position
        self.position = [x_old + 64, y_old]
        box_n = map_arr[self.box_x][self.box_y]
        map_arr[self.box_x][self.box_y] = 0
        self.box_y += 1
        map_arr[self.box_x][self.box_y] = box_n

    def move_left(self):
        x_old, y_old = self.position
        self.position = [x_old - 64, y_old]
        box_n = map_arr[self.box_x][self.box_y]
        map_arr[self.box_x][self.box_y] = 0
        self.box_y -= 1
        map_arr[self.box_x][self.box_y] = box_n

    def move_up(self):
        x_old, y_old = self.position
        self.position = [x_old, y_old + 64]
        box_n = map_arr[self.box_x][self.box_y]
        map_arr[self.box_x][self.box_y] = 0
        self.box_x -= 1
        map_arr[self.box_x][self.box_y] = box_n

    def move_down(self):
        x_old, y_old = self.position
        self.position = [x_old, y_old - 64]
        box_n = map_arr[self.box_x][self.box_y]
        map_arr[self.box_x][self.box_y] = 0
        self.box_x += 1
        map_arr[self.box_x][self.box_y] = box_n


class Box2(Box):
    def __init__(self):
        super().__init__()
        spr = cocos.sprite.Sprite("res/Crate_Red.png")
        self.add(spr)
        x0 = -64*3 + self.width/2
        y0 = 64
        self.box_x = 2
        self.box_y = 2
        self.position = [x0, y0]


class Box3(Box):
    def __init__(self):
        super().__init__()
        spr = cocos.sprite.Sprite("res/Crate_Red.png")
        self.add(spr)
        x0 = -64 + self.width / 2
        y0 = 64
        self.box_x = 2
        self.box_y = 4
        self.position = [x0, y0]


class Box4(Box):
    def __init__(self):
        super().__init__()
        spr = cocos.sprite.Sprite("res/Crate_Red.png")
        self.add(spr)
        x0 = -64*3 + self.width / 2
        y0 = -64
        self.box_x = 4
        self.box_y = 2
        self.position = [x0, y0]


class Box5(Box):
    def __init__(self):
        super().__init__()
        spr = cocos.sprite.Sprite("res/Crate_Red.png")
        self.add(spr)
        x0 = -64 + self.width / 2
        y0 = -64
        self.box_x = 4
        self.box_y = 4
        self.position = [x0, y0]


class MainLayer(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        spr = cocos.sprite.Sprite("res/map.png")
        self.position = 320, 224
        self.add(spr)

        self.player_layer = Player()
        self.box2_layer = Box2()
        self.box3_layer = Box3()
        self.box4_layer = Box4()
        self.box5_layer = Box5()
        #
        self.add(self.player_layer, 1)
        self.add(self.box2_layer, 2)
        self.add(self.box3_layer, 2)
        self.add(self.box4_layer, 2)
        self.add(self.box5_layer, 2)

    def update(self, dt):
        px = self.player_layer.player_x
        py = self.player_layer.player_y

        #button right
        if keyboard[key.RIGHT] == 1:
            if map_arr[px][py + 1] in [2, 3, 4, 5]:
                #universal box
                box_n = 'box'+ str(map_arr[px][py + 1]) +'_layer'
                if map_arr[px][py + 2] == 0:
                    self.player_layer.move_right()
                    exec("self." + box_n +".move_right()")
            elif map_arr[px][py + 1] == 1:
                pass
            elif map_arr[px][py + 1] == 0:
                self.player_layer.move_right()

        #button left
        elif keyboard[key.LEFT] == 1:
            if map_arr[px][py - 1] in [2, 3, 4, 5]:
                box_n = 'box' + str(map_arr[px][py - 1]) + '_layer'
                if map_arr[px][py - 2] == 0:
                    self.player_layer.move_left()
                    exec("self." + box_n + ".move_left()")
            elif map_arr[px][py - 1] == 1:
                pass
            elif map_arr[px][py - 1] == 0:
                self.player_layer.move_left()

        # button up
        elif keyboard[key.UP] == 1:
            if map_arr[px - 1][py] in [2, 3, 4, 5]:
                box_n = 'box' + str(map_arr[px - 1][py]) + '_layer'
                if map_arr[px - 2][py] == 0:
                    self.player_layer.move_up()
                    exec("self." + box_n + ".move_up()")
            elif map_arr[px - 1][py] == 1:
                pass
            elif map_arr[px - 1][py] == 0:
                self.player_layer.move_up()

        #button down
        elif keyboard[key.DOWN] == 1:
            if map_arr[px + 1][py] in [2, 3, 4, 5]:
                box_n = 'box' + str(map_arr[px + 1][py]) + '_layer'
                if map_arr[px + 2][py] == 0:
                    self.player_layer.move_down()
                    exec("self." + box_n + ".move_down()")
            elif map_arr[px + 1][py] == 1:
                pass
            elif map_arr[px + 1][py] == 0:
                self.player_layer.move_down()



if __name__ == "__main__":
    director.init(width=640, height=448, caption="sokoban")

    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    map_arr = []
    for i in range(0, 7):
        new_line = []
        for j in range(0, 10):
            new_line += [0]
        map_arr += [new_line]

    for i in range(0, 10):
        map_arr[0][i] = 1
        map_arr[6][i] = 1

    for i in range(0, 7):
        map_arr[i][0] = 1
        map_arr[i][9] = 1

    map_arr[1][5] = 1
    map_arr[2][5] = 1
    map_arr[4][5] = 1
    map_arr[5][5] = 1

    #boxes
    map_arr[2][2] = 2
    map_arr[2][4] = 3
    map_arr[4][2] = 4
    map_arr[4][4] = 5


    canvas = cocos.scene.Scene()

    map_layer = MainLayer()
    map_layer.schedule_interval(map_layer.update, 1 / 12)

    canvas.add(map_layer, 0, "background map")

    director.run(canvas)

import pyxel
from helpers import Vec2

WIDTH = 64
HEIGHT = 32

EYE = Vec2(11, 14)
BUBBLE_R = 2

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Rainbow Trout")
        pyxel.load("resources.pyxres")
        pyxel.mouse(False)
        self.bubbles = []
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or \
           pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.bubbles.append(Vec2(pyxel.mouse_x, pyxel.mouse_y))

        for i, _ in enumerate(self.bubbles):
            self.bubbles[i].x += pyxel.rndi(-1, 1)
            self.bubbles[i].y -= 1

            if self.bubbles[i].x + BUBBLE_R < 0 or self.bubbles[i].y + BUBBLE_R < 0:
                del self.bubbles[i]

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(-1, 0, 0, 0, 0, 64, 32)

        color = None
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if x == pyxel.mouse_x and y == pyxel.mouse_y:
                    pyxel.pset(x, y, 0)
                    continue

                if x == EYE.x and y == EYE.y:
                    pyxel.pset(x, y, 7)
                    continue

                if pyxel.pget(x, y) == 7: # body
                    n = pyxel.noise(x / 10, y / 10, pyxel.frame_count / 45)
                    if n > 0.6:
                        color = 8 # red
                    elif n > 0.3:
                        color = 9 # orange
                    elif n > 0:
                        color = 10 # yellow
                    elif n > -0.3:
                        color = 3 # green
                    elif n > -0.6:
                        color = 5 # blue
                    else:
                        color = 2 # purple
                elif pyxel.pget(x, y) == 1: # outline
                    color = 1
                elif pyxel.pget(x, y) == 0: # background
                    color = 6

                pyxel.pset(x, y, color)

        for bubble in self.bubbles:
            pyxel.circb(bubble.x, bubble.y, BUBBLE_R, 0)

App()

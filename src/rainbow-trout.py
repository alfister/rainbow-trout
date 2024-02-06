import pyxel

class App:
    def __init__(self):
        pyxel.init(64, 32, title="Rainbow Trout")
        pyxel.load("resources.pyxres")
        pyxel.mouse(False)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or \
           pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(-1, 0, 0, 0, 0, 64, 32)
        color = None
        for y in range(32):
            for x in range(64):
                if x == pyxel.mouse_x and y == pyxel.mouse_y:
                    pyxel.pset(x, y, 0)
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
                    pyxel.pset(x, y, color)
                elif pyxel.pget(x, y) == 1: # outline
                    pyxel.pset(x, y, 1)
                elif pyxel.pget(x, y) == 0: # background
                    pyxel.pset(x, y, 6)

        pyxel.pset(11, 14, 7) # eye

App()

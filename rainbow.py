import pyxel

class App:
    def __init__(self):
        pyxel.init(128, 64, title="Rainbow Trout")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0) # clear screen
        color = None
        for y in range(64):
            for x in range(128):
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

App()

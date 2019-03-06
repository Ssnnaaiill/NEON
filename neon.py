import math, random, pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="N E O N")
        pyxel.mouse(True)
        self.r, self.r2 = random.uniform(1, 5), random.uniform(20, 25)
        self.x, self.y = random.uniform(self.r2, SCREEN_WIDTH - self.r2), random.uniform(self.r2, SCREEN_HEIGHT - self.r2)
        self.color = random.randrange(8, 13, 2)
        self.SCORE, self.FLAG, self.LIFE, self.LEVEL = 0, 0, 100, 1
        self.TIME = self.LEVEL * 50
        pyxel.run(self.update, self.draw)

    def title_circ(self, x, y):
        for i in range(3): pyxel.circ(x + i * 15, y, 5, (i + 4) * 2)
        pyxel.text(62, 62, "z", 7)
        pyxel.text(77, 62, "x", 7)
        pyxel.text(92, 62, "c", 7)

    def reset(self):
        self.r, self.r2 = random.uniform(1, 5), random.uniform(20, 25)
        self.x, self.y = random.uniform(self.r2, SCREEN_WIDTH - self.r2), random.uniform(self.r2, SCREEN_HEIGHT - self.r2)
        self.color = random.randrange(8, 13, 2)
    
    def calc(self):
        if(abs(self.r2 - self.r) < 2): self.SCORE += 20
        else: self.SCORE += 10
    def loselife(self):
        self.LIFE -= 5

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q): pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.FLAG == 0: self.FLAG = 1

        if pyxel.btnp(pyxel.KEY_Z):
            if self.color == 8: self.calc()
            else: self.loselife()
        if pyxel.btnp(pyxel.KEY_X):
            if self.color == 10: self.calc()
            else: self.loselife()
        if pyxel.btnp(pyxel.KEY_C):
            if self.color == 12: self.calc()
            else: self.loselife()
        if self.LIFE <= 0: self.FLAG = 2

    def draw(self):
        pyxel.cls(0)
        if (self.FLAG == 0):
            pyxel.text(64, 45, "N E O N", pyxel.frame_count % 16)
            self.title_circ(63, 64)
            if(pyxel.frame_count % 60 < 30):
                pyxel.text(34, 80, "press spacebar to start", 5)
        elif (self.FLAG == 1):
            pyxel.circ(self.x, self.y, self.r, self.color)
            pyxel.circb(self.x, self.y, self.r2, self.color)
            pyxel.text(10, 10, "score " + str(self.SCORE), 7)
            pyxel.text(10, 20, "life  " + str(self.LIFE), 7)
            if (self.r < self.r2): self.r += 1
            else: self.reset()
        else:
            pyxel.text(64, 45, "GAME OVER", pyxel.frame_count % 16)
App()
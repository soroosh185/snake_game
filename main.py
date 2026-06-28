import pygame
import random
from time import sleep

pygame.init()

screen = pygame.display.set_mode(size=(800, 600))
pygame.display.set_caption("SNAKE")
pygame.display.update()

Red = (255, 0, 0)


class snakes():
    type_move = None
    box = []
    screen = None

    def __init__(self, screen, start_move="R"):
        self.type_move = start_move
        self.box = {1: {"type": "R", "location": (400, 300)}, "num": 1, "food": (40, 20)}
        self.screen = screen
        
    def move(self):
        if self.type_move == "R":
            self.go_right()
        elif self.type_move == "L":
            self.go_left()
        elif self.type_move == "U":
            self.go_up()
        elif self.type_move == "D":
            self.go_down()


    def go_left(self):
        self.type_move = "L"
        box_back = None
        for i in range(1, self.box["num"] + 1):
            if box_back:
                ii = self.box[i]
                self.box[i] = box_back
                box_back = ii
            else:
                box_back = self.box[i]
                ll = self.box[i]["location"][0] - 20
                ff = self.box[i]["location"][1]
                if (ll, ff) == self.box["food"]:
                    self.eat()
                self.box[i] = {"type": "L", "location": (ll, ff)}

    def go_right(self):
        self.type_move = "R"
        box_back = None
        for i in range(1, self.box["num"] + 1):
            if box_back:
                ii = self.box[i]
                self.box[i] = box_back
                box_back = ii
            else:
                box_back = self.box[i]
                ll = self.box[i]["location"][0] + 20
                ff = self.box[i]["location"][1]
                if (ll, ff) == self.box["food"]:
                    self.eat()
                self.box[i] = {"type": "R", "location": (ll, ff)}

    def go_up(self):
        self.type_move = "U"
        box_back = None
        for i in range(1, self.box["num"] + 1):
            if box_back:
                ii = self.box[i]
                self.box[i] = box_back
                box_back = ii
            else:
                box_back = self.box[i]
                ll = self.box[i]["location"][0]
                ff = self.box[i]["location"][1] - 20
                if (ll, ff) == self.box["food"]:
                    self.eat()
                self.box[i] = {"type": "U", "location": (ll, ff)}

    def go_down(self):
        self.type_move = "D"
        box_back = None
        for i in range(1, self.box["num"] + 1):
            if box_back:
                ii = self.box[i]
                self.box[i] = box_back
                box_back = ii
            else:
                box_back = self.box[i]
                ll = self.box[i]["location"][0]
                ff = self.box[i]["location"][1] + 20
                if (ll, ff) == self.box["food"]:
                    self.eat()
                self.box[i] = {"type": "D", "location": (ll, ff)}



    def eat(self):
        xx = self.box[self.box["num"]]
        self.box["num"] += 1
        if xx["type"] == "R":
            ll = xx["location"][0] - 20
            ff = xx["location"][1]
        if xx["type"] == "L":
            ll = xx["location"][0] + 20
            ff = xx["location"][1]
        if xx["type"] == "U":
            ll = xx["location"][0]
            ff = xx["location"][1] + 20
        if xx["type"] == "D":
            ll = xx["location"][0]
            ff = xx["location"][1] - 20

        self.box[self.box["num"]] = {"type": xx["type"], "location": (ll, ff)}
        self.draw()
        self.creat_food()
        self.draw()


    def creat_food(self):
        while True:
            xx = random.randrange(0, 800, 20)
            yy = random.randrange(0, 600, 20)
            yeky = False
            for i in range(1, self.box["num"] + 1):
                if (xx, yy) == self.box[i]["location"]:
                    yeky = True
            if not yeky:
                self.box["food"] = (xx, yy)
                break
                
    
    def draw(self):
        for i in range(1, self.box["num"] + 1):
            x, y = self.box[i]["location"]
            g = max(50, 255 - (i * 4))
            color = (0, g, 0)
            if i == 1:
                pygame.draw.rect(self.screen, (0, 200, 0), (x, y, 20, 20), border_radius=10)
                pygame.draw.circle(self.screen, (255,255,255), (x+5, y+5), 4)
                pygame.draw.circle(self.screen, (255,255,255), (x+15, y+5), 4)
                pygame.draw.circle(self.screen, (0,0,0), (x+6, y+5), 2)
                pygame.draw.circle(self.screen, (0,0,0), (x+16, y+5), 2)
            else:
                pygame.draw.rect(self.screen, color, (x, y, 20, 20), border_radius=6)
        

        fx, fy = self.box["food"]
        pygame.draw.circle(self.screen, (255, 50, 50), (fx+10, fy+10), 8)
        pygame.draw.rect(self.screen, (0, 200, 0), (fx+10, fy-5, 4, 8))



def end_game():
    all_box = snake.box
    first = all_box[1]
    zg = 0
    for i in range(1, all_box["num"] + 1):
        if all_box[i]["location"][0] >= 800:
            return True
        if all_box[i]["location"][1] >= 600:
            return True
        if 0 >= all_box[i]["location"][0]:
            return True
        if 0 >= all_box[i]["location"][1]:
            return True

        if first["location"] == all_box[i]["location"]:
            zg += 1

    if zg >= 2:
        return True
    return False
    


def draw_grid():
    for x in range(0, 800, 20):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, 600))
    for y in range(0, 600, 20):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (800, y))

pygame.draw.rect(screen, Red, (400, 300, 20, 20))
snake = snakes(screen)

run = True

while run:
    screen.fill((0, 0, 0))
    draw_grid()
    
    events = pygame.event.get()

    moved = False
    
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.go_left()
                moved = True
            elif event.key == pygame.K_RIGHT:
                snake.go_right()
                moved = True
            elif event.key == pygame.K_UP:
                snake.go_up()
                moved = True
            elif event.key == pygame.K_DOWN:
                snake.go_down()
                moved = True
            else:
                snake.move()
                moved = True

    if not moved:
        snake.move()
        
    snake.draw()
    pygame.display.update()

    if end_game():
        run = False

    sleep(0.2)
            

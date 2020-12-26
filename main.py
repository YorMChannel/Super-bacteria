import pygame
import random
import time

pygame.init()

color_list = {"red": (255, 0, 0), "blue": (0, 0, 255), "green": (0, 255, 0), "yellow": (0, 0, 0)}

class Cell: 
    def __init__(self, color, x, y): 
        self.color = color
        self.x = x
        self.y = y
        self.cell = 0
        self.clicked = False

    def show(self): 
        if self.color == "yellow":
            self.cell = pygame.draw.circle(screen, self.get_color(), (self.x, self.y), 20, 2)
            return
        self.cell = pygame.draw.circle(screen, self.get_color(), (self.x, self.y), 20)

    def get_color(self):
        return color_list[self.color]

    def drag(self):
        if self.clicked:
            mouse = pygame.mouse.get_pos()
            if mouse[0] > 320 or mouse[1] > 310:
                self.x = pygame.mouse.get_pos()[0]
                self.y = pygame.mouse.get_pos()[1]


screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Bacteria")

cell_list = []
for i in range(1, 11):
    cell = Cell("red", random.randint(320, 1870), random.randint(310, 1030))
    cell_list.append(cell)
    cell = Cell("blue", random.randint(320, 1870), random.randint(310, 1030))
    cell_list.append(cell)
    cell = Cell("green", random.randint(320, 1870), random.randint(310, 1030))
    cell_list.append(cell)
color_count = {"red": 10, "blue": 10, "green": 10, "yellow": 0}

font = pygame.font.Font(None, 50)

running = True
while running: 
    pygame.time.Clock().tick(60)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            clicked_cell = 0
            if add_yellow.collidepoint(mouse): 
                cell = Cell("yellow", random.randint(300, 1870), random.randint(100, 1030))
                cell_list.append(cell)
                color_count["yellow"] += 1

            elif random_remove.collidepoint(mouse):
                remove_list = []
                for cell in cell_list:
                    if cell.color != "yellow":
                        remove_list.append(cell)
                random.shuffle(remove_list)
                for i in range(0, 15): 
                    if len(remove_list) >= i+1:
                        del cell_list[cell_list.index(remove_list[i])]
                        color_count[remove_list[i].color] -= 1
            
            elif make_double.collidepoint(mouse):
                copy_cell_list = []
                for cell in cell_list:
                    copy_cell_list.append(cell)

                for cell in copy_cell_list:
                    new_cell = Cell(cell.color, random.randint(320, 1870), random.randint(310, 1030))
                    cell_list.append(new_cell)
                    color_count[new_cell.color] += 1

            else:
                for cell in cell_list:
                    if cell.cell.collidepoint(mouse):
                        if clicked_cell != 0:
                            clicked_cell.clicked = False
                        cell.clicked = True
                        clicked_cell = cell
                if event.button == 3:
                    if clicked_cell != 0:
                        del cell_list[cell_list.index(clicked_cell)]
                        color_count[clicked_cell.color] -= 1
                        clicked_cell = 0

        elif event.type == pygame.MOUSEBUTTONUP:
            if clicked_cell != 0:
                clicked_cell.clicked = False
            
    
    screen.fill((255, 212, 0))

    pygame.draw.rect(screen, (128, 128, 128), [0, 0, 300, 290])

    pygame.draw.circle(screen, (255, 0, 0), (30, 30), 20)
    pygame.draw.circle(screen, (0, 0, 255), (30, 80), 20)
    pygame.draw.circle(screen, (0, 255, 0), (170, 30), 20)
    pygame.draw.circle(screen, (255, 212, 0), (170, 80), 20)

    screen.blit(font.render(": {}".format(color_count.get("red")), True, (255, 255, 255)), (60, 15))
    screen.blit(font.render(": {}".format(color_count.get("blue")), True, (255, 255, 255)), (60, 65))
    screen.blit(font.render(": {}".format(color_count.get("green")), True, (255, 255, 255)), (200, 15))
    screen.blit(font.render(": {}".format(color_count.get("yellow")), True, (255, 255, 255)), (200, 65))

    add_yellow = pygame.draw.rect(screen, (0, 0, 0), [10, 110, 280, 50])
    screen.blit(font.render("ADD YELLOW", True, (255, 255, 255)), (33, 120))

    random_remove = pygame.draw.rect(screen, (0, 0, 0), [10, 170, 280, 50])
    screen.blit(font.render("RD REMOVE", True, (255, 255, 255)), (42, 180))

    make_double = pygame.draw.rect(screen, (0, 0, 0), [10, 230, 280, 50])
    screen.blit(font.render("DOUBLE", True, (255, 255, 255)), (75, 240))
    
    for cell in cell_list:
        cell.show()
        cell.drag()

    pygame.display.update()

pygame.quit()
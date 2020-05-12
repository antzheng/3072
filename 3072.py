"3072 - Anthony Zheng"

import pygame
import random
from pygame.locals import *

class Block:
    def __init__(self, position, num = 3, color = (160,82,45)):
        self.num = num
        self.position = position
        self.color = color

    def merge(self, other):
        self.num += other.num

    def __repr__(self):
        return "I'm a block at {} with value {}.".format(self.position, self.num)


def main():

    pygame.init()
    screenSize = 750
    clock = pygame.time.Clock()
    fps = 60

    backgroundColor = (255,218,185)
    tileColor = (255,248,220)
    blockColor = (160,82,45)
    textColor = (255,250,205)
    spawnColor = (119,136,153)
    mergeColor = (244,164,96)

    screen = pygame.display.set_mode((screenSize, screenSize))

    screen.fill(backgroundColor)

    for row in range(22, 570, 182):
        for col in range(22, 570, 182):
            screen.fill(tileColor, (row, col, 160, 160))

    available = [(22,22),
                (22, 204),
                (22, 386),
                (22, 568),
                (204, 22),
                (204, 204),
                (204, 386),
                (204, 568),
                (386, 22),
                (386, 204),
                (386, 386),
                (386, 568),
                (568, 22),
                (568, 204),
                (568, 386),
                (568, 568)]

    lose = False

    gameDict = {}

    font = pygame.font.SysFont("Georgia", 100)

    smallfont = pygame.font.SysFont("Georgia", 25)

    (x, y) = random.choice(available)

    available.remove((x, y))
                
    spawn = Block((x, y, 160, 160), random.choice([3,3,3,3,6,6,6]))

    gameDict[(x, y)] = spawn

    screen.fill(spawnColor, spawn.position)

    text = font.render(str(spawn.num), True, textColor)
    
    textWidth = text.get_width()
    
    textHeight = text.get_height()
    
    screen.blit(text, (x + 80 - textWidth/2, y + 80 - textHeight/2))

    lastSpawn = (spawn.position[0], spawn.position[1])

    highScore = 0

    while True:
        ev = pygame.event.wait()
        
        if ev.type == pygame.QUIT:
            break

        elif lose:
            continue

        elif ev.type == pygame.KEYDOWN:

            if pygame.key.name(ev.dict['key']) == 'left':
                for col in range(204, 570, 182):
                    for row in range(22, 570, 182):
                        if (col, row) not in available and (col, row) in gameDict:
                            for current in range(col, 203, -182):
                                if (current - 182, row) not in available:
                                    if gameDict[(current - 182, row)].num == gameDict[(current, row)].num:
                                        gameDict[(current - 182, row)].merge(gameDict[(current, row)])
                                        gameDict[(current, row)] = None
                                        if gameDict[(current - 182, row)].color != blockColor:
                                            currentcolor = gameDict[(current - 182, row)].color
                                            newcolor = (currentcolor[0] - 7, currentcolor[1] - 4, currentcolor[2] - 1)
                                            gameDict[(current - 182, row)].color = newcolor
                                        else:
                                            gameDict[(current - 182, row)].color = mergeColor
                                        available.append((current, row))
                                        screen.fill(tileColor, (current, row, 160, 160))
                                else:
                                    gameDict[(current, row)].position = (current - 182, row, 160, 160)
                                    gameDict[(current - 182, row)] = gameDict[(current, row)]
                                    gameDict[(current, row)] = None
                                    available.append((current, row))
                                    available.remove((current - 182, row))
                                    screen.fill(tileColor, (current, row, 160, 160))


            elif pygame.key.name(ev.dict['key']) == 'right':
                for col in range(386, 21, -182):
                    for row in range(22, 570, 182):
                        if (col, row) not in available and (col, row) in gameDict:
                            for current in range(col, 387, 182):
                                if (current + 182, row) not in available:
                                    if gameDict[(current + 182, row)].num == gameDict[(current, row)].num:
                                        gameDict[(current + 182, row)].merge(gameDict[(current, row)])
                                        gameDict[(current, row)] = None
                                        if gameDict[(current + 182, row)].color != blockColor:
                                            currentcolor = gameDict[(current + 182, row)].color
                                            newcolor = (currentcolor[0] - 7, currentcolor[1] - 4, currentcolor[2] - 1)
                                            gameDict[(current + 182, row)].color = newcolor
                                        else:
                                            gameDict[(current + 182, row)].color = mergeColor
                                        available.append((current, row))
                                        screen.fill(tileColor, (current, row, 160, 160))
                                else:
                                    gameDict[(current, row)].position = (current + 182, row, 160, 160)
                                    gameDict[(current + 182, row)] = gameDict[(current, row)]
                                    gameDict[(current, row)] = None
                                    available.append((current, row))
                                    available.remove((current + 182, row))
                                    screen.fill(tileColor, (current, row, 160, 160))


            elif pygame.key.name(ev.dict['key']) == 'up':
                for row in range(204, 570, 182):
                    for col in range(22, 570, 182):
                        if (col, row) not in available and (col, row) in gameDict:
                            for current in range(row, 203, -182):
                                if (col, current - 182) not in available:
                                    if gameDict[(col, current - 182)].num == gameDict[(col, current)].num:
                                        gameDict[(col, current - 182)].merge(gameDict[(col, current)])
                                        gameDict[(col, current)] = None
                                        if gameDict[(col, current - 182)].color != blockColor:
                                            currentcolor = gameDict[(col, current - 182)].color
                                            newcolor = (currentcolor[0] - 7, currentcolor[1] - 4, currentcolor[2] - 1)
                                            gameDict[(col, current - 182)].color = newcolor
                                        else:
                                            gameDict[(col, current - 182)].color = mergeColor
                                        available.append((col, current))
                                        screen.fill(tileColor, (col, current, 160, 160))
                                else:
                                    gameDict[(col, current)].position = (col, current - 182, 160, 160)
                                    gameDict[(col, current - 182)] = gameDict[(col, current)]
                                    gameDict[(col, current)] = None
                                    available.append((col, current))
                                    available.remove((col, current - 182))
                                    screen.fill(tileColor, (col, current, 160, 160))


            elif pygame.key.name(ev.dict['key']) == 'down':
                for row in range(386, 21, -182):
                    for col in range(22, 570, 182):
                        if (col, row) not in available and (col, row) in gameDict:
                            for current in range(row, 387, 182):
                                if (col, current + 182) not in available:
                                    if gameDict[(col, current + 182)].num == gameDict[(col, current)].num:
                                        gameDict[(col, current + 182)].merge(gameDict[(col, current)])
                                        gameDict[(col, current)] = None
                                        if gameDict[(col, current + 182)].color != blockColor:
                                            currentcolor = gameDict[(col, current + 182)].color
                                            newcolor = (currentcolor[0] - 7, currentcolor[1] - 4, currentcolor[2] - 1)
                                            gameDict[(col, current + 182)].color = newcolor
                                        else:
                                            gameDict[(col, current + 182)].color = mergeColor
                                        available.append((col, current))
                                        screen.fill(tileColor, (col, current, 160, 160))
                                else:
                                    gameDict[(col, current)].position = (col, current + 182, 160, 160)
                                    gameDict[(col, current + 182)] = gameDict[(col, current)]
                                    gameDict[(col, current)] = None
                                    available.append((col, current))
                                    available.remove((col, current + 182))
                                    screen.fill(tileColor, (col, current, 160, 160))

            else:
                continue


            for (key, value) in gameDict.items():
                if value != None:
                    (x, y, height, width) = value.position
                    screen.fill(value.color, value.position)
                    text = font.render(str(value.num), True, textColor)
                    textWidth = text.get_width()
                    textHeight = text.get_height()
                    screen.blit(text, (x + 80 - textWidth/2, y + 80 - textHeight/2))
                    if value.num > highScore:
                        highScore = value.num

            
                                
                                

            if len(available) != 1:      # spawning new blocks

                if lastSpawn in available:
                    available.remove(lastSpawn)
                    (x, y) = random.choice(available)
                    available.append(lastSpawn)

                else:
                    (x, y) = random.choice(available)

                available.remove((x, y))
                
                spawn = Block((x, y, 160, 160), random.choice([3,3,3,3,6,6,6]))

                gameDict[(x, y)] = spawn

                screen.fill(spawnColor, spawn.position)

                text = font.render(str(spawn.num), True, textColor)
                textWidth = text.get_width()
                textHeight = text.get_height()
                screen.blit(text, (x + 80 - textWidth/2, y + 80 - textHeight/2))

                lastSpawn = (x, y)

            else:          # losing screen
                screen.fill(backgroundColor)
                text = font.render("You lost!", True, (0,0,0))
                score = smallfont.render("Your highest block was {}".format(highScore), True, (0,0,0))
                textWidth = text.get_width()
                textHeight = text.get_height()
                scoreWidth = score.get_width()
                scoreHeight = score.get_height()
                screen.blit(text, (375 - textWidth/2, 375 - textHeight/2 - scoreHeight))
                screen.blit(score, (375 - scoreWidth/2, 375 - scoreHeight/2 + textHeight/2))
                lose = True


        pygame.display.flip()

        clock.tick(fps) 

    pygame.quit()

main()



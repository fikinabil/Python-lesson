#Initialize import lib
import pygame
from pygame.locals import *
import random

pygame.init()

game_clock = pygame.time.Clock()
game_fps = 60

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 735

display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird - Development')

fontStyle = pygame.font.SysFont('arial black', 55)

black = (0, 0, 0)

baseScroll = 0
scrollSpeed = 4
birdFlying = False
gameOver = False
pipeGap = 150
pipeFrequency = 1450
lastPipe = pygame.time.get_ticks() - pipeFrequency
playerScore = 0
passPipe = False

background = pygame.image.load('images/background.png')
base = pygame.image.load('images/base.png')
button = pygame.image.load('images/restart.png')

def drawText(text, fontStyle, textColor, x_coordinate, y_coordinate):
    image = fontStyle.render(text, True, textColor)
    display_screen.blit(image, (x_coordinate, y_coordinate))

def resetGame():
    global playerScore
    pipeGroup.empty()
    bird.rect.x = 200
    bird.rect.y = int(SCREEN_HEIGHT / 2)
    playerScore = 0
    return playerScore

class FlappyBird(pygame.sprite.Sprite):
    def __init__(self, x_coordinate, y_coordinate):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = []
        self.index = 0
        self.counter = 0
        for i in range(1, 4):
            image = pygame.image.load(f'images/bird_{i}.png')
            self.image_list.append(image)
        self.image = self.image_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x_coordinate, y_coordinate]
        self.velocity = 0
        self.pressed = False

    def update(self):
        global birdFlying, gameOver
        if birdFlying:
            self.velocity += 0.5
            if self.velocity > 8.5:
                self.velocity = 8.5
            if self.rect.bottom < 576:
                self.rect.y += int(self.velocity)
        if not gameOver:
            if pygame.mouse.get_pressed()[0] == 1 and not self.pressed:
                self.pressed = True
                self.velocity = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.pressed = False
            self.counter += 1
            flapCooldown = 5
            if self.counter > flapCooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.image_list):
                    self.index = 0
            self.image = self.image_list[self.index]
            self.image = pygame.transform.rotate(self.image_list[self.index], self.velocity * -2)
        else:
            self.image = pygame.transform.rotate(self.image_list[self.index], -90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x_coordinate, y_coordinate, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/pipe.png')
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x_coordinate, y_coordinate - int(pipeGap / 2)]
        if position == -1:
            self.rect.topleft = [x_coordinate, y_coordinate + int(pipeGap / 2)]

    def update(self):
        global scrollSpeed
        self.rect.x -= scrollSpeed
        if self.rect.right < 0:
            self.kill()

class Button():
    def __init__(self, x_coordinate, y_coordinate, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_coordinate, y_coordinate)

    def draw(self):
        action = False
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        display_screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

birdGroup = pygame.sprite.Group()
pipeGroup = pygame.sprite.Group()

bird = FlappyBird(200, int(SCREEN_HEIGHT / 2))
birdGroup.add(bird)

restartButton = Button(150, 100, button)

game_run = True

while game_run:
    game_clock.tick(game_fps)
    display_screen.blit(background, (0, 0))
    birdGroup.draw(display_screen)
    birdGroup.update()
    pipeGroup.draw(display_screen)
    display_screen.blit(base, (baseScroll, 576))
    if len(pipeGroup) > 0:
        if birdGroup.sprites()[0].rect.left > pipeGroup.sprites()[0].rect.left \
            and birdGroup.sprites()[0].rect.left < pipeGroup.sprites()[0].rect.right \
            and not passPipe:
            passPipe = True
        if passPipe:
            if birdGroup.sprites()[0].rect.left > pipeGroup.sprites()[0].rect.right:
                playerScore += 1
                passPipe = False
    drawText(str(playerScore), fontStyle, black, int(SCREEN_WIDTH / 2), 15)
    if pygame.sprite.groupcollide(birdGroup, pipeGroup, False, False) or bird.rect.top < 0:
        gameOver = True
    if bird.rect.bottom >= 576:
        gameOver = True
        birdFlying = False
    if not gameOver and birdFlying:
        timeNow = pygame.time.get_ticks()
        if timeNow - lastPipe > pipeFrequency:
            pipeHeight = random.randint(-100, 100)
            bottomPipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) + pipeHeight, -1)
            topPipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) + pipeHeight, 1)
            pipeGroup.add(bottomPipe)
            pipeGroup.add(topPipe)
            lastPipe = timeNow
        baseScroll -= scrollSpeed
        if abs(baseScroll) > 70:
            baseScroll = 0
        pipeGroup.update()
    if gameOver:
        if restartButton.draw():
            gameOver = False
            playerScore = resetGame()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not birdFlying and not gameOver:
            birdFlying = True
    pygame.display.update()

pygame.quit()
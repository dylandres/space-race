import pygame
import random
import time

#SBUHacks 2019
#Dylan Andres
#Ryan Chung
#You Kwhan Kim
#Chris Magallona

#In honor of our fallen heroes at the Area 51 Raid
pygame.init()
winx, winy = 1000, 683
window = pygame.display.set_mode((winx, winy))
pygame.display.set_caption("Space Race")
background = pygame.image.load("spacebro.jpg")
screen = pygame.Surface((100, 100)).convert_alpha()
screen.fill((0, 0, 0, 0))
naruto = pygame.mixer.music.load('naruto.wav')
pygame.mixer.music.play(-1)

ayy = pygame.image.load("temp2.png")
astronaut = pygame.image.load("astronaut.png")
wolfie = pygame.image.load("wolfie.png")
thanos = pygame.image.load("thanos.png")
sonic = pygame.image.load("sonic.png")

clock = pygame.time.Clock()

# colors
darkRed = (255, 0, 0)
lightRed = (255, 127, 130)
darkOrange = (255, 154, 25)
lightOrange = (255, 199, 127)
darkYellow = (255, 242, 26)
lightYellow = (255, 249, 153)
darkGreen = (1, 158, 0)
lightGreen = (153, 255, 153)
darkBlue = (0, 0, 255)
lightBlue = (135, 206, 235)
purple = (130, 5, 250)

position = 1000
radius = 18
edge = 60
velocity = 3

f1 = False
f2 = False
f3 = False
f4 = False
f5 = False


def message(text, color, size, x, y):
    font = pygame.font.SysFont(None, size)
    screentext = font.render(text, True, color)
    window.blit(screentext, (x, y))


class Note:

    def __init__(self, clickable, color, position, radius, velocity):
        self.clickable = clickable
        self.color = color
        self.position = position
        self.radius = radius
        self.velocity = velocity

    def draw(self):

        if self.color == 'r':
            pygame.draw.circle(screen, purple, (self.position, 45), self.radius, 0)
            window.blit(ayy, (self.position - self.radius, 45 - self.radius))
        if self.color == 'o':
            pygame.draw.circle(screen, purple, (self.position, 120), self.radius, 0)
            window.blit(astronaut, (self.position - self.radius, 120 - self.radius))
        if self.color == 'y':
            pygame.draw.circle(screen, purple, (self.position, 195), self.radius, 0)
            window.blit(thanos, (self.position - self.radius, 195 - self.radius))
        if self.color == 'g':
            pygame.draw.circle(screen, purple, (self.position, 270), self.radius, 0)
            window.blit(wolfie, (self.position - self.radius, 270 - self.radius))
        if self.color == 'b':
            pygame.draw.circle(screen, purple, (self.position, 345), self.radius, 0)
            window.blit(sonic, (self.position - self.radius, 345 - self.radius))

    def move(self):
        self.position -= self.velocity


n1 = Note(False, 'r', position, radius, velocity)
n2 = Note(False, 'o', position, radius, velocity)
n3 = Note(False, 'y', position, radius, velocity)
n4 = Note(False, 'g', position, radius, velocity)
n5 = Note(False, 'b', position, radius, velocity)

running = True
while running:
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                n1.velocity += 1
            if event.key == pygame.K_p:
                n2.velocity += 1
            if event.key == pygame.K_z:
                n3.velocity += 1
            if event.key == pygame.K_m:
                n4.velocity += 1
            if event.key == pygame.K_SPACE:
                n5.velocity += 1

    pygame.draw.rect(window, darkRed, pygame.Rect(15, 15, edge, 60))
    pygame.draw.rect(window, darkOrange, pygame.Rect(15, 90, edge, 60))
    pygame.draw.rect(window, darkYellow, pygame.Rect(15, 165, edge, 60))
    pygame.draw.rect(window, darkGreen, pygame.Rect(15, 240, edge, 60))
    pygame.draw.rect(window, darkBlue, pygame.Rect(15, 315, edge, 60))

    message("Q", (0, 0, 0), 50, 30, 30)
    message("P", (0, 0, 0), 50, 35, 105)
    message("Z", (0, 0, 0), 50, 35, 180)
    message("M", (0, 0, 0), 50, 30, 255)
    message("SPACE", (0, 0, 0), 25, 17, 335)

    if n1.position - n1.radius < edge:
        pygame.draw.rect(window, lightRed, pygame.Rect(15, 15, 60, 60))
        f1 = True
    if n2.position - n2.radius < edge:
        pygame.draw.rect(window, lightOrange, pygame.Rect(15, 90, 60, 60))
        f2 = True
    if n3.position - n3.radius < edge:
        pygame.draw.rect(window, lightYellow, pygame.Rect(15, 165, 60, 60))
        f3 = True
    if n4.position - n4.radius < edge:
        pygame.draw.rect(window, lightGreen, pygame.Rect(15, 240, 60, 60))
        f4 = True
    if n5.position - n5.radius < edge:
        pygame.draw.rect(window, lightBlue, pygame.Rect(15, 315, 60, 60))
        f5 = True
    if f1 == True or f2 == True or f3 == True or f4 == True or f5 == True:
        message(("WINNER!"), (255, 20, 147), 100, winx / 4, winy / 2)

    n1.move()
    n1.draw()
    n2.move()
    n2.draw()
    n3.move()
    n3.draw()
    n4.move()
    n4.draw()
    n5.move()
    n5.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

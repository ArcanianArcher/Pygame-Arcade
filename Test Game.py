import pygame, os
from pygame.locals import *
from Arcade import arcade
from colours import *

def Game(arcade):

    arcade.setCaption(__file__)
    
    ball_x, ball_y = 290, 290
    ball = pygame.Surface((600,600), pygame.SRCALPHA, 32).convert_alpha()
    pygame.draw.circle(ball, gold, (10,10), 10)
    speed_x, speed_y = 3, 3

    player_x, player_y = 300, 550
    player = pygame.Surface((100, 25))
    player.fill(navy,(0,0,100,25))

    background = pygame.Surface((600,600))
    background.fill(green,(0,0,600,600))
    arcade.initBackground(background)

    last = pygame.time.get_ticks()
    cooldown = 10
    alive = True
    
    while alive:
        arcade.getEvents()
        now = pygame.time.get_ticks()
        if now - last >= cooldown:
            last = now

            pressed = arcade.getKey()
            if pressed[K_a] or pressed[K_LEFT]:
                player_x -= 5
            if pressed[K_d] or pressed[K_RIGHT]:
                player_x += 5

            
            arcade.drawBackground(background)
            arcade.draw((player, player_x, player_y),
                        (ball, ball_x, ball_y))

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    Game(arcade())

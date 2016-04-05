# Ross' Game (Group Assignment)
# March 21, 2016
# Ross Morgan

import sys, pygame
from pygame.locals import*
from Arcade import arcade
import random

def game(arcade):
    # Screen Specs
    size = width, height = 200,150
    arcade.setWindow(width,height)
    screen = arcade.get_screen()
    pygame.display.set_caption("Ross")
    #Colors
    r_red = (214,133,175)
    r_green = (133,214,172)
    r_blue = (26,102,255)
    # Set Letter Coordinates
    r_left_x, r_left_y = (20,40)
    r_points = 0
    # Font Variables
    r_pts_display = 0
    r_font = pygame.font.SysFont("monospace", 15)

    # Alphabet Array
    r = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in range(len(alphabet)):
        r.append(arcade.getImage(__file__, str(alphabet[letter]) + '.png').convert())

    def get_letters():
        return random.randint(0,25), random.randint(0,25)
    # Grab Initial Random Letters
    r_left, r_right = get_letters()

    # Reset Game after time limit
    def reset(r_left,r_right):
        if counter % 200 == 1:
            r_left, r_right = get_letters()
            r_left_x = 40
        return r_left, r_right

    # Draws pts on screen
    def r_text(r_points):
        r_pts_text = "pts:" + str(r_points)
        r_pts_display = r_font.render(r_pts_text, False, r_blue)
        screen.blit(r_pts_display, (0,0))

    r_counter = 0
    # Main Game Loop
    while True:
        r_counter += 1
        # What does this do?
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # Background colours
        screen.fill(r_red)
        pygame.draw.rect(screen,r_green,(100,0,100,150),0)

        # Finishes Round
        
        if r_counter % 200 == 1 and r_counter != 1:
            # Checks Answer
            # Above
            if r_left_y == 20 and r_left > r_right:# replace all of these if statements with a flag variable like( up=true, middle = true
                r_points+=1
            elif r_left_y == 20 and r_left < r_right:
                r_points-=1
              # Middle
            if r_left_y == 40 and r_left == r_right:
                r_points+1
            elif r_left_y == 40 and r_left != r_right:
                r_points-=1
            # Below
            if r_left_y == 60 and r_left < r_right:
                r_points+=1
            elif r_left_y == 60 and r_left > r_right:
                r_points -=1
            # Gets New Letters
            r_left, r_right = get_letters()
            r_left_y = 40
        #reset(left,right)

        # User Input
        keys=pygame.key.get_pressed()
        if keys[K_w]:
            r_left_y = 20
        elif keys[K_s]:
            r_left_y = 60
        if keys[K_ESCAPE]:
            arcade.returnToArcade()
        
        # Draws Letters (Left, Right)
        screen.blit(r[r_left], (r_left_x, r_left_y))
        screen.blit(r[r_right], (120, 40))
        r_text(r_points)

        # Update Screen
        pygame.time.Clock().tick(60)
        pygame.display.update()
        #end loop

if __name__ == '__main__':
    pygame.init()
    game(arcade())

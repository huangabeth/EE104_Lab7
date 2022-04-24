# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:54:08 2022

@author: chris.pham
"""

import pgzrun
import pygame
import pgzero
import random
from pgzero.builtins import Actor
from random import randint

#Declare constants
FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
SPACEITEMS = ["nyancat", "cat", "astrocat"] # Actors changed to spacecat themed

#Declare global variables
game_over = False
game_complete = False
current_level = 1

#Keep track of the spaceguys (cat and asteroids) on the screen
spaceguys = []
animations = []

#Draw the spaceguys, background, and messages on screen
def draw():
    global spaceguys, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0,0)) #add a background image to the game window
    screen.blit("earth", (-40,450)) #add Earth to the background to bottom part of screen
    screen.blit("moon", (100,100))  #add the moon to the background
    if game_over: # display losing message
        display_message("GAME OVER!", "Click the space bar to try again.")
    elif game_complete: # display winning message
        display_message("YOU WON!", "Well done. Click the space bar to play again.")
    else: # draw spaceguys
        for spaceguy in spaceguys:
            spaceguy.draw()

#Updates counts, booleans, and objects
def update():
    global spaceguys, game_complete, game_over, current_level
    if len(spaceguys) == 0:
        spaceguys = make_spaceguys(current_level)
    # Try again: restarts game when game_complete or game_over if user clicks space bar.
    if (game_complete or game_over) and keyboard.space:
        spaceguys = []
        current_level = 1
        game_complete = False
        game_over = False

#Makes spaceguys based on the number of extra spaceguys there should be on the screen
def make_spaceguys(number_of_extra_spaceguys):
    # creates list of spaceguys that should be on the screen, places them, and animates them.
    colors_to_create = get_colors_to_create(number_of_extra_spaceguys)
    new_spaceguys = create_spaceguys(colors_to_create)
    layout_spaceguys(new_spaceguys)
    animate_spaceguys(new_spaceguys)
    return new_spaceguys

#Creates a list of spaceguys with the asteroid being the first index.
def get_colors_to_create(number_of_extra_spaceguys):
    #return[]
    colors_to_create = ["asteroid"]
    for i in range(0, number_of_extra_spaceguys):
        random_color = random.choice(SPACEITEMS)
        colors_to_create.append(random_color)
    return colors_to_create

#Creats objects (Actors) for the list of space guys
def create_spaceguys(colors_to_create):
    #return[]
    new_spaceguys = []
    for color in colors_to_create:
        spaceguy = Actor(color + "-spaceguy")
        new_spaceguys.append(spaceguy)
    return new_spaceguys

#Assigns placement to spaceguys
def layout_spaceguys(spaceguys_to_layout):
    #pass
    number_of_gaps = len(spaceguys_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(spaceguys_to_layout)
    for index, spaceguy in enumerate(spaceguys_to_layout):
        new_x_pos = (index + 1) * gap_size
        spaceguy.x = new_x_pos

#Animates spaceguys by assigning its speed
def animate_spaceguys(spaceguys_to_animate):
    #pass
    for spaceguy in spaceguys_to_animate:
        # A need for speed:
        random_speed_adjustment = random.randint(0, 2)  # sets speed randomly to 0, 1, or 2
        duration = START_SPEED - current_level + random_speed_adjustment
        spaceguy.anchor = ("center", "bottom")
        animation = animate(spaceguy, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

#Flags boolean value game_over to = True
def handle_game_over():
    global game_over 
    game_over = True
    
#Function to handle user input whenever mouse is clicked.
def on_mouse_down(pos):
    global spaceguys, current_level
    for spaceguy in spaceguys:
        if spaceguy.collidepoint(pos): # if user clicks on any Actors,
            if "asteroid" in spaceguy.image: # and the Actor clicked is an asteroid
                asteroid_click()    # perform this function
            else:
                handle_game_over()  # otherwise game_over

#Function to handle when an asteroid is clicked
def asteroid_click():
    global current_level, spaceguys, animations, game_complete 
    stop_animations(animations) #stops animations
    if current_level == FINAL_LEVEL: #checks if the current level is the final level
        game_complete = True         #adjusts boolean value to flag that the game is complete
    else: #if the current level is not the final level
        current_level = current_level + 1 # increments level
        #resets list of actors and animations
        spaceguys = []
        animations = []

#Function to stop animations
def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()
        
#Formats messages
def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text,
                     fontsize=30,
                     center=(CENTER_X, CENTER_Y+30),
                     color=FONT_COLOR)


pgzrun.go()
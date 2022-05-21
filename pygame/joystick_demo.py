#!/usr/bin/env python3

import pygame

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
clock = pygame.time.Clock()

while True:
    pygame.event.pump() # internally process pygame event handlers
    neck_axis = joystick.get_axis(1)
    head_axis = joystick.get_axis(2)
    print(neck_axis, head_axis)
    clock.tick(20)

pygame.quit()

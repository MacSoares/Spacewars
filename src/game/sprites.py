#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
from cocos.sprite import Sprite
from cocos.actions import MoveTo
from configs import WIDTH, HEIGHT, DATA_DIR
from pyglet import image
import os


class SpaceShipSprite(Sprite):

    def __init__(self):
        image = 'sprites/spaceship/center.png'
        super(SpaceShipSprite, self).__init__(image)

        self.position = (WIDTH / 2, - self.image.height)
        self.scale = 0.35
        self.do(MoveTo((WIDTH / 2, 100), 2))

    def move_left(self):
        x = self.position[0] - 10
        y = self.position[1]

        self.position = (x, y)

        self.image = image.load('data/sprites/spaceship/left4.png')

    def move_rigth(self):
        x = self.position[0] + 10
        y = self.position[1]

        self.position = (x, y)

        self.image = image.load('data/sprites/spaceship/right4.png')

    def center_spaceship(self):
        self.image = image.load('data/sprites/spaceship/center.png')


class AeroliteSprite(Sprite):

    def __init__(self, width=WIDTH / 2, height=2 * HEIGHT):
        image = 'sprites/aerolite/aero1.png'
        super(AeroliteSprite, self).__init__(image)

        self.position = (width, height)
        self.scale = 0.15
        self.do(MoveTo((width, -self.image.height), 5.5))


class RohenianSprite(Sprite):

    def __init__(self):
        image = "sprites/rohenians/F5S1.png"
        super(RohenianSprite, self).__init__(image)

        self.position = (WIDTH, HEIGHT)
        self.scale = 0.50
        self.do(MoveTo((WIDTH / 2, 100), 5.5))

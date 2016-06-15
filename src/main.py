#!/usr/bin/python
# -*- coding:utf-8 -*-

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
import signal

from cocos.layer import MultiplexLayer
from cocos.director import director
from cocos.scene import Scene

from pyglet import resource, font

from layers.base_layers import BackgroundLayer
from layers.menu import MainMenu, Credits, OptionsMenu


def signal_handler(signal_received, frame):
    if signal_received is signal.SIGINT:
        # erase the ^C on Terminal
        print "\r  "
        exit(0)

if __name__ == "__main__":
    resource.path.append('data')
    resource.reindex()
    font.add_directory('data/fonts')

    signal.signal(signal.SIGINT, signal_handler)
    director.init(width=800, height=600, caption='SpaceWars')
    scene = Scene()
    scene.add(BackgroundLayer('backgrounds/space_background.png'), z=0)
    scene.add(MultiplexLayer(
        MainMenu(),
        Credits(),
        OptionsMenu(),
    ),
        z=1)
    director.run(scene)
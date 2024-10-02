#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        print("Setup Start")
        pygame.init()
        window = pygame.display.set_mode((600, 480))
        print("Setup Done")

        print("Loop Start")
        while True:
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Se o evento for do tipo pygame.QUIT
                    print("Quitting...")
                    pygame.quit()  # Close window
                    quit()  # End pygame

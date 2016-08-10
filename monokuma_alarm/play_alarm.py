# -*- coding: utf-8 -*-

import sys
import string
import pygame
from time import sleep

def play():
    try:
        while True:
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
    except KeyboardInterrupt:
        pygame.mixer.music.stop()

        print "What do you want to do?"
        print "STOP - Stop alarm"
        print "N (number) = Snooze N minutes"
        print "Any other keyzZzZz = Snooze 5 minutes"
        choice = raw_input()

        if choice.isdigit() and (int(choice) > 0):
            snooze(choice)
        elif choice == "STOP":
            return
        else:
            snooze(5)

def snooze(minutes):
    minutes = int(minutes)
    seconds = minutes * 60

    try:
        print "Snoozing " + str(minutes) + " minute(s)..."
        sleep(seconds)
        print "Snooze over! Wake up!"
        play()
    except KeyboardInterrupt:
        print "Alarm cancelled!"
        return

pygame.mixer.init()
pygame.mixer.music.load("morning1.mp3")
play()

# EOF

# Faca um programa que reproduza um arquivo em mp3.

import pygame

pygame.init()
pygame.mixer.music.load('musica tem q estar dentro da pasta raiz(exercicio)')
pygame.mixer.music.play()
pygame.event.wait()
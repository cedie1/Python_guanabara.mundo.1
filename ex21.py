#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#resolução


import pygame

pygame.init()
pygame.mixer.music.load("eu.MP3")
pygame.event.wait()
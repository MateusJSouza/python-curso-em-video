import pygame

pygame.init()

# Carregando arquivo MP3
pygame.mixer.music.load('ex021.mp3')

# Reproduzindo áudio
pygame.mixer.music.play()

input()

pygame.event.wait()
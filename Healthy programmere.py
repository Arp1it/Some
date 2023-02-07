import pygame
import time
from datetime import date

pygame.init()

ab = pygame.mixer.music.load("krish.wav")

init_water = time.time()
init_eye = time.time()
init_exer = time.time()

def mixerere(l):
    pygame.mixer.music.load(l)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

def musictopper(stopper, l):
    if n == "drank" or m == "exdone" or  k == "eydone":
        pygame.mixer.music.load(l)
        pygame.mixer.music.stop()

def saving(value):
    today = date.today()
    with open("healty.txt", "a") as d:
        d.write(f"{today} - {value}\n")

while True:
    a = time.time() - init_water
    b = time.time() - init_exer
    c = time.time() - init_eye
    # print(a, b, c)

    if a >= 1800.0:
        mixerere("krish.wav")
        n = input("enter drank: ")
        musictopper(n, "krish.wav")
        saving(n)
        init_water = time.time()

    if b >= 3000.0:
        mixerere("krish.wav")
        m = input("enter exdone: ")
        musictopper(m, "krish.wav")
        saving(m)
        init_exer = time.time()

    if c >= 900.0:
        mixerere("krish.wav")
        k = input("enter eydone: ")
        musictopper(k,"krish.wav")
        saving(k)
        init_eye = time.time()

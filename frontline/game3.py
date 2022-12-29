import pygame
from random import choice
from random import randint
import os
import time
import tkinter as tk
import sys
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGRAY = (58, 58, 58)
GRAY =(100, 100, 100)

def menu():
    Menu_window = tk.Tk()
    


    def btn1_cklick():
        gamestart()

    def btn2_cklick():
        HowPlay()
    
    def btn3_cklick():
        Menu_window.quit()


    btn1 = tk.Button(text='Играть', command=btn1_cklick)
    btn1.pack()
    
    btn2 = tk.Button(text='Как играть', command=btn2_cklick)
    btn2.pack()

    btn3 = tk.Button(text='Выход', command=btn3_cklick)
    btn3.pack()



    Menu_window.mainloop()
    

def HowPlay():
    HowPlay_window = tk.Tk()

    Podskazka = tk.Label(master=HowPlay_window,text="ляляляля",font=("Arial", 14))
    Podskazka.pack()

    HowPlay_window.mainloop()




class tank:
    def __init__(self, pos, move, range, bk, condition, png):
        self.png ='tank.png'


class arta:
    def __init__(self, range, pos, move, bk, condition):
        pass



class solider:
    def __init__(self, pos, range, move, bk, mins, condition, png):
    
        pass



def tank_place():
    pass
def arta_place():
    pass
def solider_place():
    pass




def gamestart():
    FPS = 60
    WIN_WIDTH = 1080
    WIN_HEIGHT = 720
    WHITE = (255, 255, 255)
    ORANGE = (255, 150, 100)
 
    clock = pygame.time.Clock()
    sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))
    
    tank1 = pygame.image.load('tank.png')
    tank2 = pygame.image.load('tank1.png')
    x1 = 1000
    y1 = 5
    x1_change = 0
    y1_change = 0


    while 1:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                sys.exit()

            if event1.type == pygame.KEYDOWN:
                if event1.key == pygame.K_LEFT:
                    x1_change = -100 #Указываем шаг изменения положения змейки
#в 10 пикселей.
                    y1_change = 0
                elif event1.key == pygame.K_RIGHT:
                    x1_change = 100
                    y1_change = 0
                elif event1.key == pygame.K_UP:
                    y1_change = -100
                    x1_change = 0
                elif event1.key == pygame.K_DOWN:
                    y1_change = 100
                    x1_change = 0
                x1 += x1_change #Записываем новое значение положения змейки по оси х.
                y1 += y1_change #Записываем новое значение положения змейки по оси y.
    # заливаем фон
        sc.fill(WHITE)
        #pygame.draw.rect(sc,DARKGRAY , 
          #       (0, 0, 540, 720))
        pygame.draw.rect(sc,BLUE , 
                 (1000, 320, 80, 80))
        pygame.draw.rect(sc,RED , 
                 (0, 320, 80, 80))
        sc.blit(tank1, [x1,y1])
        sc.blit(tank2, [0,5])
        

        pygame.display.update()

menu()
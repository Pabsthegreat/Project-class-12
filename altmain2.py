import pygame

pygame.init()

#creating the screen
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hunter Assassin")

Walk = [pygame.image.load('Hunter_Move/1.png'),pygame.image.load('Hunter_Move/2.png'),pygame.image.load('Hunter_Move/3.png'),
pygame.image.load('Hunter_Move/4.png'),pygame.image.load('Hunter_Move/5.png'),pygame.image.load('Hunter_Move/6.png'),
pygame.image.load('Hunter_Move/7.png'),pygame.image.load('Hunter_Move/8.png'), pygame.image.load("Hunter_Move/8a.png"),pygame.image.load('Hunter_Move/9.png'),pygame.image.load('Hunter_Move/10.png'),pygame.image.load('Hunter_Move/11.png'),
pygame.image.load('Hunter_Move/12.png'),pygame.image.load('Hunter_Move/13.png'),pygame.image.load('Hunter_Move/14.png'),
pygame.image.load('Hunter_Move/15.png')]

rest = pygame.image.load("Hunter_Move/8a.png")

icon = pygame.image.load("Hunter_Move/8a.png")
pygame.display.set_icon(icon)

bg =  pygame.image.load('bg.png')

#fuck this shit im sleeping , see you tomorrow ,im starting enemy tomorrow
import pygame

pygame.init()
pygame.display.set_caption('ToneMatrix')
window = pygame.display.set_mode((800, 800))
running = True
handled = False
c = pygame.time.Clock()

#Draw Once

#This command creates an image object. 
# variable name = image.load(IMG NAME)
R_P1 = pygame.image.load("Piece-Yellow2.png")
Off_Piece1= pygame.image.load("Piece-Off.png")

# This command creates a rectangle for collision detection.
RedPiece1 = R_P1.get_rect()
OffPiece1 = Off_Piece1.get_rect()

# window is the name of our display screen.
#.blit draws the image to the screen.
#.blit(IMAGE OBJECT, (x position, y position))
window.blit(Off_Piece1, (0,0))

#Always update the display after!
pygame.display.update()

#Main Loop
while running:
#mouse position and button clicking
    #This updates where the mouse position is.
    pos = pygame.mouse.get_pos()
    (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
#if statement
    c.tick(7)
    #this if statement uses the virtual rectangle we drew before, and asks if the mouse is inside it.
    if (OffPiece1.collidepoint(pos)& pressed1 == 1)& (handled == False):
        print("You have pressed #A1!")
        window.blit(R_P1, (0,0))
        handled = True
        pygame.display.update()
    elif (OffPiece1.collidepoint(pos)& pressed1 == 1)& (handled == True):
        print("You have turned off #A1!")
        window.blit(Off_Piece1, (0,0))
        handled = False
        pygame.display.update()
        
#Quit pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

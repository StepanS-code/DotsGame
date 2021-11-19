import pygame
pygame.init()

#Defining the screen width (pixels)
screen = pygame.display.set_mode([500,500])


#Writing a game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Feeling screen with color (RGB parameters)
    screen.fill((255, 255, 255))

    #Circle added (display, color, coordinates, size)
    pygame.draw.circle(screen, (220,20,60), (250, 250), 75)

    #Pusing concepts of the function
    pygame.display.flip()
pygame.quit()

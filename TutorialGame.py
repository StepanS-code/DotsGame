from types import CellType
import pygame
from pygame.constants import K_a, K_d, K_s, K_w
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        #super finction allows you to call superclass methods
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    
    def update(self, pressed_keys):
        #We can change coordinates both ways:
        if pressed_keys[K_w]:
            self.rect.top = self.rect.top -1
        # And like this: 
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_a]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(1, 0)
        #move_ip stands for move in place current rect

        # Keep player on the screen
        #After assinging a new coordinate we check if it' less than zero ect. If it is - we reassign the coordinate
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()




player1 = Player()

#Creating groups of Sprites
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)


#Creating a custom event wich takes place at a regular interval
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250) #miliseconds


running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running == False
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == ADDENEMY:
        # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    screen.fill((0,0,0))

    # Creating a new surface object 
    surf = pygame.Surface((50,50))
    surf.fill((220,20,60))
    rect = surf.get_rect()

    #Transfering our rectangle onto our screen: 
    for entity in all_sprites:
        screen.blit(entity.surf,player1.rect)
#    Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    # Now the player's able to move: 
    player1.update(pressed_keys)
    enemies.update()

    



    pygame.display.flip()
    


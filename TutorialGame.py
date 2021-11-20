from types import CellType
import pygame
from pygame.constants import K_a, K_d, K_s, K_w, K_q
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL
)
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        #super finction allows you to call superclass methods
        super(Cloud, self).__init__()
        self.surf = pygame.image.load('DotsGame\cloud-removebg-preview (1).jpg').convert()
        self.surf.set_colorkey((255, 255, 255),RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = 5

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        #super finction allows you to call superclass methods
        super(Player, self).__init__()
        self.surf = pygame.image.load('DotsGame\pixel2-removebg-preview (1).jpg').convert()
        self.surf.set_colorkey((255, 255, 255),RLEACCEL)
        self.rect = self.surf.get_rect()
    
    def update(self, pressed_keys):
        #We can change coordinates both ways:
        if pressed_keys[K_w]:
            self.rect.top = self.rect.top -5
        # And like this: 
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)
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
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()




player1 = Player()

#Creating groups of Sprites
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
clouds = pygame.sprite.Group()


#Creating a custom event wich takes place at a regular interval
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250) #miliseconds

ADDCLOUD = pygame.USEREVENT+ 2
pygame.time.set_timer(ADDCLOUD, 500)

# Ensuring the program tuns 30 frames per second
clock = pygame.time.Clock()


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
        elif event.type == ADDCLOUD:
            new_could = Cloud()
            clouds.add(new_could)
            all_sprites.add(new_could)


    screen.fill((0,191,255))

    
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)

    #  Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player1, enemies):
        player1.kill()
        running = False
    # Creating a new surface object dddddwa


    #Transfering our rectangle onto our screen: 

#    Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    # Now the player's able to move: 
    player1.update(pressed_keys)
    enemies.update()
    clouds.update()
    


    pygame.display.flip()

    #Ensuring the program runs in 30 fps
    clock.tick(30)

    

    


import pygame, random

class enemyProjectiles:
    def __init__(self, x):
        self.entity = pygame.image.load("enemy_bullet.png").convert_alpha()
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(x.rect.left+29, x.rect.bottom-20)
        self.entity = pygame.transform.scale(self.entity, (45,19))
        self.entity = pygame.transform.rotate(self.entity, -90)
        self.mask = pygame.mask.from_surface(self.entity)
        self.enemyshot = pygame.mixer.music.load('enemyshot.mp3')
        self.enemyshot = pygame.mixer.music.play(0)
    def checkBounds(self):
        if self.rect.top >= 1080:
            return 1

class enemyProjecticleList:
    def __init__(self):
        self.enemyProjectileArray = []
    def createBullet(self, enemy):
        x = random.randint(0,70000)
        if(x <= 100):
            self.enemyProjectileArray.append(enemyProjectiles(enemy))
    def moveAll(self):
        bullet = 0
        for bullet in self.enemyProjectileArray:
            bullet.rect = bullet.rect.move(0, 10)
            
            if bullet.checkBounds() == 1:
                self.enemyProjectileArray.remove(bullet)
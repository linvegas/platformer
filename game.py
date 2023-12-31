import pygame
import sys

from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.utils import  load_image, load_images

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Ninja")

        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'player': load_image('entities/player.png'),
            'grass': load_images('tiles/grass'),
            'stone': load_images('tiles/stone'),
            'decoration': load_images('tiles/decor'),
            'large_decor': load_images('tiles/large_decor'),
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, title_size=16)

    def run(self):
        while True:
            self.display.fill((14, 219, 248))

            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_h:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                        self.movement[1] = True
                    if event.key == pygame.K_UP or event.key == pygame.K_k:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_h:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                        self.movement[1] = False


            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()


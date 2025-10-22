import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        screen.fill("Black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = fps_clock.tick(60)/1000


if __name__ == "__main__":
    main()

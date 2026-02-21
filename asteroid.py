import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            direction = random.uniform(20, 50)
            position1 = pygame.Vector2(self.position.x, self.position.y).rotate(direction)
            position2 = pygame.Vector2(self.position.x, self.position.y).rotate(-direction)
            radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, radius)
            a2 = Asteroid(self.position.x, self.position.y, radius)
            a1.velocity = 1.2 * position1
            a2.velocity = 1.2 * position2

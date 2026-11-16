from turtle import position

from logger import log_event
import pygame
import random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self,x:float, y:float, radius:float) -> None:
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position[0], self.position[1], new_radius)
            a2 = Asteroid(self.position[0], self.position[1], new_radius)
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_state,log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def kill_i(self):
        if self.radius<= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            p1 = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
            p2 = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
            p1.velocity = self.velocity.rotate(angle)*1.2
            p2.velocity = self.velocity.rotate(-angle)*1.2
            self.kill()
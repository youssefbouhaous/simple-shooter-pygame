
from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame
class Shot(CircleShape):
    containers: tuple[pygame.sprite.Group, ...]
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity=pygame.Vector2(0,1)
    def draw(self, screen: pygame.Surface) -> None:
            pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_RADIUS)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
from Game.Game import Game
from Game.gameElements.sprite import sprite
import pygame

def main():
        sprite.init(1080, 720, "Best game ever")
        game = Game()
        
        while game.model.run:
                game.run()
                sprite.clock.tick(60)

        pygame.quit()


main()

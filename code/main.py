from settings import *
from sys import exit

#components
from game import Game
from score import Score
from preview import Preview

from random import choice


class Main:
    def __init__(self):
        #general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Pytris')

        #shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]
        
        
        #components\
        self.game = Game(self.get_next_shape)
        self.score = Score( )
        self.preview = Preview()
    
    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            #display
            self.display_surface.fill(GRAY)

            #components
            self.game.run()
            self.score.run()
            self.preview.run()
            
            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.run()
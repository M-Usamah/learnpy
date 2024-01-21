import pygame
x = pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_width = 900
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

exit_game = False
game_over = False
snake_x = 50
snake_y = 50
snake_size = 10



while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()   

pygame.quit()
quit()
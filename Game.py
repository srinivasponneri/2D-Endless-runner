import pygame
import random


pygame.init()


WIDTH, HEIGHT = 600, 300
SCREEN = pygame.display.set_ mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Endless Runner")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_COLOR = (180, 120, 60)


FPS = 60
GRAVITY = 0.8
GROUND_HEIGHT = HEIGHT - 40


player_width, player_height = 40, 50
player_x = 50
player_y = GROUND_HEIGHT - player_height
player_vel_y = 0
jumping = False


obstacle_width, obstacle_height = 30, 50
obstacle_vel_x = 6
obstacles = []
obstacle_timer = 0
OBSTACLE_INTERVAL = 1500  


score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()
running = True
last_obstacle_time = pygame.time.get_ticks()

def draw_ground():
    pygame.draw.rect(SCREEN, GROUND_COLOR, (0, GROUND_HEIGHT, WIDTH, 40))

def draw_player(x, y):
    pygame.draw.rect(SCREEN, (50, 120, 200), (x, y, player_width, player_height))

def draw_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(SCREEN, (200, 50, 50), obs)

while running:
    clock.tick(FPS)
    SCREEN.fill(WHITE)
    draw_ground()

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not jumping:
            player_vel_y = -14
            jumping = True

    
    player_y += player_vel_y
    player_vel_y += GRAVITY
    if player_y >= GROUND_HEIGHT - player_height:
        player_y = GROUND_HEIGHT - player_height
        player_vel_y = 0
        jumping = False

    draw_player(player_x, int(player_y))

    
    current_time = pygame.time.get_ticks()
    if current_time - last_obstacle_time > OBSTACLE_INTERVAL:
        obstacles.append(pygame.Rect(WIDTH, GROUND_HEIGHT - obstacle_height, obstacle_width, obstacle_height))
        last_obstacle_time = current_time

    
    for obs in obstacles:
        obs.x -= obstacle_vel_x
    obstacles = [obs for obs in obstacles if obs.x + obstacle_width > 0]
    draw_obstacles(obstacles)

    
    player_rect = pygame.Rect(player_x, int(player_y), player_width, player_height)
    for obs in obstacles:
        if player_rect.colliderect(obs):
            running = False  

    
    score += 1
    score_text = font.render(f"Score: {score // 10}", True, BLACK)
    SCREEN.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()

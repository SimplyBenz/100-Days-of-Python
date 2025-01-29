import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 700, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle dimensions
paddle_width, paddle_height = 10, 100

# Ball dimensions
ball_size = 20

# Game objects
player_paddle = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)

# Ball speed
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Paddle speed
paddle_speed = 10

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_s] and player_paddle.bottom < height:
        player_paddle.y += paddle_speed

    # Opponent AI (simple)
    if ball.y + ball_size > opponent_paddle.y + opponent_paddle.height // 2:
        opponent_paddle.y += paddle_speed
    if ball.y < opponent_paddle.y + opponent_paddle.height // 2:
        opponent_paddle.y -= paddle_speed

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1

    # Win condition (simplified)
    if ball.x < 0:
        print("Opponent wins!")
        running = False
    elif ball.x > width:
        print("Player wins!")
        running = False

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, player_paddle)
    pygame.draw.rect(screen, white, opponent_paddle)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (width // 2, 0), (width // 2, height))

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
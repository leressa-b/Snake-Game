import pygame
import random
pygame.init()

# Creating a static screen/window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Creating objects
food = pygame.Rect((random.randint(0, 780), random.randint(0, 580), 12, 12))

# Snake properties
segment_width = 20
segment_height = 20
initial_length = 15
snake_speed = 4
snake_direction = "right"  # Initial direction

# Create a list to hold the snake segments
snake_segments = []
for i in range(initial_length):
    segment = pygame.Rect((screen_width // 2 - (initial_length - i) * segment_width), screen_height // 2, segment_width, segment_height)
    snake_segments.append(segment)

# Timer event for continuous movement
MOVE_SNAKE = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE, 100)  # Timer interval in milliseconds

# Main loop to handle events
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():    # Checks each event in the returned list of events happening
        if event.type == pygame.QUIT:
            run = False
        elif event.type == MOVE_SNAKE:
            # Move the snake continuously
            if snake_direction == "up":
                snake_segments[0].y -= snake_speed
            elif snake_direction == "down":
                snake_segments[0].y += snake_speed
            elif snake_direction == "left":
                snake_segments[0].x -= snake_speed
            elif snake_direction == "right":
                snake_segments[0].x += snake_speed
        elif event.type == pygame.KEYDOWN:
            # Change snake direction when arrow keys are pressed
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"

    # Move the tail segments to follow the head
    for i in range(len(snake_segments) - 1, 0, -1):
        snake_segments[i].x = snake_segments[i-1].x
        snake_segments[i].y = snake_segments[i-1].y

    # Check for collision with food
    if snake_segments[0].colliderect(food):
        food.x = random.randint(0, 780)
        food.y = random.randint(0, 580)

    # Refresh the screen
    screen.fill((0, 0, 0))
    for segment in snake_segments:
        pygame.draw.rect(screen, (255, 0, 0), segment)
    pygame.draw.rect(screen, (0, 0, 255), food)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(30)  # Adjust the frame rate if needed

# Cleanup
pygame.quit()

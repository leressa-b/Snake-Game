#import and initialize
import pygame
import random
pygame.init()

#creating a static screen/window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")

#creating objects
food = pygame.Rect((random.randint(0,788), random.randint(0,588), 12, 12))

# Snake properties
segment_width = 20
segment_height = 20
initial_length = 15
snake_speed = 4

# Create a list to hold the snake segments
snake_segments = []
for i in range(initial_length):
    segment = pygame.Rect((screen_width // 2 - (initial_length - i) * segment_width), screen_height // 2, segment_width, segment_height)
    snake_segments.append(segment)


#main loop to handle events
clock = pygame.time.Clock()
run = True
while run:

    for event in pygame.event.get():    #checks each event in the returned list of events happening
        if event.type == pygame.QUIT:
            run = False

    #move the snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_segments[0].y -= snake_speed
    elif keys[pygame.K_s]:
        snake_segments[0].y += snake_speed
    elif keys[pygame.K_a]:
        snake_segments[0].x -= snake_speed
    elif keys[pygame.K_d]:
        snake_segments[0].x += snake_speed

    # Move the tail segments to follow the head
    for i in range(len(snake_segments) - 1, 0, -1):
        snake_segments[i].x = snake_segments[i-1].x
        snake_segments[i].y = snake_segments[i-1].y


    if snake_segments[1].colliderect(food):
        food.x = random.randint(0,788)
        food.y = random.randint(0,588)
    

   #to always refresh
    screen.fill((0,0,0))

    #drawing objects
    for segment in snake_segments:
        pygame.draw.rect(screen, (255, 0, 0), segment)
    pygame.draw.rect(screen, (0, 0, 255), food)

    #updating all changes
    pygame.display.update()

    #set the max frame rate
    clock.tick(30)

#cleanup
pygame.quit()

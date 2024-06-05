#import and initialize
import pygame
import random
pygame.init()

#creating a static screen/window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")

background_img = pygame.image.load('grass.png')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

#creating objects
food = pygame.Rect((random.randint(0,788), random.randint(0,588), 12, 12))

# Snake properties
segment_width = 20
segment_height = 20
initial_length = 4
snake_speed = 20

# Create a list to hold the snake segments
snake_segments = []
x = random.randint(0,780)
y = random.randint(0,580)
for i in range(initial_length):
    segment = pygame.Rect(x,y,segment_width,segment_height)
    snake_segments.append(segment)
    x -= 20

# #defining colours
# color1 = (0, 255, 0)  # Green
# color2 = (255, 255, 255)  # White
# colors = [color1, color2]

# for x in range(0,800,24):
#     column = pygame.Rect(x,0,12,600)
#     pygame.draw.rect(screen, (255,255,255), column)

# for y in range(12,600,24):
#     for x in range(0,800,24):
#         row = pygame.Rect(x,y,12,12)
#         pygame.draw.rect(screen, (0,0,0), row)
#         row = pygame.Rect(y,x,12,12)
#         pygame.draw.rect(screen, (255,255,255), row)

# for y in range(0,600,24):
#     for x in range(12,800,24):
#         row = pygame.Rect(x,y,12,12)
#         pygame.draw.rect(screen, (255,255,255), row)

score = 0
font = pygame.font.SysFont("None",25)

def show_score(score):
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, [10, 10])
    

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
    



    #Check for collision between the snake head and the food
    if snake_segments[1].colliderect(food):
        score += 1
        # Add new food
        food.x = random.randint(0, 788)
        food.y = random.randint(0, 588)
        # Add a new segment to the snake
        new_segment = pygame.Rect(snake_segments[-1].x, snake_segments[-1].y, segment_width, segment_height)
        snake_segments.append(new_segment)

    
    screen.blit(background_img, (0,0))

                
    #drawing objects
    for segment in snake_segments:
        pygame.draw.rect(screen, (105, 199, 222), segment)
        pygame.draw.rect(screen, (0,0,0), segment, 1)
    pygame.draw.rect(screen, (255, 0, 0), food)
    pygame.draw.rect(screen, (0,0,0), food, 1)

    show_score(score)

    #updating all changes
    pygame.display.update()

    #set the max frame rate
    clock.tick(10)

#cleanup
pygame.quit()

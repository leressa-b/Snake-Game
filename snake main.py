#import and initialize
import pygame
import time
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
food = pygame.Rect((random.randint(0,39) * 20, random.randint(0,29) * 20, 12, 12))

# Snake properties
segment_width = 20
segment_height = 20
initial_length = 4
snake_speed = 20

random_multiple1 = random.randint(0,20)
random_x = random_multiple1 * 20
random_multiple2 = random.randint(0,29)
random_y = random_multiple2 * 20

# Create a list to hold the snake segments
snake_segments = []
for i in range(initial_length):
    segment = pygame.Rect(random_x,random_y,segment_width,segment_height)
    snake_segments.append(segment)
    random_x -= 20


score = 0

def show_score(score):
    score_font = pygame.font.SysFont("None",25)
    score_text = score_font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, [10, 10])
    
def game_over():
    game_font1 = pygame.font.SysFont("None",50)
    game_font2 = pygame.font.SysFont("None",30)

    large_text = game_font1.render("GAME OVER", True, (255,0,0))
    small_text = game_font2.render("Your score is: " + str(score), True, (0,0,0))

    large_text_rect = large_text.get_rect()
    small_text_rect = small_text.get_rect()

    screen.blit(large_text, (screen_width//2 - large_text_rect.width//2, 250))
    screen.blit(small_text, (screen_width//2 - small_text_rect.width//2, 300))

    pygame.display.update()
    time.sleep(2)
    pygame.quit()


#main loop to handle events
clock = pygame.time.Clock()
run = True
direction = "right"
while run:

    for event in pygame.event.get():    #checks each event in the returned list of events happening
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_s and direction != 'up':
                direction = 'down'
            elif event.key == pygame.K_a and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_d and direction != 'left':
                direction = 'right'



    # Move the tail segments to follow the head
    for i in range(len(snake_segments) - 1, 0, -1):
        snake_segments[i].x = snake_segments[i-1].x
        snake_segments[i].y = snake_segments[i-1].y
        
    # Update head position based on direction
    if direction == 'up':
        snake_segments[0].y -= snake_speed
    elif direction == 'down':
        snake_segments[0].y += snake_speed
    elif direction == 'left':
        snake_segments[0].x -= snake_speed
    elif direction == 'right':
        snake_segments[0].x += snake_speed
    


    #Check for collision between the snake head and the food
    if snake_segments[0].colliderect(food):
        score += 1
        # Add new food
        food.x = random.randint(0,39) * 20
        food.y = random.randint(0,29) * 20
        # Add a new segment to the snake
        new_segment = pygame.Rect(snake_segments[-1].x, snake_segments[-1].y, segment_width, segment_height)
        snake_segments.append(new_segment)

    for i in range(2,len(snake_segments)):
        if snake_segments[0].colliderect(snake_segments[i]):
            game_over()
            
    
    if snake_segments[0].x < 0 or snake_segments[0].x > 780:
        game_over()
        
    if snake_segments[0].y < 0 or snake_segments[0].y > 580:
        game_over()
        

    
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

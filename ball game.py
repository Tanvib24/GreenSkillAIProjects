#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pygame')


# In[2]:


import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Animation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Ball properties
ball_radius = 20
ball_x = WIDTH // 2
ball_y = ball_radius
ball_velocity_y = 0

# Physics properties
gravity = 0.5
elasticity = 0.7

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Physics calculations
    ball_velocity_y += gravity
    ball_y += ball_velocity_y

    # Bounce on the ground
    if ball_y + ball_radius > HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_velocity_y = -ball_velocity_y * elasticity

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, BLUE, (ball_x, int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()


# In[4]:


import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Animation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Ball properties
ball_radius = 20
ball_x = WIDTH // 2
ball_y = ball_radius
ball_velocity_x = 3
ball_velocity_y = 0

# Physics properties
gravity = 0.5
elasticity = 0.7

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Physics calculations
    ball_velocity_y += gravity
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Bounce on the ground
    if ball_y + ball_radius > HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_velocity_y = -ball_velocity_y * elasticity

    # Bounce on the walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_velocity_x = -ball_velocity_x

    # Clear the screen
    screen.fill(WHITE)

    # Draw the floor
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 10, WIDTH, 10))

    # Draw the ball
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()


# In[5]:


import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Animation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Ball properties
ball_radius = 20
ball_x = WIDTH // 2
ball_y = ball_radius
ball_velocity_x = 3
ball_velocity_y = 0

# Physics properties
gravity = 0.5
elasticity = 0.7

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball_velocity_y = -15  # Apply an upward force to simulate a bounce

    # Physics calculations
    ball_velocity_y += gravity
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Bounce on the ground
    if ball_y + ball_radius > HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_velocity_y = -ball_velocity_y * elasticity

    # Bounce on the walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_velocity_x = -ball_velocity_x

    # Clear the screen
    screen.fill(WHITE)

    # Draw the floor
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 10, WIDTH, 10))

    # Draw the ball
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()


# In[6]:


import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Animation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Ball properties
ball_radius = 20
ball_x = WIDTH // 2
ball_y = ball_radius
ball_velocity_x = 3
ball_velocity_y = 0

# Physics properties
gravity = 0.5
elasticity = 0.7

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball_velocity_y = -15  # Apply an upward force to simulate a bounce

    # Physics calculations
    ball_velocity_y += gravity
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Bounce on the ground
    if ball_y + ball_radius > HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_velocity_y = -ball_velocity_y * elasticity

    # Bounce on the ceiling
    if ball_y - ball_radius < 0:
        ball_y = ball_radius
        ball_velocity_y = -ball_velocity_y * elasticity

    # Bounce on the walls
    if ball_x - ball_radius < 0:
        ball_x = ball_radius
        ball_velocity_x = -ball_velocity_x
    if ball_x + ball_radius > WIDTH:
        ball_x = WIDTH - ball_radius
        ball_velocity_x = -ball_velocity_x

    # Clear the screen
    screen.fill(WHITE)

    # Draw the walls
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, 10))  # Ceiling
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 10, WIDTH, 10))  # Floor
    pygame.draw.rect(screen, BLACK, (0, 0, 10, HEIGHT))  # Left wall
    pygame.draw.rect(screen, BLACK, (WIDTH - 10, 0, 10, HEIGHT))  # Right wall

    # Draw the ball
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()


# In[ ]:





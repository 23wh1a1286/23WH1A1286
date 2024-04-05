import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird AI")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird attributes
BIRD_WIDTH, BIRD_HEIGHT = 40, 30
BIRD_X = 50
bird_y = HEIGHT // 2 - BIRD_HEIGHT // 2
BIRD_VELOCITY = 5
GRAVITY = 0.25
JUMP_HEIGHT = -8

# Pipe attributes
PIPE_WIDTH = 80
PIPE_GAP = 150
PIPE_VELOCITY = 3
pipes = []

# Fonts
font = pygame.font.SysFont(None, 36)

# Game loop
def game_loop():
    global bird_y
    bird_y = HEIGHT // 2 - BIRD_HEIGHT // 2
    pipes.clear()
    score = 0
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Bird movement
        bird_y += BIRD_VELOCITY
        BIRD_VELOCITY += GRAVITY

        # Check for collisions
        if bird_y <= 0 or bird_y + BIRD_HEIGHT >= HEIGHT:
            return score
        for pipe in pipes:
            if bird_y < pipe["top_height"] or bird_y + BIRD_HEIGHT > pipe["bottom_height"]:
                if pipe["x"] <= BIRD_X + BIRD_WIDTH:
                    return score

        # Generate new pipes
        if len(pipes) == 0 or pipes[-1]["x"] < WIDTH - 200:
            top_pipe_height = random.randint(50, HEIGHT - 200)
            pipes.append({"x": WIDTH, "top_height": top_pipe_height, "bottom_height": top_pipe_height + PIPE_GAP})

        # Move pipes
        for pipe in pipes:
            pipe["x"] -= PIPE_VELOCITY

        # Remove pipes that go off-screen
        if pipes[0]["x"] + PIPE_WIDTH < 0:
            pipes.pop(0)
            score += 1

        # Draw everything
        WIN.fill(WHITE)
        pygame.draw.rect(WIN, BLACK, (BIRD_X, bird_y, BIRD_WIDTH, BIRD_HEIGHT))
        for pipe in pipes:
            pygame.draw.rect(WIN, BLACK, (pipe["x"], 0, PIPE_WIDTH, pipe["top_height"]))
            pygame.draw.rect(WIN, BLACK, (pipe["x"], pipe["bottom_height"], PIPE_WIDTH, HEIGHT - pipe["bottom_height"]))
        score_text = font.render(f"Score: {score}", True, BLACK)
        WIN.blit(score_text, (10, 10))
        pygame.display.update()

    return score

# Main function
def main():
    while True:
        score = game_loop()
        print(f"Your score: {score}")
        restart = input("Press 'r' to restart, or any other key to quit: ")
        if restart.lower() != "r":
            break

if _name_ == "_main_":
    main()

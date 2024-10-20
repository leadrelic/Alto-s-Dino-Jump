import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alto's Dino Jump")

# Define colors for monochrome scheme
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up game variables
clock = pygame.time.Clock()
fps = 60
gravity = 0.5
game_speed = 5
score = 0
xp = 0
level = 1
xp_to_next_level = 3
jump_strength = 10
has_fireball = False
fireball_timer = 0
double_jump = False
extra_jump = 0
shield_active = False
magnet_active = False
double_xp_active = False
double_xp_timer = 0
glide_active = False
extra_life = False
fireballs = []
particles = []

# Define possible upgrades
UPGRADES = [
    {"name": "Jump Boost", "effect": "jump_boost"},
    {"name": "Fireball Ability", "effect": "fireball"},
    {"name": "Speed Boost", "effect": "speed_boost"},
    {"name": "Extra XP", "effect": "extra_xp"},
    {"name": "Double Jump", "effect": "double_jump"},
    {"name": "Shield", "effect": "shield"},
    {"name": "Magnet", "effect": "magnet"},
    {"name": "Double XP", "effect": "double_xp"},
    {"name": "Glide", "effect": "glide"},
    {"name": "Extra Life", "effect": "extra_life"}
]

# Load images for dinosaur
dino_image = pygame.image.load('dinoo.png').convert_alpha()
dino_image.set_colorkey(WHITE)
dino_image = pygame.transform.scale(dino_image, (50, 50))

# Function to create parallax scrolling background
def draw_background(ground_offset):
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 50, WIDTH, 50))
    pygame.draw.line(screen, WHITE, (0, HEIGHT - 50), (WIDTH, HEIGHT - 50), 2)
    for i in range(-ground_offset % 20, WIDTH, 20):
        pygame.draw.rect(screen, WHITE, (i, HEIGHT - 48, 4, 2))

def reset_game(keep_score=False):
    global player, player_y_speed, is_jumping, obstacle, xp_item, cloud, score, game_speed, xp, level, xp_to_next_level, fireballs, fireball_timer, shield_active, double_xp_timer, extra_jump
    player = pygame.Rect(100, HEIGHT - 150, 50, 50)
    player_y_speed = 0
    is_jumping = False
    game_speed = 5
    fireballs = []
    fireball_timer = 0
    double_xp_timer = 0
    extra_jump = 1 if double_jump else 0
    shield_active = False  # Reset shield status

    # Define obstacle properties (cactus-like)
    obstacle = pygame.Rect(WIDTH, HEIGHT - 100, 20, 50)
    xp_item = pygame.Rect(random.randint(WIDTH, WIDTH + 300), HEIGHT - 130, 20, 20)
    cloud = pygame.Rect(random.randint(WIDTH, WIDTH + 400), 100, 60, 30)

    if not keep_score:
        score = 0
        xp = 0
        level = 1
        xp_to_next_level = 3

def level_up():
    global level, xp_to_next_level, jump_strength, has_fireball, game_speed, fireball_timer
    level += 1
    xp = 0
    xp_to_next_level += 2

    # Randomly select three upgrades from the pool
    chosen_upgrades = random.sample(UPGRADES, 3)

    # Display the upgrade options
    font = pygame.font.Font(None, 36)
    text1 = font.render("Level Up! Choose an upgrade:", True, WHITE)
    option1 = font.render(f"1: {chosen_upgrades[0]['name']}", True, WHITE)
    option2 = font.render(f"2: {chosen_upgrades[1]['name']}", True, WHITE)
    option3 = font.render(f"3: {chosen_upgrades[2]['name']}", True, WHITE)

    screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 3))
    screen.blit(option1, (WIDTH // 2 - option1.get_width() // 2, HEIGHT // 2 - 40))
    screen.blit(option2, (WIDTH // 2 - option2.get_width() // 2, HEIGHT // 2))
    screen.blit(option3, (WIDTH // 2 - option3.get_width() // 2, HEIGHT // 2 + 40))
    pygame.display.flip()

    # Wait for the player to choose an upgrade
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    apply_upgrade(chosen_upgrades[0]["effect"])
                    waiting_for_input = False
                elif event.key == pygame.K_2:
                    apply_upgrade(chosen_upgrades[1]["effect"])
                    waiting_for_input = False
                elif event.key == pygame.K_3:
                    apply_upgrade(chosen_upgrades[2]["effect"])
                    waiting_for_input = False

def apply_upgrade(effect):
    global jump_strength, has_fireball, fireball_timer, game_speed, xp, double_jump, extra_jump, shield_active, magnet_active, double_xp_active, double_xp_timer, glide_active, extra_life
    if effect == "jump_boost":
        jump_strength += 2
    elif effect == "fireball":
        has_fireball = True
        fireball_timer = fps * 5
    elif effect == "speed_boost":
        game_speed += 1
    elif effect == "extra_xp":
        xp += 2
    elif effect == "double_jump":
        double_jump = True
        extra_jump = 1
    elif effect == "shield":
        shield_active = True
    elif effect == "magnet":
        magnet_active = True
    elif effect == "double_xp":
        double_xp_active = True
        double_xp_timer = fps * 5
    elif effect == "glide":
        glide_active = True
    elif effect == "extra_life":
        extra_life = True

def create_particles(position):
    """ Create a small burst of particles at the given position. """
    for _ in range(10):
        particles.append([list(position), [random.randint(-2, 2), random.randint(-2, 0)], random.randint(2, 4)])

def update_particles():
    """ Update and draw particles on the screen. """
    for particle in particles[:]:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        pygame.draw.circle(screen, WHITE, (int(particle[0][0]), int(particle[0][1])), int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

def game_over():
    global extra_life
    if extra_life:
        extra_life = False
        reset_game(keep_score=True)
        return

    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3))
    pygame.display.flip()
    pygame.time.wait(1000)

    font = pygame.font.Font(None, 36)
    text = font.render("Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting_for_input = False
                    reset_game()
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

# Start the game for the first time
reset_game()

# Game loop
running = True
ground_offset = 0

while running:
    screen.fill(BLACK)

    # Move the ground for parallax effect
    ground_offset += game_speed
    draw_background(ground_offset)

    # Draw the dinosaur, cactus, and cloud
    screen.blit(dino_image, (player.x, player.y))
    pygame.draw.rect(screen, WHITE, obstacle)
    pygame.draw.rect(screen, WHITE, cloud)

    # Draw XP items
    pygame.draw.circle(screen, WHITE, xp_item.center, 10)

    # Update particles and draw them
    update_particles()

    # Glide functionality: reduce fall speed when gliding
    if glide_active and player_y_speed > 0:
        player.y += player_y_speed * 0.8  # Slow down fall speed when gliding
    else:
        player.y += player_y_speed

    if player.y >= HEIGHT - 100:
        player.y = HEIGHT - 100
        player_y_speed = 0
        is_jumping = False
        extra_jump = 1 if double_jump else 0
    else:
        player_y_speed += gravity

    # Obstacle movement
    obstacle.x -= game_speed
    if obstacle.x < -50:
        obstacle.x = WIDTH
        score += 1

    # XP item movement
    xp_item.x -= game_speed
    if xp_item.x < -20:
        xp_item.x = random.randint(WIDTH, WIDTH + 300)

    if player.colliderect(xp_item):
        xp += 2 if double_xp_active else 1
        xp_item.x = random.randint(WIDTH, WIDTH + 300)
        if xp >= xp_to_next_level:
            level_up()

    # Draw shield outline if shield is active
    if shield_active:
        pygame.draw.circle(screen, WHITE, player.center, 30, 2)

    # Fireball timer bar
    if has_fireball:
        fireball_bar_width = 200
        fireball_fill = (fireball_timer / (fps * 5)) * fireball_bar_width
        pygame.draw.rect(screen, WHITE, (10, 120, fireball_bar_width, 20), 2)
        pygame.draw.rect(screen, WHITE, (10, 120, fireball_fill, 20))
        font = pygame.font.Font(None, 24)
        fireball_label = font.render("Fireball Timer", True, WHITE)
        screen.blit(fireball_label, (10, 100))

    # Check for collision with obstacles
    if player.colliderect(obstacle):
        if shield_active:
            # Deactivate shield and move obstacle out of screen range
            shield_active = False
            obstacle.x = WIDTH  # Move the obstacle out of the way to avoid immediate game-over
            score += 1  # Give the player a point for avoiding damage with the shield
        else:
            game_over()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not is_jumping:
                    player_y_speed = -jump_strength
                    is_jumping = True
                    create_particles(player.midbottom)
                elif double_jump and extra_jump > 0:
                    player_y_speed = -jump_strength
                    extra_jump -= 1
                    create_particles(player.midbottom)
            if event.key == pygame.K_f and has_fireball:
                fireball = pygame.Rect(player.x + 50, player.y + 10, 10, 5)
                fireballs.append(fireball)

    # Fireball movement
    for fireball in fireballs[:]:
        fireball.x += 10
        pygame.draw.ellipse(screen, WHITE, fireball)
        if fireball.x > WIDTH:
            fireballs.remove(fireball)
        if fireball.colliderect(obstacle):
            fireballs.remove(fireball)
            obstacle.x = WIDTH
            score += 1
            create_particles(fireball.topleft)

    # Update fireball timer
    if has_fireball:
        fireball_timer -= 1
        if fireball_timer <= 0:
            has_fireball = False

    # Draw UI elements
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    xp_fill = (xp / xp_to_next_level) * 200
    pygame.draw.rect(screen, WHITE, (10, 50, 200, 20), 2)
    pygame.draw.rect(screen, WHITE, (10, 50, xp_fill, 20))

    # Update the screen
    pygame.display.update()
    clock.tick(fps)

pygame.quit()

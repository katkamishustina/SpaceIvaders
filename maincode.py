import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Spaceship.png")
pygame.display.set_icon(icon)

# Background img
bg = pygame.image.load("bg.jpg")

# Player
playerImg = pygame.image.load("Spaceship.png")
playerX = 370  # Min: 25 Max:750
playerY = 550  # Min: 25 Max: 550
X_change = 0

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 28)
textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Enemy
enemyImg = pygame.image.load("ufo.png")
enemyX = random.randint(25, 750)  # Min: 25 Max:750
enemyY = 0  # Min: 25 Max: 550
enemyX_change = 0.05
enemyY_change = 0.05

# Bullet
bullet = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 0
bulletY_change = 0.5
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 8, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 15:
        return True
    else:
        return False


# Game loop
running = True

while running:

    # Background color
    screen.fill((0, 0, 0))
    screen.blit(bg, (-100, 15))
    screen.blit(bg, (555, 435))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if score_value < 6:
                    X_change = -0.25
                else:
                    X_change = -0.35

            if event.key == pygame.K_RIGHT:
                if score_value < 6:
                    X_change = 0.25
                else:
                    X_change = 0.35

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = 550
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                X_change = 0
            # if event.key == pygame.K_SPACE:

    playerX += X_change
    if playerX <= 25:
        playerX = 25
    elif playerX >= 750:
        playerX = 750

    enemyX += enemyX_change
    if enemyX <= 25:
        enemyX_change = 0.05
    elif enemyX >= 750:
        enemyX_change = -0.05
    if score_value >= 9:
        enemyImg = pygame.image.load("ufo2.png")
        enemyY_change = 0.135
    elif score_value >= 6:
        enemyY_change = 0.10
        playerImg = pygame.image.load("Spaceship2.png")
        bulletY_change = 0.75

    elif score_value >= 3:
        enemyY_change = 0.08
        if enemyX_change > 0:
            enemyX_change = 0.2
        elif enemyX_change < 0:
            enemyX_change = -0.2

    enemyY += enemyY_change
    if enemyY >= 800:
        enemyY = 0

    # Bullet movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 0
        bullet_state = "ready"
        score_value += 1
        enemyY = random.randint(25, 170)
        enemyX = random.randint(50, 750)

    show_score(textX, textY)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

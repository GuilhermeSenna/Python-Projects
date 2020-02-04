# Objetivos
# Movimento de fundo
# Animação ao perder
# Adicionar Bônus (Velocidade adicionado, falta + munição e - velocidade dos inimigos)
# Novos inimigos, tiro vertical e tiro direcionado ao jogador
# Sistema de pontuações

import pygame
import random
from pygame import mixer
from functions import screen_size, background, distance_between_two_points

# Initialize the pygame
pygame.init()

# create the screen
screen = screen_size(800, 600)

# Background
Background = background('background.png')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)
# -1 significa deixar em loop

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('foguete.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
time_explosion = []
explosionX = []
explosionY = []

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(40)
    time_explosion.append(301)
    explosionX.append(0)
    explosionY.append(0)
# Bullet

# Ready - you can't see the bullet on the screen
# Fire - the bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = 'ready'

# Tempo de duração do bônus
time_bonus = 6001

# Efeito explosao
explosionImg = pygame.image.load('flame.png')

# Bonus velocidade
speedImg = pygame.image.load('thunder.png')

# estado do jogo
game_state = 'ok'

# estado do bonus
bonus_state = 'out'

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    global game_state
    game_state = 'game over'
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    # Desenha na tela
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    # Desenha na tela
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    # Bala sair do meio do foguete
    screen.blit(bulletImg, (x + 16, y + 10))


def create_new_enemy(num_enemies):
    num_enemies += 1
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(40)
    time_explosion.append(301)
    explosionX.append(0)
    explosionY.append(0)
    return num_enemies


bonusX = 0
bonusY = 0
# 1 segundo ~= 380/400 counts

seg = 400


ant = 0
running = True
# Game Loop
new_enemyX_change = 0.5
while running:
    '''if pygame.time.get_ticks() // 1000 == count:
        print(f'Passou-se {pygame.time.get_ticks() // 1000} segundos.')
        count += 1'''

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(Background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystrok is pressed check wether its right or left
        if event.type == pygame.KEYDOWN and game_state is 'ok':
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    # Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemies):

        # Game Over:
        if enemyY[i] > 400:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = new_enemyX_change
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -new_enemyX_change
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = distance_between_two_points(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            escolha = random.choice(['Nothing', 'Nothing', 'Speed', 'Nothing', 'Nothing', 'Nothing', 'Nothing', 'Nothing', 'Nothing'])
            if escolha is 'Speed' and bonus_state is 'out':
                bonus_state = 'in'
                bonusX = enemyX[i]
                bonusY = enemyY[i]
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            explosionX.insert(i, enemyX[i])
            explosionY.insert(i, enemyY[i])
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
            time_explosion.insert(i, 0)

        enemy(enemyX[i], enemyY[i], i)

    # Aumenta dificuldade
    if score_value % 5 == 0 and score_value != 0: # Aumenta 1 inimigo
        if ant != score_value:
            num_of_enemies = create_new_enemy(num_of_enemies)
            if score_value % 10 == 0: # Aumenta velocidade dos inimigos
                for c in range(num_of_enemies):
                    new_enemyX_change += 0.05
                    if enemyX_change[c] < 0:
                        enemyX_change[c] = -new_enemyX_change
                    else:
                        enemyX_change[c] = new_enemyX_change
            ant = score_value

    print(num_of_enemies)

    # Se o bonus esta caindo
    if bonus_state is 'in':
        bonusY += 0.2
        screen.blit(speedImg, (bonusX, bonusY))

        if bonusY >= 600:
            bonus_state = 'out'

    # Player toca no bonus
    touch = distance_between_two_points(bonusX, bonusY, playerX, playerY)
    if touch:
        time_bonus = 15*seg
        if bulletY_change < 4:
            bulletY_change *= 2
        bonusY = 600
        bonus_state = 'out'

    if time_bonus > 0:
        time_bonus -= 1
    else:
        if bulletY_change == 4:
            bulletY_change = 2
            time_bonus = 15*seg
        elif bulletY_change == 2:
            bulletY_change = 1

    # Efeito de explosao
    for j in range(num_of_enemies):
        if time_explosion[j] < 300:
            time_explosion[j] += 1
            screen.blit(explosionImg, (explosionX[j], explosionY[j]))

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

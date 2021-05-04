from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transfrom.scale(image.load(player_image), (wight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_w] and self.rect.y < 500:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

window = display.set_mode((500, 500))
display.set_caption('Ping-pong')

game = True 
finish = False
clock = time.Clock()
FPS = 60

racket1= Player('image.png', 10, 100, 20, 100, 2)
racket2= Player('image.png', 410, 100, 20, 100, 2)

ball = GameSprite('image.png', 200, 200, 50, 10)

font.init()
font1 = font.SysFont("Arial", 36)
lose1 = font1.render("Игрок 1 проиграл", True (180,0,0))
lose2 = font1.render("Игрок 2 проиграл", True (0,180,0))


speed_x = 3
speed_y = 3

if finish != True:
    racket1.update_l()
    racket2.update_r()

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2)
    speed_x *= -1

    if ball.rect.y < 0 or ball.rect.y > 400:
        speed_y += -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x > 500:
        finish = True
        window.blit(lose2, (200, 200))

    racket1.update_l()
    




import random
import pygame
import pygame.freetype  # Import the freetype module.
pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Game")
money = pygame.image.load('picture/money.png')

man1 = pygame.image.load('picture/human.png')#sag
man2 = pygame.transform.rotate(man1, 90)#ust
man3 = pygame.transform.rotate(man1, 180)#sol
man4 = pygame.transform.rotate(man1, 270)#asagı

green = [24, 77, 10]
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = ( 255, 0, 0)
x = 100
y = 100
width = 40
height = 60
vel = 4
moneyy = 0
#parax
mx = 40
my = 40
#adamx
manx = 50
many = 50

sag=True
sol=False
ust=False
asagı=False

def yon(sag,sol,asagı,ust):
    if sag:
        sag = True
        sol = False
        ust = False
        asagı = False
        win.blit(man1, (x, y))
        pygame.display.update()
    if sol:
        sag = False
        sol = True
        ust = False
        asagı = False
        win.blit(man3, (x, y))
        pygame.display.update()
    if asagı:
        sag = False
        sol = False
        ust = False
        asagı = True
        win.blit(man4, (x, y))
        pygame.display.update()
    if ust:
        sag = False
        sol = False
        ust = True
        asagı = False
        win.blit(man2, (x, y))
        pygame.display.update()


isJump = False
jumpCount =False
#m = random.randrange(50,600)
ma = random.randrange(60,600)
mb = random.randrange(60,600)


def init():

    #ekran
    win.fill(green)
    #para
    win.blit(money, (m, m))
    #karakter
    yon(sag, sol, asagı, ust)
    #güncellemeler
    updatem()
    updatemoney()
    update()
    #ekrana yüklemek
    pygame.display.update()
#çok önemli en zor kısım


def update():
    font = pygame.font.SysFont("comicsans", 25, True)
    text = font.render("Money: " + str(moneyy), 1, (255, 255, 255))
    win.blit(text, (650, 30))


def updatemoney():

    hitboxmoney = (m-10, m-10, mx, my)
    pygame.draw.rect(win, (255, 0, 0), hitboxmoney, 2)
def updatem():

    hitboxman = (x-13,y-10 , manx, many)
    pygame.draw.rect(win, (255, 0, 0), hitboxman, 2)

def screen():


    init()
rn = True
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if y < m - 20 + my and y > m - 20:
        if x - 5 > m - 20 and x - 13 < m - 20 + mx:
            moneyy = moneyy + 10
            rn = True
            print("oldu")
    if rn:
        m=random.randrange(50, 600)
        rn=False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        sag = False
        sol = True
        ust = False
        asagı = False
        x -= vel

    if keys[pygame.K_d] and x < 800 - vel - width:
        sag = True
        sol = False
        ust = False
        asagı = False
        x += vel

    if not (isJump):
        if keys[pygame.K_w] and y > vel:
            sag = False
            sol = False
            ust = True
            asagı = False
            y -= vel

        if keys[pygame.K_s] and y < 600 - height - vel:
            sag = False
            sol = False
            ust = False
            asagı = True
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    clock.tick(27)
    
    screen()


pygame.quit()

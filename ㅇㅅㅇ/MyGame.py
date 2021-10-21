import pygame as PG

PG.init()
PG.display.set_caption("Freeze Tag")

# RGB 색 전역변수
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 화면 변수
xSize = 1366
ySize = 768
screen = PG.display.set_mode((xSize, ySize))
background_image = PG.image.load("C:\ㅇㅅㅇ\image\Map_1.jpg")
background_image = PG.transform.scale(background_image, (xSize, ySize))
rect = background_image.get_rect()
rect = rect.move((0, 0))



# 루프 변수
running = False
clock = PG.time.Clock()
while not running:
    clock.tick(30)

    for event in PG.event.get():
        if event.type == PG.QUIT:
            running = True
    
    screen.blit(background_image, rect)

    PG.display.flip()

PG.quit()
import pygame as PG
from pygame import key

xSize = 1050
ySize = 700
clock = PG.time.Clock()

class base:
    
    def __init__(self):
        pass
    
    # GUI 크기
    def screen():
        return PG.display.set_mode((xSize, ySize))

    # 바탕화면 반환
    def BG_image():
        background_image = PG.image.load("ㅇㅅㅇ\image\map\BG.png")
        background_image = PG.transform.scale(background_image, (xSize, ySize))
        return background_image

    # 초기화 및 제목 설정
    def start():
        PG.init()
        PG.display.set_caption("escape!")

    # 화면 출력 및 종료 이벤트
    def loop_fps():
        running = True
        
        while running:
            clock.tick(30)
            
            for event in PG.event.get():
                if event.type == PG.QUIT or (event.type == PG.KEYDOWN and event.key == PG.K_F4 and (key[PG.K_LALT] or key[PG.K_RALT])):
                    running = False

            PG.display.flip()


import pygame as PG

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
        background_image = PG.image.load("image\map\BG.png")
        background_image = PG.transform.scale(background_image, (xSize, ySize))
        return background_image

    # 초기화 및 제목 설정
    def start():
        PG.init()
        PG.display.set_caption("escape!")

    # 폰트 적용된 텍스트
    def Font_text(Contents, Tsize):
        myFont = PG.font.Font("ka1.ttf", Tsize)
        BLACK = ( 0, 0, 0 )
        return myFont.render("{}".format(Contents), True, BLACK)
import pygame as PG
import Methods as Mtd
import GrassMap_2

Mtd.base.start()

def view():
    # 화면 변수
    screen = Mtd.base.screen()
    Mtd.base.BG_image()
    
    # 타일 변수
    Grass_mid = PG.image.load("ㅇㅅㅇ\image\Tiles\grassMid.png")
    Grass_base = PG.image.load("ㅇㅅㅇ\image\Tiles\grassCenter.png")

    GM_dest = Grass_mid.get_rect()
    GB_dest = Grass_base.get_rect()

    for i in range(15):
        globals()['GM_dest{}'.format(i)] = GM_dest
        globals()['GB_dest{}'.format(i)] = GB_dest

    GM_dest0 = PG.Rect.move(GM_dest, 0, 560)
    GM_dest1 = PG.Rect.move(GM_dest, 70, 560)
    GM_dest2 = PG.Rect.move(GM_dest, 140, 560)
    GM_dest3 = PG.Rect.move(GM_dest, 210, 560)
    GM_dest4 = PG.Rect.move(GM_dest, 280, 560)
    GM_dest5 = PG.Rect.move(GM_dest, 350, 560)
    GM_dest6 = PG.Rect.move(GM_dest, 420, 560)
    GM_dest7 = PG.Rect.move(GM_dest, 490, 560)
    GM_dest8 = PG.Rect.move(GM_dest, 560, 560)
    GM_dest9 = PG.Rect.move(GM_dest, 630, 560)
    GM_dest10 = PG.Rect.move(GM_dest, 700, 560)
    GM_dest11 = PG.Rect.move(GM_dest, 770, 560)
    GM_dest12 = PG.Rect.move(GM_dest, 840, 560)
    GM_dest13 = PG.Rect.move(GM_dest, 910, 560)
    GM_dest14 = PG.Rect.move(GM_dest, 980, 560)

    GB_dest0 = PG.Rect.move(GM_dest, 0, 630)
    GB_dest1 = PG.Rect.move(GM_dest, 70, 630)
    GB_dest2 = PG.Rect.move(GM_dest, 140, 630)
    GB_dest3 = PG.Rect.move(GM_dest, 210, 630)
    GB_dest4 = PG.Rect.move(GM_dest, 280, 630)
    GB_dest5 = PG.Rect.move(GM_dest, 350, 630)
    GB_dest6 = PG.Rect.move(GM_dest, 420, 630)
    GB_dest7 = PG.Rect.move(GM_dest, 490, 630)
    GB_dest8 = PG.Rect.move(GM_dest, 560, 630)
    GB_dest9 = PG.Rect.move(GM_dest, 630, 630)
    GB_dest10 = PG.Rect.move(GM_dest, 700, 630)
    GB_dest11 = PG.Rect.move(GM_dest, 770, 630)
    GB_dest12 = PG.Rect.move(GM_dest, 840, 630)
    GB_dest13 = PG.Rect.move(GM_dest, 910, 630)
    GB_dest14 = PG.Rect.move(GM_dest, 980, 630)

    screen.blit(Mtd.base.BG_image(), Mtd.base.BG_image().get_rect())
    screen.blit(Grass_mid, GM_dest0)
    screen.blit(Grass_mid, GM_dest1)
    screen.blit(Grass_mid, GM_dest2)
    screen.blit(Grass_mid, GM_dest3)
    screen.blit(Grass_mid, GM_dest4)
    screen.blit(Grass_mid, GM_dest5)
    screen.blit(Grass_mid, GM_dest6)
    screen.blit(Grass_mid, GM_dest7)
    screen.blit(Grass_mid, GM_dest8)
    screen.blit(Grass_mid, GM_dest9)
    screen.blit(Grass_mid, GM_dest10)
    screen.blit(Grass_mid, GM_dest11)
    screen.blit(Grass_mid, GM_dest12)
    screen.blit(Grass_mid, GM_dest13)
    screen.blit(Grass_mid, GM_dest14)

    screen.blit(Grass_base, GB_dest0)
    screen.blit(Grass_base, GB_dest1)
    screen.blit(Grass_base, GB_dest2)
    screen.blit(Grass_base, GB_dest3)
    screen.blit(Grass_base, GB_dest4)
    screen.blit(Grass_base, GB_dest5)
    screen.blit(Grass_base, GB_dest6)
    screen.blit(Grass_base, GB_dest7)
    screen.blit(Grass_base, GB_dest8)
    screen.blit(Grass_base, GB_dest9)
    screen.blit(Grass_base, GB_dest10)
    screen.blit(Grass_base, GB_dest11)
    screen.blit(Grass_base, GB_dest12)
    screen.blit(Grass_base, GB_dest13)
    screen.blit(Grass_base, GB_dest14)

    Mtd.base.loop_fps() 

PG.quit()
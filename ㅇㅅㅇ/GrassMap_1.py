import pygame as PG
import Methods as Mtd
from pygame import key
import GrassMap_2

Mtd.base.start()

def view():
    running = True
    clock = PG.time.Clock()

    player_images_right = []
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk01.png') )
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk02.png') )
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk03.png') )
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk04.png') )
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk05.png') )
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk06.png') )
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk07.png') )
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk08.png') )
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk09.png') )
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk10.png') )
    player_images_right.append( PG.image.load('ㅇㅅㅇ\image\Player\p1_walk\PNG\p1_walk11.png') )
    player_current = 0

    player_images_left = [PG.transform.flip(image, True, False) for image in player_images_right]

    player = player_images_right[player_current]
    player = player.get_rect()

    playerX = 0
    playerY = 460

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

    
    blit_tuple = ((Mtd.base.BG_image(), Mtd.base.BG_image().get_rect()),
    (Grass_mid, GM_dest0), (Grass_mid, GM_dest1), (Grass_mid, GM_dest2),
    (Grass_mid, GM_dest3), (Grass_mid, GM_dest4), (Grass_mid, GM_dest5),
    (Grass_mid, GM_dest6), (Grass_mid, GM_dest7), (Grass_mid, GM_dest8),
    (Grass_mid, GM_dest9), (Grass_mid, GM_dest10), (Grass_mid, GM_dest11),
    (Grass_mid, GM_dest12), (Grass_mid, GM_dest13), (Grass_mid, GM_dest14),
    (Grass_base, GB_dest0), (Grass_base, GB_dest1), (Grass_base, GB_dest2),
    (Grass_base, GB_dest3), (Grass_base, GB_dest4), (Grass_base, GB_dest5),
    (Grass_base, GB_dest6), (Grass_base, GB_dest7), (Grass_base, GB_dest8),
    (Grass_base, GB_dest9), (Grass_base, GB_dest10), (Grass_base, GB_dest11),
    (Grass_base, GB_dest12), (Grass_base, GB_dest13), (Grass_base, GB_dest14))
    screen.blits(blit_tuple, True)
   
    while running:
        clock.tick(30)

        for event in PG.event.get():
            if event.type == PG.QUIT or (event.type == PG.KEYDOWN and event.key == PG.K_F4 and (key[PG.K_LALT] or key[PG.K_RALT])):
                running = False
            elif event.type == PG.KEYDOWN:
                if event.key == PG.K_RIGHT:
                    return
                elif event.key == PG.K_LEFT:
                    return
            elif event.type == PG.KEYUP:
                if event.key == PG.K_RIGHT or event.key == PG.K_LEFT:
                    player.velocity_x = 0
                    player.state = 0

        PG.display.flip()
    
PG.quit()
import sys
import pygame as PG
import Methods as Mtd
from pygame import key
import random

def view():
    running = True
    clock = PG.time.Clock()
    playerX = 0
    playerY = 463
    move_right = False
    move_left = False
    move_up = False
    state = True
    walking_steps = 0
    player_list_count = 0
    jump_count = 10

    bigE = Mtd.base.Font_text("E", 150)
    bigS = Mtd.base.Font_text("S", 150)
    bigC = Mtd.base.Font_text("C", 150)
    bigA = Mtd.base.Font_text("A", 150)
    bigP = Mtd.base.Font_text("P", 150)

    smallE = Mtd.base.Font_text("E", 70)
    smallS = Mtd.base.Font_text("S", 70)
    smallC = Mtd.base.Font_text("C", 70)
    smallA = Mtd.base.Font_text("A", 70)
    smallP = Mtd.base.Font_text("P", 70)

    big_txt_rect = bigE.get_rect()
    big_txt_rect.y = -50

    small_txt_rect = smallE.get_rect()
    small_txt_rect.y = 20

    GTS_small_txt_rect = smallE.get_rect()
    GTS_small_txt_rect.y = 550 - GTS_small_txt_rect.height

    big_text = [bigE, bigS, bigC, bigA, bigP]
    small_text = [smallE, smallS, smallC, smallA, smallP]

    # player image list 생성
    player_images_right = []
    player_images_right.append( PG.image.load('image\Player\p1_stand.png') )
    player_images_right.append( PG.image.load('image\Player\p1_jump.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk01.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk02.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk03.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk04.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk05.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk06.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk07.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk08.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk09.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk10.png') )
    player_images_right.append( PG.image.load('image\Player\p1_walk\PNG\p1_walk11.png') )
    
    player_images_left = [PG.transform.flip(image, True, False) for image in player_images_right]
    PWR = player_images_right[player_list_count]
    PWR_rect = PWR.get_rect()
    PWR_rect = PG.Rect.move(PWR_rect, playerX, playerY)

    # 화면 변수
    screen = Mtd.base.screen()
    Mtd.base.BG_image()
    
    # 타일 변수
    Grass_mid = PG.image.load("image\Tiles\grassMid.png")
    Grass_base = PG.image.load("image\Tiles\grassCenter.png")

    GM_dest = Grass_mid.get_rect()
    GB_dest = Grass_base.get_rect()

    # 타일 1개 당 rect 설정 (바닥)
    for i in range(15):
        globals()['GM_dest{}'.format(i)] = GM_dest
        globals()['GM_dest{}'.format(i)] = PG.Rect.move(GM_dest, i * 70, 560)
        globals()['GB_dest{}'.format(i)] = GB_dest
        globals()['GB_dest{}'.format(i)] = PG.Rect.move(GB_dest, i * 70, 630)

    # 타일 출력
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

    # 소리 무한 반복 재생
    PG.mixer.music.load("music\Field.mp3")
    PG.mixer.music.play(-1, 0, 30)
    big_falling_cnt = 0
    small_falling_cnt = 0
    small_GTS_cnt = 0

    falling_big_text = random.choice(big_text)
    falling_small_text = random.choice(small_text)
    GTS_small_text = random.choice(small_text)

    big_txt_rect.x = random.randrange(0, 1050 - big_txt_rect.width)
    small_txt_rect.x = random.randrange(0, 1050 - small_txt_rect.width)
    GTS_small_txt_rect.x = 1050 + GTS_small_txt_rect.width

    time_score = 0

    while running:
        clock.tick(60)
        time_score += 1
        # 게임 종료 이벤트
        for event in PG.event.get():
            if event.type == PG.QUIT or (event.type == PG.KEYDOWN and event.key == PG.K_F4 and (key[PG.K_LALT] or key[PG.K_RALT])):
                running = False

        # keys 변수로 방향 이벤트 받고 처리 
        keys = PG.key.get_pressed()

        if state:
            if keys[PG.K_RIGHT]:
                move_right = True
                move_left = False
                walking_steps = 8
                if PWR_rect.left < 1050 - PWR_rect.width:
                    PWR_rect.left += walking_steps
                else:
                    PWR_rect.left = 1050 - PWR_rect.width

            if keys[PG.K_LEFT]:
                move_left = True
                move_right = False
                walking_steps = 8
                if PWR_rect.left > 0:
                    PWR_rect.left -= walking_steps
                else:
                    PWR_rect.left = 0

            if not move_up:
                if keys[PG.K_SPACE]:
                    move_up = True
                    move_left = False
                    move_right = False
                    player_list_count = 1
                    if event.type == PG.KEYDOWN and keys[PG.K_RIGHT]:
                        PWR = player_images_right[player_list_count]
                    if event.type == PG.KEYDOWN and keys[PG.K_LEFT]:
                        PWR = player_images_left[player_list_count]
                    walking_steps = 0
            else:
                if jump_count >= -10:
                    PWR_rect.y -= (jump_count * abs(jump_count)) * 0.5
                    jump_count -= 1
                else:
                    move_up = False
                    jump_count = 10
                    PWR_rect.y = playerY

            # 방향에 따라 image list 선택 후 프레임에 따라 image 바꿈
            if move_right == True:
                if walking_steps > 0:
                    player_list_count = (player_list_count + 1) % len(player_images_right)
                    if player_list_count == 0 or player_list_count == 1:
                        while True:
                            player_list_count += 1
                            if player_list_count >= 2:
                                break
                    if move_up == True:
                        player_list_count = 1
                    else: 
                        pass
                    PWR = player_images_right[player_list_count]
                    walking_steps -= 1
                else:
                    move_right = False
                    player_list_count = 0
                    PWR = player_images_right[player_list_count]

            elif move_left == True:
                if walking_steps > 0:
                    player_list_count = (player_list_count + 1) % len(player_images_left)
                    if player_list_count == 0 or player_list_count == 1:
                        while True:
                            player_list_count += 1
                            if player_list_count >= 2:
                                break
                    if move_up == True:
                        
                        player_list_count = 1
                    else: 
                        pass
                    PWR = player_images_left[player_list_count]
                    walking_steps -= 1
                else:
                    move_left = False
                    player_list_count = 0
                    PWR = player_images_left[player_list_count]
            
            # 마지막 이벤트에 따라 list를 바꿔서 stand 모습을 유지
            else:
                if event.type == PG.KEYDOWN and keys[PG.K_RIGHT]:
                    PWR = player_images_right[player_list_count]
                if event.type == PG.KEYDOWN and keys[PG.K_LEFT]:
                    PWR = player_images_left[player_list_count]

            if big_falling_cnt == 0:
                big_txt_rect.y += 10
                if big_txt_rect.y > 700:
                    big_txt_rect.y = -30
                    falling_big_text = random.choice(big_text)
                    big_txt_rect.x = random.randrange(0, 1050 - big_txt_rect.width)

            if small_falling_cnt == 0:
                small_txt_rect.y += 15
                if small_txt_rect.y > 700:
                    small_txt_rect.y = -30
                    falling_small_text = random.choice(small_text)
                    small_txt_rect.x = random.randrange(0, 1050 - small_txt_rect.width)

            if small_GTS_cnt == 0:
                GTS_small_txt_rect.x -= 8
                if GTS_small_txt_rect.x < 0:
                    GTS_small_text = random.choice(small_text)
                    GTS_small_txt_rect.x = 1050 + GTS_small_txt_rect.width

            screen.blits(blit_tuple, True)
            screen.blit(PWR, PWR_rect)
            screen.blit(falling_big_text, big_txt_rect)
            screen.blit(falling_small_text, small_txt_rect)
            screen.blit(GTS_small_text, GTS_small_txt_rect)

            if PWR_rect.colliderect(big_txt_rect) or PWR_rect.colliderect(small_txt_rect) or PWR_rect.colliderect(GTS_small_txt_rect):
                score = Mtd.base.Font_text("score   " + str(time_score), 50)
                score_rect = score.get_rect()
                score_rect.centerx = 1050 / 2
                score_rect.y = 180

                again = Mtd.base.Font_text("Try Again Press G", 30)
                again_rect = again.get_rect()
                again_rect.centerx = 1050 / 2
                again_rect.y = 300

                screen.blits(blit_tuple, True)
                screen.blit(score, score_rect)
                screen.blit(again, again_rect)
                state = False
                PG.mixer.music.pause()

        if not state:    
            if keys[PG.K_g]:
                state = True
                time_score = 0
                PWR_rect.x = 0
                PWR_rect.y = 463
                big_txt_rect.x = random.randrange(0, 1050 - big_txt_rect.width)
                big_txt_rect.y = -50
                small_txt_rect.x = random.randrange(0, 1050 - small_txt_rect.width)
                small_txt_rect.y = 20
                GTS_small_txt_rect.x = 1050 + GTS_small_txt_rect.width
                PG.mixer.music.rewind()
                PG.mixer.music.unpause()

        PG.display.update()
    
    PG.quit()
    sys.exit(0)
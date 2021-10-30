import pygame as PG
from pygame import key
import Methods as Mtd
import Play_game

Mtd.base.start()

xSize = 1050
ySize = 700

Main_title = Mtd.base.Font_text("ESCAPE", 160)
Main_title_rect = Main_title.get_rect()
Main_title_rect.centerx = xSize / 2
Main_title_rect.y = 180

Sub_title = Mtd.base.Font_text("Press any key to start", 30)
Sub_title_rect = Sub_title.get_rect()
Sub_title_rect.centerx = xSize / 2
Sub_title_rect.y = 500

blit_tuple = (Mtd.base.BG_image(), Mtd.base.BG_image().get_rect()), (Main_title, Main_title_rect), (Sub_title, Sub_title_rect)
Lobby_blit = Mtd.base.screen().blits(blit_tuple, True)

running = True
clock = PG.time.Clock()
state = False

while running:
    clock.tick(30)
      
    for event in PG.event.get():
        if event.type == PG.QUIT or (event.type == PG.KEYDOWN and event.key == PG.K_F4 and (key[PG.K_LALT] or key[PG.K_RALT])):
            running = False

        if event.type == PG.KEYDOWN:
            state = True

    if state == True:
        Play_game.view()
        
    PG.display.flip()

PG.quit()
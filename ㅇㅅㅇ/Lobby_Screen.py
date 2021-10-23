import pygame as PG
import Methods as Mtd
import GrassMap_1

Mtd.base.start()

Main_title = Mtd.base.Font_text(30)
blit_tuple = (Mtd.base.BG_image(), Mtd.base.BG_image().get_rect()), (Main_title, Main_title.get_rect())
Mtd.base.screen().blits(blit_tuple, True)
"""for event in PG.event.get():
    if event.type == PG.KEYDOWN and event.key == PG.K_a:
            state = True

if state == True:
    SurFace.inflate(0, 0)
    GrassMap_1.view()"""

Mtd.base.loop_fps()
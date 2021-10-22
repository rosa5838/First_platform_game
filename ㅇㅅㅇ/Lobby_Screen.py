import pygame as PG
import Methods as Mtd
import GrassMap_1

Mtd.base.start()

SurFace = Mtd.base.screen().blit(Mtd.base.BG_image(), Mtd.base.BG_image().get_rect())

state = False

for event in PG.event.get():
    if event.type == PG.KEYDOWN and event.key == PG.K_a:
            state = True

if state == True:
    SurFace.inflate(0, 0)
    GrassMap_1.view()

Mtd.base.loop_fps()
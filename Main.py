#Wizard Platform Game

import pygame as pg
import random
from settings import * #Imports all from settings
from Sprites import * #Imports Sprites from Sprites.py


#Game class, another object
class Game:
    def __init__(self):
        
        pg.init()
        pg.mixer.init()
        #WIDTH and HEIGHT are constants from settings.py file, the rest if for controlling the screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only when falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platform, False)
            if hits:
                self.player.pos = hits[0].rect.top + 1
                self.player.vel.y = 0

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()
        #Add background when available
        # dungeon_background = pg.image.load()
        # screen.blit(dungeon_background,(0,0))
        # pg.draw.rect(screen,(255,0,0), rect)
        
        

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()

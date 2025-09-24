
import pygame
import random
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('north-bound kitty')
fps = 60
clock = pygame.time.Clock()

moving_left = False
moving_right = False
moving_up = False
moving_down = False
bottom_left = False
bottom_right = False
top_left = False
top_right = False

class Lootbar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lootbar_animationlist = []
        self.bar_index = 0
        self.framerate = 0.10
        self.lootable = False

        self.lootbar_animationlist.append(pygame.image.load('assets/blank.png'))
        self.lootbar_animationlist.append(pygame.image.load('assets/menui/loot_bar1.png'))
        self.lootbar_animationlist.append(pygame.image.load('assets/menui/loot_bar2.png'))
        self.lootbar_animationlist.append(pygame.image.load('assets/menui/loot_bar3.png'))
        self.lootbar_animationlist.append(pygame.image.load('assets/menui/loot_bar4.png'))
        self.lootbar_animationlist.append(pygame.image.load('assets/menui/loot_bar5.png'))
        self.lootbar_animationlist.append(pygame.image.load('assets/menui/loot_bar6.png'))
        self.lootbar_animationlist.append(pygame.image.load('assets/menui/loot_bar7.png'))

        self.lootable = False
        self.loot_bar = self.lootbar_animationlist[int(self.bar_index)]
        self.loot_bar = pygame.transform.scale(self.loot_bar, (200, 100))
        self.loot_bar_rect = self.loot_bar.get_rect()
        self.loot_bar_rect.center = (400, 500)


    def draw_lootbar(self, is_looting):
        key = pygame.key.get_pressed()
        if player.player_rect.colliderect(rs1.rockspot_rect) or player.player_rect.colliderect(rs2.rockspot_rect) \
           or player.player_rect.colliderect(rs3.rockspot_rect):
            self.lootable = True
        else:
            self.lootable = False
        if key[pygame.K_e]:
            if self.lootable == False:
                self.bar_index = 0
            if self.lootable == True:
                self.bar_index += self.framerate
                if self.bar_index >= 8:
                    self.lootable = False
                    self.bar_index = 0

        self.loot_bar = self.lootbar_animationlist[int(self.bar_index)]
        self.loot_bar = pygame.transform.scale(self.loot_bar, (200, 100))
        screen.blit(self.loot_bar, self.loot_bar_rect)
    

lb = Lootbar()

class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y, grass_speed):
        pygame.sprite.Sprite.__init__(self)
        self.grass_animation = []
        self.grass_index = 0
        self.x = x
        self.y = y
        self.grass_speed = grass_speed
        self.grass_animation.append(pygame.image.load('assets/textures/grass1.png'))
        self.grass_animation.append(pygame.image.load('assets/textures/grass2.png'))
        self.grass_animation.append(pygame.image.load('assets/textures/grass3.png'))

        self.grass = self.grass_animation[int(self.grass_index)]
        self.grass_rect = self.grass.get_rect()

    def draw(self):
        self.grass_index += self.grass_speed
        if self.grass_index > 3:
            self.grass_index = 0
        self.grass = self.grass_animation[int(self.grass_index)]
        screen.blit(self.grass, (self.x, self.y))

        if pause_state == 1:
            self.grass_index = 0

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x += 3
        if key[pygame.K_d]:
            self.x -= 3
        if key[pygame.K_w]:
            self.y += 3
        if key[pygame.K_s]:
            self.y -= 3

    def grass_oob(self):
        if self.x < -400:
            self.x = 800
        if self.x > 800:
            self.x = -400

        if self.y < -300:
            self.y = 600
        if self.y > 600:
            self.y = -300
        
#grasstiles  ###
spot1 = Grass(0, 0, 0.10)
spot2 = Grass(400, 0, 0.10)
spot3 = Grass(0, 300, 0.10)
spot4 = Grass(400, 300, 0.10)
spot5 = Grass(-400, 0, 0.10)
spot6 = Grass(-400, 300, 0.10)
spot7 = Grass(-400, 600, 0.10)
spot8 = Grass(0, 600, 0.10)
spot9 = Grass(400, 600, 0.10)

#  pause logic
pause_state = 0
pause = pygame.image.load('assets/menui/pause.png')
pause = pygame.transform.scale(pause, (800, 600))
pause_dest = 50, 50

is_looting = False

class Rocks:
    def __init__(self, x, y, mineral):
        self.rock_list = []
        self.x = x
        self.y = y
        self.mineral = mineral
        self.rock_list.append(pygame.image.load('assets/rocks/amethyst.png'))
        self.rock_list.append(pygame.image.load('assets/rocks/coal.png'))
        self.rock_list.append(pygame.image.load('assets/rocks/diamond.png'))
        self.rock_list.append(pygame.image.load('assets/rocks/jade.png'))
        self.rock_list.append(pygame.image.load('assets/rocks/quartz.png'))
        self.rock_list.append(pygame.image.load('assets/rocks/topaz.png'))
        self.rock_list.append(pygame.image.load('assets/rocks/trash3coin.png'))
        self.rock_list.append(pygame.image.load('assets/rocks/trash1.png'))
        self.rock_list.append(pygame.image.load('assets/rocks/trash2.png'))
        self.rock = self.rock_list[int(self.mineral)]

    def mineral_ui(self):
        self.r0ck = self.rock_list[int(self.mineral)]
        self.rock_rect = self.rock.get_rect()
        self.rock = pygame.transform.scale(self.rock, (50, 50))
        screen.blit(self.rock, (self.x, self.y))

    def ui_move(self):
        self.r0ck = self.rock_list[int(self.mineral)]
        self.rock_rect = self.rock.get_rect()
        self.rock_rect.center = (self.x, self.y)
        self.rock = pygame.transform.scale(self.rock, (50, 50))
        screen.blit(self.rock, (self.x, self.y))

        self.y -= 3

### rocs n mineralz
amethyst = Rocks(10, 10, 0)
coal = Rocks(90, 10, 1)
diamond = Rocks (175, 10, 2)
jade = Rocks(10, 90, 3)
quartz = Rocks(90, 90, 4)
topaz = Rocks(175, 90, 5)
coin = Rocks(700, 10, 6)

am_ui = Rocks(300, -300, 0)
co_ui = Rocks(300, -300, 1)
di_ui = Rocks(300, -300, 2)
ja_ui = Rocks(300, -300, 3)
qu_ui = Rocks(300, -300, 4)
to_ui = Rocks(300, -300, 5)
coi_ui = Rocks(300, -300, 6)
coi2_ui = Rocks(300, -300, 6)
tr1_ui = Rocks(300, -300, 7)
tr2_ui = Rocks(300, -300, 8)

##text
font = pygame.font.SysFont('bahnschrift', 20)
sell_font = pygame.font.SysFont('bahnschrift', 40)
##text
class Rock_stats:
    def __init__(self, rock_qty, x, y):
        self.rock_qty = 0
        self.x = x
        self.y = y
        self.uno = 1
        self.rock_text = font.render(f"x{self.rock_qty}", True, (15, 15, 15))

    def draw_text(self):
   #     key = pygame.key.get_pressed()
    #    if key[pygame.K_f]:
   #         self.rock_qty += self.uno
            
        self.rock_text = font.render(f"x{self.rock_qty}", True, (15, 15, 15))
        screen.blit(self.rock_text, (self.x, self.y))

###sounds
nbk_ost = pygame.mixer.Sound('sounds/ost.mp3')
nbk_ost.set_volume(.1)
collect_sound = pygame.mixer.Sound('sounds/sound1.mp3')
collect_sound.set_volume(5)
sell_sfx = pygame.mixer.Sound('sounds/soldsfx.mp3')
sell_sfx.set_volume(.1)
lvl_sfx = pygame.mixer.Sound('sounds/lvlup.mp3')
lvl_sfx.set_volume(.1)

ameth = Rock_stats(0, 55, 20)
co = Rock_stats(0, 135, 20)
diam = Rock_stats(0, 220, 20)
jad = Rock_stats(0, 60, 90)
quart = Rock_stats(0, 135, 90)
topa = Rock_stats(0, 220, 90)
coi = Rock_stats(0, 740, 30)

def roll_the_dice():
    rtd = random.randint(1, 600)
    x = 61
    if lb.bar_index >= 7:
        collect_sound.play()
        if rtd > 0 and rtd < 45:
            ameth.rock_qty += 1
            am_ui.x = 350
            am_ui.y = 350
                
        if rtd >= 45 and rtd < 150:
            co.rock_qty += 1
            co_ui.x = 350
            co_ui.y = 350
            
        if rtd >= 150 and rtd < 162:
            diam.rock_qty += 1
            di_ui.x = 350
            di_ui.y = 350
            
        if rtd >= 162 and rtd < 210:
            jad.rock_qty += 1
            ja_ui.x = 350
            ja_ui.y = 350
            
        if rtd >= 210 and rtd < 280:
            quart.rock_qty += 1
            qu_ui.x = 350
            qu_ui.y = 350
            
        if rtd >= 280 and rtd < 350:
            topa.rock_qty += 1
            to_ui.x = 350
            to_ui.y = 350
            
        if rtd >= 350 and rtd < 455:
            coi.rock_qty += 1
            coi_ui.x = 350
            coi_ui.y = 350
            
        if rtd >= 455 and rtd < 525:
            tr1_ui.x = 350
            tr1_ui.y = 350

        if rtd >= 525 and rtd <= 600:
            tr2_ui.x = 350
            tr2_ui.y = 350


def text_scroll():
    am_text = font.render('x1 amethyst', True, (255, 255, 255))
    screen.blit(am_text, (am_ui.x + 50, am_ui.y + 15))
    co_text = font.render('x1 coal', True, (255, 255, 255))
    screen.blit(co_text, (co_ui.x + 50, co_ui.y + 15))
    di_text = font.render('x1 diamond', True, (255, 255, 255))
    screen.blit(di_text, (di_ui.x + 50, di_ui.y + 15))
    ja_text = font.render('x1 jade', True, (255, 255, 255))
    screen.blit(ja_text, (ja_ui.x + 50, ja_ui.y + 15))
    qu_text = font.render('x1 quartz', True, (255, 255, 255))
    screen.blit(qu_text, (qu_ui.x + 50, qu_ui.y + 15))
    to_text = font.render('x1 topaz', True, (255, 255, 255))
    screen.blit(to_text, (to_ui.x + 50, to_ui.y + 15))
    coi_text = font.render('x1 coin', True, (255, 255, 255))
    screen.blit(coi_text, (coi_ui.x + 50, coi_ui.y + 15))
    tr1_text = font.render('x1 can', True, (255, 255, 255))
    screen.blit(tr1_text, (tr1_ui.x + 50, tr1_ui.y + 15))
    tr2_text = font.render('x1 boot', True, (255, 255, 255))
    screen.blit(tr2_text, (tr2_ui.x + 50, tr2_ui.y + 15))

    trader_text = font.render(f'${the_trader.total}', True, (22, 88, 34))
    coi2_ui.y -= 3
    screen.blit(trader_text, (coi2_ui.x + 50, coi2_ui.y))   

#  main charecter ###3
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.animation_list = []
        self.index = 0
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral1.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral2.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral3.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral4.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral5.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral6.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral7.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral8.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral9.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral10.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral11.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral12.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral13.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral14.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral15.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral16.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral17.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral18.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral19.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral20.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral21.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral22.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral23.png'))
        self.animation_list.append(pygame.image.load('assets/charecter/mc_neutral24.png'))

        self.player = self.animation_list[int(self.index)]
        self.player_rect = self.player.get_rect()
        self.player_rect.center = (self.x, self.y)

    def move(self, moving_left, moving_right, moving_up, moving_down, bottom_left, bottom_right, top_left, top_right, speed):

        idle = False
        if moving_down and moving_left:
            bottom_left = True
            if bottom_left == True:
                moving_down = False
                moving_left = False
        if moving_down and moving_right:
            bottom_right = True
            if bottom_right == True:
                moving_down = False
                moving_right = False
        if moving_up and moving_left:
            top_left = True
            if top_left:
                moving_up = False
                moving_left = False
        if moving_up and moving_right:
            top_right = True
            if top_right:
                moving_up = False
                moving_right = False
            
        if moving_left == False and moving_right == False and moving_up == False and moving_down == False and bottom_left == False and bottom_right == False \
          and top_left == False and top_right == False:
            idle = True
        if idle == True:
            self.index += speed
            if int(self.index) >= 2:
                self.index = 0
        if pause_state == 1:
            self.index = 0

        if moving_left:
            idle = False 
            self.index += speed
            if self.index < 8 or self.index > 12:
                self.index = 9
           
        if moving_right:
            idle = False
            self.index += speed
            if self.index < 6 or self.index > 9:
                self.index = 6
            if moving_down:
                self.index += speed
                if self.index < 15 or self.index > 18:
                    self.index = 15
                

        if moving_up:
            idle = False
            self.index += speed
            if self.index < 3 or self.index > 6:
                self.index = 3

        if moving_down:
            idle = False
            self.index += speed
            if self.index < 0 or self.index > 3:
                self.index = 0

        if bottom_left:
            moving_down = False
            moving_left = False
            idle = False
            self.index += speed
            if self.index < 12 or self.index > 15:
                self.index = 12

        if bottom_right:
            idle = False
            self.index += speed
            if self.index < 15 or self.index > 18:
                self.index = 15

        if top_left:
            idle = False
            self.index += speed
            if self.index < 18 or self.index > 21:
                self.index = 18

        if top_right:
            idle = False
            self.index += speed
            if self.index < 21 or self.index >= 24:
                self.index = 21
            

        self.player = self.animation_list[int(self.index)]
        screen.blit(self.player, self.player_rect)

player = Player(screen_width / 2, screen_height / 2, 5)

## $$ spots to get rocks
class Rockspots(pygame.sprite.Sprite):
    def __init__(self, rs_speed):
        pygame.sprite.Sprite.__init__(self)
        self.rockspot_list = []
        self.rockspot_list.append(pygame.image.load('assets/textures/rockspot1.png'))
        self.rockspot_list.append(pygame.image.load('assets/textures/rockspot2.png'))
        self.rs_index = 0
        self.rs_speed = rs_speed
  #      self.rockspot = pygame.image.load('assets/textures/rockspot1.png')
        self.x = random.randint(10, screen_width - 10)
        self.y = random.randint(10, screen_height - 10)
        self.rockspot = self.rockspot_list[int(self.rs_index)]
        self.rockspot_rect = self.rockspot.get_rect()
        self.rockspot_rect.center = self.x + 35, self.y + 35


    def draw_rs(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x += 3
            self.rockspot_rect.x += 3
        if key[pygame.K_d]:
            self.x -= 3
            self.rockspot_rect.x -= 3
        if key[pygame.K_w]:
            self.y += 3
            self.rockspot_rect.y += 3
        if key[pygame.K_s]:
            self.y -= 3
            self.rockspot_rect.y -= 3

        self.rockspot = self.rockspot_list[int(self.rs_index)]
        self.rs_index += self.rs_speed
        if pause_state == 1:
            self.rs_index = 0
        if self.rs_index >= 2:
            self.rs_index = 0

        if self.x > screen_width + 400 or self.x < -400 or self.y > screen_height + 400 or self.y < -400:
            self.x = random.randint(-400, screen_width + 400)
            self.y = random.randint(-400, screen_height + 400)
            if self.x > 0 and self.x < screen_width:
                self.x = random.randint(-400, screen_width + 400)
            if self.y > 0 and self.y < screen_height:
                self.y = random.randint(-400, screen_height + 400)
            self.rockspot_rect.center = self.x + 35, self.y + 35

        hit = False
        if player.player_rect.colliderect(self.rockspot_rect):
            hit = True
        if lb.bar_index >= 7 and hit == True:
            self.x = random.randint(-390, screen_width + 390)
            self.y = random.randint(-390, screen_height + 390)
            self.rockspot_rect.center = self.x + 35, self.y + 35
            screen.blit(self.rockspot, (self.x, self.y))
            
        self.rockspot = pygame.transform.scale(self.rockspot, (100, 100))
        screen.blit(self.rockspot, (self.x, self.y))

# spot classes
rs1 = Rockspots(0.05)
rs2 = Rockspots(0.05)
rs3 = Rockspots(0.05)

#def collected():
#    hit = False
#    if player.player_rect.colliderect(rs1.rockspot_rect):
 #       hit = True
 #   if lb.bar_index >= 7 and hit == True:
 #       rs1.x = random.randint(-390, screen_width + 390)
 #       rs1.y = random.randint(-390, screen_height + 390)
  #      rs1.rockspot_rect.center = rs1.x, rs1.y
  #      screen.blit(rs1.rockspot, (rs1.x, rs1.y))
  #      rs2.x = random.randint(-390, screen_width + 390)
  #      rs2.y = random.randint(-390, screen_height + 390)
 #    rs2.rockspot_rect.center = rs2.x, rs2.y
 #       screen.blit(rs2.rockspot, (rs2.x, rs2.y))

class Tradesman(pygame.sprite.Sprite):
    def __init__(self, x, y, tradesman_framerate):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.tradesman_framerate = tradesman_framerate
        self.trader_list = []
        self.trader_list.append(pygame.image.load('assets/tradesman/tradesman1.png'))
        self.trader_list.append(pygame.image.load('assets/tradesman/tradesman2.png'))
        self.trader_index = 0
        self.trader = self.trader_list[int(self.trader_index)]
        self.trader_rect = self.trader.get_rect()
        self.trader_rect.center = self.x + 40, self.y + 35 
        self.can_sell = False
        self.total = 0
        self.sold = False

    def draw_trader(self):
        if pause_state == 1:
            self.trader_index = 0
        
        self.trader_index += self.tradesman_framerate
        if self.trader_index >= 2:
            self.trader_index = 0
        self.trader_rect.center = self.x + 40, self.y + 35
        self.trader = self.trader_list[int(self.trader_index)]
        screen.blit(self.trader, (self.x, self.y))

        if moving_left:
            self.x += 3
        if moving_right:
            self.x -= 3
        if moving_down:
            self.y -= 3
        if moving_up:
            self.y += 3

        if self.x > 3500:
            self.x = -50
            self.y = random.randint(10, screen_height - 10)
        if self.x < -3500:
            self.x = screen_width + 50
            self.y = random.randint(10, screen_height - 10)

        if self.y > 3500:
            self.y = -50
            self.x = random.randint(10, screen_width - 10)
        if self.y < -3500:
            self.y = screen_height + 50
            self.x = random.randint(10, screen_width - 10)

    def make_sell(self):
        sell_text = sell_font.render("press 'f' to sell all", True, (0, 0, 0))
        if player.player_rect.colliderect(self.trader_rect) == False:
            self.can_sell = False
        if player.player_rect.colliderect(self.trader_rect):
            key = pygame.key.get_pressed()
            self.can_sell = True
            screen.blit(sell_text, (self.x - 20, self.y + 170))

            if coi2_ui.y < 0:
                self.total = 0
            
            if key[pygame.K_f]:
                sell_sfx.play()
                self.sold = True
                qty1 = ameth.rock_qty * 50
                coi.rock_qty = coi.rock_qty + qty1
                ameth.rock_qty = 0

                qty2 = co.rock_qty * 5
                coi.rock_qty = coi.rock_qty + qty2
                co.rock_qty = 0

                qty3 = diam.rock_qty * 250
                coi.rock_qty = coi.rock_qty + qty3
                diam.rock_qty = 0

                qty4 = jad.rock_qty * 75
                coi.rock_qty = coi.rock_qty + qty4
                jad.rock_qty = 0

                qty5 = quart.rock_qty * 30
                coi.rock_qty = coi.rock_qty + qty5
                quart.rock_qty = 0

                qty6 = topa.rock_qty * 60
                coi.rock_qty = coi.rock_qty + qty6
                topa.rock_qty = 0

                coi2_ui.x = 350
                coi2_ui.y = 350
                res = qty1 + qty2 + qty3 + qty4 + qty5 + qty6
                self.total = res + self.total
                
 
            

the_trader = Tradesman(500, 400, 0.06)
lootable = False


#def make_sell():
#    sell_text = sell_font.render("press 'f' to sell all", True, (255, 255, 255))
#    if player.player_rect.colliderect(the_trader.trader_rect) == False:
#        the_trader.can_sell = False
#    if player.player_rect.colliderect(the_trader.trader_rect):
#        the_trader.can_sell = True
#        screen.blit(sell_text, (245, 400))

#level ui
#lvl = 1
#lvl_ui = font.render(f"lvl: {lvl}", True, (0, 0, 0))
#lvl_ui_spot = (715, 70)


class Lvlhere(pygame.sprite.Sprite):
    def __init__(self, x, y, framerate):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.framerate = framerate
        self.lvl_index = 0
        self.lvlsman_list = []
        self.lvlsman_list.append(pygame.image.load('assets/tradesman/lvlupman1.png'))
        self.lvlsman_list.append(pygame.image.load('assets/tradesman/lvlupman2.png'))
        self.lvl = 0

    def draw(self):
        if pause_state == 1:
            self.lvl_index = 0
        
        self.lvl_index += self.framerate
        if self.lvl_index > 2:
            self.lvl_index = 0
        self.lvlsman = self.lvlsman_list[int(self.lvl_index)]
        self.lvlsman_rect = self.lvlsman.get_rect()
        self.lvlsman_rect.center = (self.x, self.y)
        screen.blit(self.lvlsman, (self.x, self.y))
        #movement
        if moving_left:
            self.x += 3
        if moving_right:
            self.x -= 3
        if moving_down:
            self.y -= 3
        if moving_up:
            self.y += 3
        if self.x > 3500:
            self.x = -50
            self.y = random.randint(10, screen_height - 10)
        if self.x < -3500:
            self.x = screen_width + 50
            self.y = random.randint(10, screen_height - 10)
        if self.y > 3500:
            self.y = -50
            self.x = random.randint(10, screen_width - 10)
        if self.y < -3500:
            self.y = screen_height + 50
            self.x = random.randint(10, screen_width - 10)

    def lvlup(self):
        lvl_ui = font.render(f"lvl: {self.lvl}", True, (0, 0, 0))
        lvl_text = sell_font.render("press 'r' (100 coins = 1 lvl)", True, (0, 0, 0))
        lvl_text_spot = (self.x - 30, self.y + 170)
        lvl_ui_spot = (715, 70)
        screen.blit(lvl_ui, lvl_ui_spot)
        can_lvl = False
        if coi.rock_qty >= 100:
            can_lvl = True
        if player.player_rect.colliderect(self.lvlsman_rect):
            screen.blit(lvl_text, lvl_text_spot)
            if can_lvl == True:
                key = pygame.key.get_pressed()
                if key[pygame.K_r]:
                    lvl_sfx.play()
                    coi.rock_qty -= 100
                    self.lvl += 1
                    can_lvl = False


lvlupsman = Lvlhere(200, 400, 0.06)

def collect_rs(is_looting):
    if player.player_rect.colliderect(rs1.rockspot_rect) or player.player_rect.colliderect(rs2.rockspot_rect) \
     or player.player_rect.colliderect(rs3.rockspot_rect):
        is_looting = True
        font1 = pygame.font.SysFont('bahnschrift', 50)
        press_e = font1.render("hold 'e'", True, (0, 0, 0))
        screen.blit(press_e, (325, 400))

#        if pygame.K_e == True:
#        lb.bar_index += 0.1
#        lb.bar_index += lb.framerate
 #       if self.bar_index >= 7:
 #           is_looting = False
 #           self.bar_index = 0

#    lb.loot_bar = lb.lootbar_animationlist[int(lb.bar_index)]
#    lb.loot_bar = pygame.transform.scale(lb.loot_bar, (200, 100))
 #   screen.blit(lb.loot_bar, lb.loot_bar_rect)

####
run = True
while run:

    clock.tick(fps)
    pygame.draw.rect(screen, 'white', player.player_rect)
    pygame.draw.rect(screen, 'white', rs1.rockspot_rect)
    pygame.draw.rect(screen, 'white', rs2.rockspot_rect)
    pygame.draw.rect(screen, 'white', rs3.rockspot_rect)
    screen.fill('lightgreen')
   # nbk_ost.play(-1)
    #grass
    spot1.draw()
    spot1.move()
    spot1.grass_oob()
    spot2.draw()
    spot2.move()
    spot2.grass_oob()
    spot3.draw()
    spot3.move()
    spot3.grass_oob()
    spot4.draw()
    spot4.move()
    spot4.grass_oob()
    spot5.draw()
    spot5.move()
    spot5.grass_oob()
    spot6.draw()
    spot6.move()
    spot6.grass_oob()
    spot7.draw()
    spot7.move()
    spot7.grass_oob()
    spot8.draw()
    spot8.move()
    spot8.grass_oob()
    spot9.draw()
    spot9.move()
    spot9.grass_oob()

    
    #rockspots
    rs1.draw_rs()
    rs2.draw_rs()
    rs3.draw_rs()
    the_trader.draw_trader()
    lvlupsman.draw()
    lvlupsman.lvlup()
 #   lvlup()
    lb.draw_lootbar(is_looting)
    
    amethyst.mineral_ui()
    ameth.draw_text()
    coal.mineral_ui()
    co.draw_text()
    diamond.mineral_ui()
    diam.draw_text()
    jade.mineral_ui()
    jad.draw_text()
    quartz.mineral_ui()
    quart.draw_text()
    topaz.mineral_ui()
    topa.draw_text()
    coin.mineral_ui()
    coi.draw_text()
    #lvl ui
 #   screen.blit(lvl_ui, lvl_ui_spot)

    text_scroll()
 #   lb.draw_lootbar()
#    lb.draw_lootbar()


    player.move(moving_left, moving_right, moving_up, moving_down, bottom_left, bottom_right, top_left, top_right, 0.10)
    collect_rs(is_looting)
    am_ui.ui_move()
    co_ui.ui_move()
    di_ui.ui_move()
    ja_ui.ui_move()
    qu_ui.ui_move()
    to_ui.ui_move()
    coi_ui.ui_move()
    tr1_ui.ui_move()
    tr2_ui.ui_move()
 #   collected()
 #   idk()
    roll_the_dice()
    the_trader.make_sell()
#    make_sell()
    
    if pause_state == 1:
        screen.blit(pause, pause_dest)
  #  if pause_state == 0 and lb.bar_index < 7:
 #       nbk_ost.play(-1)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True


            if event.key == pygame.K_ESCAPE:
                pause_state += 1
                if pause_state > 1:
                    pause_state = 0
                    

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False
            if event.key == pygame.K_e:
            #    if lootable == True:
                is_looting = False
                lb.bar_index = 0


    pygame.display.flip()
    
pygame.quit()
if __name__ == '__main__':
    main()
    

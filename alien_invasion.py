import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as fg
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)

    #创建一艘飞船,一个子弹编组，一个外星人编组
    ship = Ship(ai_settings,screen)
    """#创建一个外星人
    #alien = Alien(ai_settings,screen)
    #创建一个用于存储子弹的编组 """
    
    bullets = Group()
    aliens = Group()
    play_button = Button(ai_settings,screen,"Play")

    #创建外星人群
    fg.create_fleet(ai_settings,screen,ship,aliens)

    #创建存储游戏统计信息的实例，并创建记分牌
    sb = Scoreboard(ai_settings,screen,stats)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标的事件
        fg.check_events(ai_settings,screen,stats,play_button,ship,sb,aliens,bullets)
        if stats.game_active :
            ship.update()
            fg.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            fg.update_aliens(ai_settings,stats,screen,ship,sb,aliens,bullets)
            
        fg.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)








run_game()

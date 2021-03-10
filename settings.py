class Settings():
    """存储外星人入侵的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #速度
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_firection为1表示向右移动，为1表示向左移
        self.fleet_direction = 1

        #子弹设置
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10
        
        
        #外星人设置
        
        self.alien_dorp_speed = 5
        #外星人点数的提高速度
        self.score_scale =1.5
        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        #飞船设置
        
        self.ship_limit = 3


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.alien_points = 50
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_firection为1表示向右移动，为1表示向左移
        self.fleet_direction = 1


    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

        

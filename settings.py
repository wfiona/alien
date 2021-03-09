class Settings():
    """存储外星人入侵的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        

        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        
        
        #外星人设置
        self.alien_speed_factor = 1
        self.alien_dorp_speed = 10
        #fleet_firection为1表示向右移动，为1表示向左移
        self.fleet_direction = 1

        #飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

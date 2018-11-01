class Settings():
    """存储所有设置的类"""
            
    def __init__(self):
        """初始化设置"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        
        #飞船设置
        self.ship_speed_factor = 0.5
        self.ship_limit = 1
        
        #子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10
        
        #外星人设置
        self.fleet_drop_speed = 20

        #以什么样的速率加快游戏节奏
        self.speedup_scale = 1.1
        #外星人点数的提高
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏动态变化的参数"""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.6

        #fleet_direction 为1表示向右移，-1表示左移
        self.fleet_direction = 1

        #计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)

        
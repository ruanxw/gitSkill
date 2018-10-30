class Settings():
    """存储所有设置的类"""
            
    def __init__(self):
        """初始化设置"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        
        #飞船设置
        self.ship_speed_factor = 0.5
        
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10

        #外星人设置
        self.alien_speed_factor = 0.6
        self.fleet_drop_speed = 20
        #fleet_direction 为1表示向右移，-1表示左移
        self.fleet_direction = 1


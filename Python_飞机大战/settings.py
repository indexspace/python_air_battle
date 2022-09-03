class Settings:
    """储存游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (130, 180, 255)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_allowed = 5
        self.intensified_bullet_switch = True

        # 外星人设置
        self.try_alien_number = 15
        self.fleet_drop_speed = 10

        # 等级设置
        self.speedup_scale = 1.06

        self.score_scale = 1.2

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5

        # 记分
        self.alien_points = 1

        # fleet_direction为1则右移，-1则左移
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


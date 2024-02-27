class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (173, 216, 230)
        self.ship_limit= 3
        self.bullet_speed = 15
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 10
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_speed = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        #Alien Bomb settiings
        self.bomb_speed = 5
        self.bomb_width = 15
        self.bomb_height = 15  
        self.bomb_color = (139, 0, 0)
        self.bombs_allowed = 3
        

    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.bullet_speed = 6
        self.alien_speed = 1
        self.fleet_direction = 1
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale 
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
 
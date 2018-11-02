import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    #"""ÏÔÊ¾µÃ·ÖĞÅÏ¢µÄÀà"""

    def __init__(self, ai_settings, screen, stats):
        #"""³õÊ¼»¯ÏÔÊ¾µÃ·ÖÉæ¼°µÄÊôĞÔ"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #ÏÔÊ¾µÃ·ÖĞÅÏ¢Ê±Ê¹ÓÃµÄ×ÖÌåÉèÖÃ
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #×¼±¸µÃ·Ö³õÊ¼Í¼Ïñ ×î¸ßµÃ·ÖÍ¼Ïñ
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        #'''½«µÃ·Ö×ª»»ÎªÒ»¸±äÖÈ¾µÄÍ¼Ïñ'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                self.ai_settings.bg_color)

        #½«µÃ·Ö·ÅÔÚÆÁÄ»ÓÒÉÏ½Ç
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        #½«×î¸ßµÃ·Ö×ª»»ÎªäÖÈ¾µÄÍ¼Ïñ
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.ai_settings.bg_color)

        #½«×î¸ßµÃ·Ö·ÅÔÚÆÁÄ»¶¥¶ËÖĞÑë
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """å°†ç­‰çº§è½¬ä¸ºæ¸²æŸ“å›¾åƒ"""
        self.level_image = self.font.render(str(self.stats.level), True,
                                self.text_color, self.ai_settings.bg_color)
        #å°†ç­‰çº§æ”¾åœ¨åˆ†æ•°çš„ä¸‹æ–¹
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """æ˜¾ç¤ºè¿˜å‰©ä½™å¤šå°‘é£èˆ¹"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

        
    def show_score(self):
        #"""ÔÚÆÁÄ»ÉÏÏÔÊ¾µÃ·Ö"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        

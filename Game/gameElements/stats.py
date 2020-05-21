import pygame
from Game.gameElements.sprite import sprite

class stats(sprite):
    FONT = None
    FONTCOLOR = pygame.Color(255, 255, 255)
    HEALTHFONTCOLOR = pygame.Color(102, 255, 102)
    FATIGUEFONTCOLOR = pygame.Color(102, 153, 255)
    BGCOLOR = pygame.Color(128, 103, 59)
    MARGIN = 20
    TXTSPACING = 14
    
    def __init__(self, x, y, w):
        super().__init__(x + stats.MARGIN//2, y, w - stats.MARGIN, 200)
        if(stats.FONT == None):
            stats.FONT =pygame.font.SysFont('Courier New', 14)
        self.cleanFields()

    def cleanFields(self):
        self.title = stats.FONT.render("Stats( )", True, stats.FONTCOLOR)
        self.hp = stats.FONT.render("HP: ", True, stats.HEALTHFONTCOLOR)
        self.fatigue = stats.FONT.render("Fatigue: ", True, stats.FATIGUEFONTCOLOR)
        self.move = stats.FONT.render("Move: ", True, stats.FONTCOLOR)
        self.attack = stats.FONT.render("Attack: ", True, stats.FONTCOLOR)
        self.defense = stats.FONT.render("Defense: ", True, stats.FONTCOLOR)
        self.skill = stats.FONT.render("Skill: ", True, stats.FONTCOLOR)
        self.speed = stats.FONT.render("Speed: ", True, stats.FONTCOLOR)
        self.xp = stats.FONT.render("XP:", True, stats.FONTCOLOR)

    def setUnit(self, unit):
        if(unit.isEnemy): self.txtTitle = "Stats(Enemy)"
        else: self.txtTitle = "Stats(Ally)"
        self.title = stats.FONT.render(self.txtTitle, True, stats.FONTCOLOR)
        self.hp = stats.FONT.render("HP:       " + str(unit.HP) + "/" + str(unit.MaxHP), True, stats.HEALTHFONTCOLOR)
        self.fatigue = stats.FONT.render("Fatigue:  " + str(unit.fatigue) + "/" + str(unit.maxFatigue), True, stats.FATIGUEFONTCOLOR)
        self.move = stats.FONT.render("Move:     " + str(unit.Movement), True, stats.FONTCOLOR)
        self.attack = stats.FONT.render("Attack:   " + str(unit.Attack), True, stats.FONTCOLOR)
        self.defense = stats.FONT.render("Defense:  " + str(unit.Defense), True, stats.FONTCOLOR)
        self.skill = stats.FONT.render("Skill:    " + str(unit.Skill), True, stats.FONTCOLOR)
        self.speed = stats.FONT.render("Speed:    " + str(unit.Speed), True, stats.FONTCOLOR)
        self.xp = stats.FONT.render("XP:       " + str(unit.XP), True, stats.FONTCOLOR)

    def draw(self):
        self.drawSquare(stats.BGCOLOR)
        self.screen.blit(self.title, (self.rect.x + 10, self.rect.y + stats.TXTSPACING))
        self.screen.blit(self.hp, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*2))
        self.screen.blit(self.fatigue, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*3))
        self.screen.blit(self.move, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*4))
        self.screen.blit(self.attack, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*5))
        self.screen.blit(self.defense, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*6))
        self.screen.blit(self.skill, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*7))
        self.screen.blit(self.speed, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*8))
        self.screen.blit(self.xp, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*9))

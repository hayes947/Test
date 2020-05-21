import pygame
from Game.gameElements.sprite import sprite
import random
class levelUp(sprite):
    FONT = None
    FONTCOLOR = pygame.Color(255, 255, 255)
    STATUP = pygame.Color(204, 153, 255)
    BGCOLOR = pygame.Color(128, 103, 59)
    MARGIN = 20
    TXTSPACING = 20
    
    def __init__(self, x, y, w):
        super().__init__(x + stats.MARGIN//2, y, w - stats.MARGIN, 300)
        if(stats.FONT == None):
            stats.FONT =pygame.font.SysFont('Courier New', 20)
        self.statGains()

    def statGains(self, unit):
        self.title = stats.FONT.render("LEVEL UP", True, stats.STATUP)
        self.hp = stats.FONT.render("HP:       " + str(unit.MaxHP), True, stats.FONTCOLOR)
        self.fatigue = stats.FONT.render("Fatigue:  " + str(unit.maxFatigue), True, stats.FONTCOLOR)
        self.move = stats.FONT.render("Move:     " + str(unit.Movement), True, stats.FONTCOLOR)
        self.attack = stats.FONT.render("Attack:   " + str(unit.Attack), True, stats.FONTCOLOR)
        self.defense = stats.FONT.render("Defense:  " + str(unit.Defense), True, stats.FONTCOLOR)
        self.skill = stats.FONT.render("Skill:    " + str(unit.Skill), True, stats.FONTCOLOR)
        self.speed = stats.FONT.render("Speed:    " + str(unit.Speed), True, stats.FONTCOLOR)
        
        rn=random.randint(0,99)
        if(rn<unit.growthRates[0]):
            self.hpGain = stats.FONT.render("+1", True, stats.STATUP)
            unit.MaxHP+=1
        else:
            self.hpGain = stats.FONT.render(" ", True, stats.STATUP)

        rn=random.randint(0,99)
        if(rn<unit.growthRates[1]):
            self.fatigueGain = stats.FONT.render("+1", True, stats.STATUP)
            unit.maxFatigue+=1
        else:
            self.fatigueGain = stats.FONT.render(" ", True, stats.STATUP)

        rn=random.randint(0,99)
        if(rn<unit.growthRates[2]):
            self.moveGain = stats.FONT.render("+1", True, stats.STATUP)
            unit.Movement+=1
        else:
            self.moveGain = stats.FONT.render(" ", True, stats.STATUP)

        rn=random.randint(0,99)
        if(rn<unit.growthRates[3]):
            self.attackGain = stats.FONT.render("+1", True, stats.STATUP)
            unit.Attack+=1
        else:
            self.attackGain = stats.FONT.render(" ", True, stats.STATUP)

        rn=random.randint(0,99)
        if(rn<unit.growthRates[4]):
            self.defenseGain = stats.FONT.render("+1", True, stats.STATUP)
            unit.Defense+=1
        else:
            self.defenseGain = stats.FONT.render(" ", True, stats.STATUP)

        rn=random.randint(0,99)
        if(rn<unit.growthRates[5]):
            self.skillGain = stats.FONT.render("+1", True, stats.STATUP)
            unit.Skill+=1
        else:
            self.skillGain = stats.FONT.render(" ", True, stats.STATUP)

        rn=random.randint(0,99)
        if(rn<unit.growthRates[6]):
            self.speedGain = stats.FONT.render("+1", True, stats.STATUP)
            unit.Speed+=1
        else:
            self.speedGain = stats.FONT.render(" ", True, stats.STATUP)

    def draw(self):
        self.drawSquare(stats.BGCOLOR)
        self.screen.blit(self.title, (self.rect.x + 20, self.rect.y + stats.TXTSPACING))
        self.screen.blit(self.hp, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*2))
        self.screen.blit(self.fatigue, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*3))
        self.screen.blit(self.move, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*4))
        self.screen.blit(self.attack, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*5))
        self.screen.blit(self.defense, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*6))
        self.screen.blit(self.skill, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*7))
        self.screen.blit(self.speed, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*8))

        self.screen.blit(self.hpGain, (self.rect.x + 220, self.rect.y + stats.TXTSPACING*2))
        self.screen.blit(self.fatigueGain, (self.rect.x + 220, self.rect.y + stats.TXTSPACING*3))
        self.screen.blit(self.moveGain, (self.rect.x + 220, self.rect.y + stats.TXTSPACING*4))
        self.screen.blit(self.attackGain, (self.rect.x + 220, self.rect.y + stats.TXTSPACING*5))
        self.screen.blit(self.defenseGain, (self.rect.x + 220, self.rect.y + stats.TXTSPACING*6))
        self.screen.blit(self.skillGain, (self.rect.x + 220, self.rect.y + stats.TXTSPACING*7))
        self.screen.blit(self.speedGain, (self.rect.x + 220, self.rect.y + stats.TXTSPACING*8))


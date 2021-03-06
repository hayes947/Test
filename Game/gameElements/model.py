import json
import pygame
from Game.gameElements.sprite import sprite
from Game.gameElements.map import map
from Game.gameElements.unitMenu import unitMenu
from Game.gameElements.button import button
from Game.gameElements.menu import menu


class model:
    def __init__(self):
        self.sprites = []
        self.run = True
        self.menuSprites = [];
        self.gameSprites = [];
        self.stage = "MENU"

        self.setUpGame()
        self.setUpMenu()
        
        self.selectedTile = None
        self.tileControlledUnit = None
        self.tileDefendingUnit = None

    def setUpGame(self):
        ## Here Loading can be perform
        self.sprites = self.gameSprites
        self.unitMenu = unitMenu(830, 0, 250, 720)
        self.map = map("")
        self.addSprite(self.map)
        self.addSprite(self.unitMenu)
        self.sprites += self.unitMenu.getButtons()
        self.addSprite(self.unitMenu.getStatsSprite())

    def setUpMenu(self):
        self.menu = menu()
        self.menuSprites += self.menu.getButtons()
        self.sprites =  self.menuSprites
        
    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)

    def checkClick(self, x, y):
        if self.stage == "GAME":
            if(self.map.turn == 1):
                for sprt in self.sprites:
                    if(isinstance(sprt, button)):
                        if(sprt.checkClick(x, y)):
                            print(self.unitMenu.action)
                self.selectedTile = self.map.getSelectedTile(x, y)
                if(self.selectedTile != None):
                    if(self.selectedTile.unit != None):
                        self.unitMenu.setUnit(self.selectedTile.unit)
                        if(self.tileControlledUnit == None):
                            #Tile can only be controlled if ally or controll unit is empty
                            if(not self.selectedTile.unit.isEnemy):
                                self.tileControlledUnit =  self.selectedTile
                                self.tileControlledUnit.selected = True
                                self.unitMenu.action = ""
                        elif(not self.selectedTile.unit.isEnemy):
                            self.tileControlledUnit.selected = False
                            self.tileControlledUnit =  self.selectedTile
                            self.tileControlledUnit.selected = True
                            self.unitMenu.action = ""
                        else:
                            if(self.unitMenu.action == "A"):
                                #Check: is the enemy in range?
                                unitX=self.tileControlledUnit.getCIndex()
                                unitY=self.tileControlledUnit.getRIndex()
                                print("UnitX=", unitX)
                                print("UnitY=", unitY)
                                unitMov=self.tileControlledUnit.unit.Movement
                                self.map.constructRangeTable(unitY,unitX,unitMov)
                                EnemyX=self.selectedTile.getCIndex()
                                EnemyY=self.selectedTile.getRIndex()
                                print("EnemyX=", EnemyX)
                                print("EnemyY=", EnemyY)
                                for i in range(10):
                                    print(self.map.atkRangeTable[i])
                                if(self.map.atkRangeTable[EnemyY][EnemyX]==1):
                                    #Enemy can only be selected if action == Attack
                                    self.tileDefendingUnit = self.selectedTile
                                    self.map.combat(self.tileControlledUnit.getRIndex(),
                                                self.tileControlledUnit.getCIndex(),
                                                self.tileDefendingUnit.getRIndex(),
                                                self.tileDefendingUnit.getCIndex())
                                    #Hayce: self.map.attack(self.tileControlledUnit, self.tileDefendingUnit)
                                    #Attack successfully performed (Turn ends)
                                    self.tileControlledUnit.selected = False
                                    self.unitMenu.action = None
                                    self.tileControlledUnit = None
                                    self.map.endTurn();
                                else:
                                    print("Target is out of range")
                                self.map.clearRangeTables()
                            else:
                                print("Action can't be performed")
                    elif(self.tileControlledUnit != None and self.unitMenu.action == "W"):
                        #Check if unit can move to selected tile NOT DONE
                        unitX=self.tileControlledUnit.getCIndex()
                        unitY=self.tileControlledUnit.getRIndex()
                        print("UnitX=", unitX)
                        print("UnitY=", unitY)
                        unitMov=self.tileControlledUnit.unit.Movement
                        self.map.constructRangeTable(unitY,unitX,unitMov)
                        
                        #Moving to tile
                        print("Setting Unit")
                        newUnitX=self.selectedTile.getCIndex()
                        newUnitY=self.selectedTile.getRIndex()
                        if(self.map.rangeTable[newUnitY][newUnitX]==1):
                            self.selectedTile.setUnit(self.tileControlledUnit.unit)
                            print("Unit succesfully set")
                            self.tileControlledUnit.selected = False
                            self.tileControlledUnit.unit = None
                            self.tileControlledUnit = None
                        self.map.clearRangeTables()
            else: #Computer turn
                #Makes the game crash: self.map.enemyAIUnitSelect()
                pass
        else: ## Menu is running
            for sprt in self.sprites:
                if (isinstance(sprt, button)):
                    if(sprt.checkClick(x, y)):
                        if(self.menu.action == "G"):
                            self.stage = "GAME"
                            self.sprites = self.gameSprites
                        elif(self.menu.action == "Q"):
                            self.quitGame()
    def quitGame(self):
        self.run = False
        
    def loadGame(self):
        pass

    def saveGame(self):
        pass

    def update(self):
        # Makes button clicking animation work
        for button in self.unitMenu.getButtons():
            button.update()

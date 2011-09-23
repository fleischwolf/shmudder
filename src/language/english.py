#!/usr/bin/python

from language.universal import Context
from basic.actions import *
from basic.exceptions import *

#    This file is part of Shmudder.
#
#    Shmudder is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Shmudder is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Shmudder.  If not, see <http://www.gnu.org/licenses/>.


class CharacterChoiceContext (Context):

    def __init__ (self):
        Context.__init__(self)
        
        self.addSemantics("choose (.+)", chooseCharacter)
        self.addSemantics("info (.+)", showCharacterChoiceInfo)
        self.addExceptionHandling(UnknownAction, "What ?")
        self.addExceptionHandling(UnknownPlayerType, "There is no such character type")

class LoginContext (Context):
    
    def __init__ (self):
        Context.__init__(self)
        self.addSemantics("new", register)
        self.addSemantics("(.+)", login)
        self.addExceptionHandling(UnknownPlayer, "Never heard of you. What's your name?")

class PasswordContext (Context):
    
    def __init__ (self):
        Context.__init__(self)
        self.addSemantics("(.+)", password)
        self.addExceptionHandling(BadPassword, "Wrong password")

class NameChoiceContext (Context):
    
    def __init__(self):
        Context.__init__(self)
        self.addSemantics("([a-zA-Z0-9]+)", chooseName)
        self.addExceptionHandling(PlayerExists, "This name already exists")
        self.addExceptionHandling(UnknownAction, "Player names may only contain letters and numbers")

class PasswordChoiceContext (Context):
    
    def __init__(self):
        Context.__init__(self)
        self.addSemantics("(.+)", choosePassword)
        

class BasicContext (Context):
    
    def __init__ (self):
        Context.__init__(self)
        
        self.addSemantics("(east)",walk)
        self.addSemantics("(west)",walk)
        self.addSemantics("(north)",walk)
        self.addSemantics("(south)",walk)
        
        self.addSemantics("(northeast)",walk)
        self.addSemantics("(northwest)",walk)
        self.addSemantics("(southeast)",walk)
        self.addSemantics("(southwest)",walk)
        
        self.addSemantics("(up)",walk)
        self.addSemantics("(down)",walk)
        
        ######################################################
        
        self.addSemantics("take (.+)",take)
        self.addSemantics("throw (.+) away",throwAway)
        self.addSemantics("use (.+)",use)
        self.addSemantics("put (.+) away",unuse)
        self.addSemantics("put (.+) in (.+)",putInto)
        self.addSemantics("take (.+)",takeOut)
    
        ######################################################
        
        self.addSemantics("inv",showInventory)
        self.addSemantics("info",showInfo)
        
        self.addSemantics("look around",showRoom)
    
        self.addSemantics("examine (.+)",examine)
        self.addSemantics("ex (.+)",examine)
        
        self.addSemantics("give ([a-zA-Z]+) ([a-zA-Z]+)",giveTo)
        
        #self.addSemantics("say (.+)",say)
        #self.addSemantics("shout (.+)",shout)
        #self.addSemantics("say (.+) to (.+)",sayTo)
        
        self.addSemantics("sleep",logout)
        
        self.addSemantics("kill (.+)",kill)
        
        
        #################################################################
        
        self.addExceptionHandling(UnknownAction, "What?")
        self.addExceptionHandling(ImpossibleAction, "This is impossible")
        self.addExceptionHandling(ImprovementNotAllowed, "Not enough attribute points")
        self.addExceptionHandling(CharacterNotFound, "Nobody called by this name is here")
        self.addExceptionHandling(NoSuchDirection, "There is no such direction")
        self.addExceptionHandling(AmbigousDirection, "You are not sure, where to go")
        self.addExceptionHandling(DetailNotFound, "You don't see anything like that")
        self.addExceptionHandling(ItemNotFound, "You can't see an item like that")
        self.addExceptionHandling(ItemNotInUse, "You don't use an item like that")
        self.addExceptionHandling(UnusableItem, "You can't use this times")
        self.addExceptionHandling(NotABin, "This is not a bin")
        self.addExceptionHandling(UnsuitableBin, "You can't put that in there")
        self.addExceptionHandling(ItemReceiverNotFound, "Nobody called by this name is here")
        self.addExceptionHandling(UnsuitableItem, "You can't put that in there")
        self.addExceptionHandling(UnsupportedUseAlias, "This is the wrong way to use this item")
        self.addExceptionHandling(UnsupportedUnuseAlias, "You can't put that item away like that")
        self.addExceptionHandling(CantAttackThisCharacter,"You can't attack this character")


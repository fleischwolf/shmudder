from abstract.causality import Signal, SignalEmitter, SignalListener
from basic.items import ReusableItem
from basic.rooms import Room
from engine.ormapping import Reference, Integer

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


class LightIntensityChange (Signal):
    
    def __init__ (self):
        Signal.__init__(self)
        self.intensity = 0
        
class LightSource (ReusableItem, SignalEmitter):
    
    __class_table__ = "LightSource"
    lightintensity = Integer()
    
    def __init__ (self):
        ReusableItem.__init__(self)
        SignalEmitter.__init__(self)
        self.lightintensity = 0
    
    def use (self, actor):
        ReusableItem.use(self, actor)
        light = LightIntensityChange()
        light.intensity = self.lightintensity
        self.emit(light)
    
    def emitEntrySignal (self):
        if self.isInUse():
            light = LightIntensityChange()
            light.intensity = self.lightintensity
            self.emit(light)
            
    def emitExitSignal(self):
        if self.isInUse():
            light = LightIntensityChange()
            light.intensity = - self.lightintensity
            self.emit(light)
        
    def unuse (self, actor):
        ReusableItem.unuse(self, actor)
        light = LightIntensityChange()
        light.intensity = - self.lightintensity
        self.emit(light)
        

class LightIntensityListener (SignalListener):
    
        
    """ 
    @author: Fabian Vallon
    @license: U{GPL v3<http://www.gnu.org/licenses/>}
    @version: 0.1
    @since: 0.1
    
    Listens to LightIntensityChange signals and saves
    the current light intensity
    """
    
    __class_table__ = "LightIntensityListener"
    intensity = Integer()
    
    
    def __init__ (self):
        SignalListener.__init__(self)
        self.intensity = 0
        
    def signalReceived (self,signal):
        if isinstance(signal,LightIntensityChange):
            self.intensity += signal.intensity
    


        
class IlluminatedRoom (Room):
    
    
        
    """ 
    @author: Fabian Vallon
    @license: U{GPL v3<http://www.gnu.org/licenses/>}
    @version: 0.1
    @since: 0.1
    
    Implements light intensity changing. IlluminatedRooms
    interact with items, that derive from LightSource
    """
    
    __class_table__ = "IlluminatedRoom"
    
    lil = Reference()
    
    def __init__ (self):
        Room.__init__(self)
        li = LightIntensityListener()
        self.lil = li
        self.addListener(li)
        
    def getLightIntensity(self):
        return self.lil.intensity
    
    lightintensity = property(fget=getLightIntensity,doc="Rooms light intensity as an int")
    
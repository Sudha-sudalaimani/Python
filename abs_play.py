#Create interface Playable (method play()). Implement in Football, Cricket.
from abc import ABC,abstractmethod
class playable(ABC):
    @abstractmethod
    def play(self):
        pass
class football(playable):
    def play(self):
        print('Playing Football')
class cricket(playable):
    def play(self):
        print("Playing Cricket")
f=football()
f.play()
c=cricket()
c.play()

from .persistence import Persistence

class Entity:

    _p = Persistence 

    def save(self):
        self._p.save(self)

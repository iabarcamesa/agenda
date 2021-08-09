from app.entities.entity import Entity
from app.entities.persistence import Persistence as p

def test_save_entity():

    p.flush()

    e_1 = Entity()
    e_1.name = 'e_1'

    e_1.save()

    result = p.find(Entity, key=lambda e: e.name=='e_1')

    assert len(result) == 1
    assert result[0].name == 'e_1'
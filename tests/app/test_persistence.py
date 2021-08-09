from app.entities.persistence import Persistence

class Test:
    pass

def test_persistence():

    p = Persistence

    p.flush()

    t_1 = Test()
    t_1.name = 't_1'
    t_1.value_1 = 1
    t_1.value_2 = 2

    t_2 = Test() 
    t_2.name = 't_2'
    t_2.value_1 = 2
    t_2.value_2 = 2

    p.save(t_1)
    p.save(t_2)

    result = p.find(Test, key=lambda t: t.value_1==1 or t.value_2==2)

    assert result[0].name == 't_1'
    assert result[1].name == 't_2'

def test_uniq_id():

    p = Persistence

    p.flush()

    t_1 = Test()
    t_1.name = 't_1'
    t_1.value_1 = 1
    t_1.value_2 = 2


    p.save(t_1)

    read_t_1 = p.find(Test, key=lambda t: t.name=='t_1')[0]

    assert read_t_1.name == 't_1'
    assert read_t_1.value_1 == 1
    assert read_t_1.value_2 == 2

    read_t_1.value_2 = 4
    p.save(read_t_1)

    result = p.find(Test, key=lambda t: t.name=='t_1')

    assert len(result) == 1
    assert result[0].name == 't_1'
    assert result[0].value_1 == 1
    assert result[0].value_2 == 4

import pickle
import os
from copy import deepcopy

class Persistence:

    @classmethod
    def find(cls, entity_class, key=lambda e: True, *args, **kwargs):
        entity_class_data = cls.__get_data().get(entity_class.__name__, [])
        result = []
        for element in entity_class_data:
            if key(element):
                result.append(deepcopy(element))
        return result

    @classmethod
    def save(cls, entity):
        _id = getattr(entity, '_id', None)
        entity_name = type(entity).__name__
        entity_class_data = cls.__get_data().get(entity_name, [])

        if _id is None:
            _id = cls.__get_next_index()
            entity._id = _id
        else:
            for index, element in enumerate(entity_class_data):
                if element._id == _id:
                    del entity_class_data[index]        

        entity_class_data.append(deepcopy(entity))
        cls.__set_data(entity_name, entity_class_data)

    @classmethod
    def flush(cls):
        if os.path.exists(os.path.join('data', 'persistence.pkl')):
            os.remove(os.path.join('data', 'persistence.pkl'))

    @classmethod
    def __get_next_index(cls):
        data = cls.__load_persistence_file()
        data['_global_index'] += 1
        cls.__save_persistence_file(data)
        return data['_global_index']

    @classmethod
    def __get_data(cls):
        data = cls.__load_persistence_file()
        return data

    @classmethod
    def __set_data(cls, key, value):
        data = cls.__load_persistence_file()
        data[key] = value
        cls.__save_persistence_file(data)

    @staticmethod
    def __or_match_args(element, kwargs):
        for key, value in kwargs.items():
            if getattr(element, key) == value:
                return True
        return False

    @staticmethod
    def __element_class_name(element):
        return type(element).__name__

    @staticmethod
    def __load_persistence_file():

        if not os.path.exists('data'):
            os.makedirs('data')

        try:
            p_file = open(os.path.join('data', 'persistence.pkl'), 'rb')
        except FileNotFoundError:
            persisted_data = {'_global_index': 0}
            Persistence.__save_persistence_file(persisted_data)
            p_file = open(os.path.join('data', 'persistence.pkl'), 'rb')
        persisted_data = pickle.load(p_file)
        p_file.close()
        global_index = persisted_data.get('_global_index', None)
        if global_index is None:
            persisted_data['_global_index'] = 0
        return persisted_data

    @staticmethod
    def __save_persistence_file(persisted_data):
        p_file = open(os.path.join('data', 'persistence.pkl'), 'wb+')
        pickle.dump(persisted_data, p_file)
        p_file.close()

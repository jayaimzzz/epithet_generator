
import pytest
import json
from  backend_epithet_generator.app import app

app.config['TESTING'] = True

def test_app_index_success():
    result = app.test_client().get('/')
    data = result.data.decode()
    dict_ = json.loads(data)
    assert result.status_code == 200
    assert isinstance(data, str)
    assert isinstance(dict_, dict)
    assert 'epithets' in dict_
    assert len(dict_['epithets']) == 1


def test_app_vocabulary_success():
    result = app.test_client().get('/vocabulary')
    data = result.data.decode()
    dict_ = json.loads(data)
    assert result.status_code == 200
    assert isinstance(data, str)
    assert 'vocabulary' in dict_
    assert 'Column 1' in dict_['vocabulary']
    assert isinstance(dict_['vocabulary']['Column 1'], list)
    
def test_app_epithets_quantity_success():
    result = app.test_client().get('/epithets/13')
    data = result.data.decode()
    dict_ = json.loads(data)
    assert result.status_code == 200
    assert isinstance(data, str)
    assert 'epithets' in dict_
    assert len(dict_['epithets']) == 13

def test_app_epithets_random_quantity_success():
    result = app.test_client().get('/randomquantity')
    data = result.data.decode()
    dict_ = json.loads(data)
    assert result.status_code == 200
    assert isinstance(data, str)
    assert 'epithets' in dict_
    

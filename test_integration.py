
import pytest
import json
from  backend_epithet_generator.app import app

app.config['TESTING'] = True

def test_app_index():
    result = app.test_client().get('/')
    data = result.data.decode()
    dict_ = json.loads(data)
    assert result.status_code == 200
    assert isinstance(data, str)
    assert isinstance(dict_, dict)
    assert 'epithets' in dict_
    assert len(dict_['epithets']) == 1
    
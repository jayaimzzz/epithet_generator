from helpers import Vocabulary, EpithetGenerator
import os
import pytest

path_to_data_json = os.path.join("resources","data.json")
data = Vocabulary.read_json(path_to_data_json)
e_gen = EpithetGenerator(path_to_data_json)

def test_read_json_success():
    assert isinstance(data, dict)
    assert "Column 1" and "Column 2" and "Column 3" in data
    assert "Column 4" not in data
    assert "artless" in data.get("Column 1")
    assert "beef-witted" in data.get("Column 2")
    assert "flap-dragon" in data.get("Column 3")

def test_read_json_failure():
    path_to_data_csv = os.path.join("resources", "data.csv")
    with pytest.raises(Exception):
        Vocabulary.read_json(path_to_data_csv)
    with pytest.raises(KeyError):
        data["Column 4"]
    assert len(data) != 2
    assert len(data) != 4
    assert len(data) != 1
    assert "hello" not in data["Column 1"]


def test_get_random_words_success():
    epithet = e_gen.get_random_words()
    epithet_list = epithet.split(" ")
    assert isinstance(epithet, str)
    assert len(epithet_list) == 3
    assert epithet_list[0] in data["Column 1"]
    assert epithet_list[1] in data["Column 2"]
    assert epithet_list[2] in data["Column 3"]

def test_get_random_words_failure():
    with pytest.raises(NameError):
        not_a_epithet_generator.get_random_words()
    

epithets = e_gen.get_epithets(5)

def test_get_epithets_success():
    assert isinstance(epithets, list)
    assert len(epithets) == 5
    assert epithets[0].split(" ")[0] in data.get("Column 1")
    assert epithets[4].split(" ")[2] in data.get("Column 3")

def test_get_epithets_failure():
    with pytest.raises(IndexError):
        epithets[5]
    
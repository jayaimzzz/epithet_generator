from helpers import Vocabulary
import os
import pytest

def test_read_json_success():
    path_to_data_json = os.path.join("resources","data.json")
    data = Vocabulary.read_json(path_to_data_json)
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

    
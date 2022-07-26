import pytest
from main import resources
from os import listdir
import webbrowser

@pytest.fixture
def example_resources():
    return [resources(f"tests\\{file}") for file in listdir("tests") if file.endswith(".csv")]

def test_fileLength(example_resources, tmp_path):
    for rlist in example_resources:
        file = f"{rlist.filename}.tmp"
        rlist.save(file)
        webbrowser.open(file)
        assert all(len(r) == 11 for r in rlist.data), "Error with data length"
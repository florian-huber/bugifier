import os
from ..bugifier import python_script_runner


filename = os.path.join(os.getcwd(), "tests", "example_script.py")


def test_script_runner():
    variable_names = python_script_runner(filename)
    assert variable_names == ["filename", "variable1", "variable2"]

import os
import sys
# sys.path.append("..")
from bugifier.script_runner import python_script_runner


filename = os.path.join(os.getcwd(), "example_script.py")


def test_script_runner():
    python_script_runner(filename)

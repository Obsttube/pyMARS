import pytest
import os
import pathlib

if __name__ == "__main__":
    os.chdir(pathlib.Path.cwd() / 'tests')
    pytest.main()

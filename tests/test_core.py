from dots_editor import core
import os

def test_startup():
    core.Game('test.txt', 'ascii')
    assert True

def test_setenv():
    assert os.environ["SDL_VIDEODRIVER"] == "dummy"

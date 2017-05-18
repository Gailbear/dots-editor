from dots_editor import core

def test_startup():
    core.Game('test.txt', 'ascii')
    assert True

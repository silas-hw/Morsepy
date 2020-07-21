import pytest
from morsepy import Morsepy as mpy

def test_encrypt():

    #check if function works
    assert mpy.encrypt('hello world! 123.') == '.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.-- / .---- ..--- ...-- .-.-.-'

    #check if error is raised when it needs to
    with pytest.raises(ValueError):
        mpy.encrypt('▓')

def test_decrypt():
    #check if function works
    assert mpy.decrypt('.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.-- / .---- ..--- ...-- .-.-.-') == 'hello world! 123.'

    #test if invalid morse character raises error
    with pytest.raises(SyntaxError):
        mpy.decrypt('....--.')
        mpy.decrypt('abcd')


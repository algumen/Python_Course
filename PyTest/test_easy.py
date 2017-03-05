import pytest
#class TestEasyStart():

def summarise(a,b):
    return a+b


def test_easy_start_2x2():
    assert summarise(2, 2)==4


def test_easy_start_2x2_fail():
    assert summarise(2, 2)==5


    #test commit
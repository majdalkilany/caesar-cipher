from caesar_cipher.caesar_cipher import *

def test_encript_shift() : 
    expected = 'yza'
    actual   = encrypt('xyz' , 1)
    assert expected == actual


def test_decript_shift() : 
    expected = 'xyz'
    actual   = decrypt('yza' , 1)
    assert expected == actual


def test_encript_upper_case_handle() : 
    expected = 'yza'
    actual   = encrypt('xyz' , 1)
    assert expected == actual


def test_encript_non_string_handle() : 
    expected = 'yza'
    actual   = encrypt('xy@*z' , 1)
    assert expected == actual




def test_breack_code():
    expected = 'it was the best of times it was the worst of times'
    actual = breack_code('Sd gkc dro locd yp dswoc sd gkc dro gybcd yp dswoc')
    assert expected == actual

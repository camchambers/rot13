import rot13

def test_encrypt_lowercase():
    """Test encrypting a simple word of lowercase letters"""
    output = rot13.encrypt("abc")
    assert output == "nop"
    
def test_encrypt_uppercase():
    """Test encrypting a simple word of uppercase letters"""
    output = rot13.encrypt("ABC")
    assert output == "NOP"
    
def test_encrypt_with_spaces():
    """Test encrypting a phrase with spaces"""
    output = rot13.encrypt("space space")
    assert output == "fcnpr fcnpr"
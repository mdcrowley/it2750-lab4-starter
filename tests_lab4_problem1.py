######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest

test_file = "lab4_problem1"
test_inputs = ['lab4_data_problem1.zip']

def test(monkeypatch, capsys):
    global test_file
    global test_inputs
    try:
        exists = os.path.exists(test_file + '.py')
        assert exists == True
        source = __import__(test_file)
    except:
        sys.exit()
    if len(test_inputs) > 0:
        inputs = iter(test_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Test: Ensure all 20 passwords are stored in the list
    assert len(source.passwords) == 20, "Password list is incomplete"

    source.main()
    captured = capsys.readouterr()
    output = captured.out.split('\n')
    output.pop() # Remove last blank line since split by \n

    tc = unittest.TestCase()

    # Test: Ensure 21 lines of output
    assert len(output) == 21, "Incorrect overall output"
    
    # Test: Ensure charset matches selection
    password_results = '((123456|123456789|qwerty|password|1111111|12345678|abc123|1234567|' + \
                       'password1|12345|1234567890|000000|Iloveyou|1234|1q2w3e4r5t|' + \
                       'Qwertyuiop|123|Monkey|Dragon): Failed)|(123123: Success!)'
    for line in output[1:21]:
        tc.assertRegex(line, '^Password ' + password_results + '$', "Incorrect output for password tests")

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################
######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest
import random

test_file = "lab4_problem2"
test_inputs = ['lab4_data_problem2.csv']

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
    
    list_items = source.csv_sample_data_as_list(test_inputs[0])

    # Test: Ensure there are 50 rows in the data file (header skipped)
    assert len(list_items) == 50, "Input CSV data is incorrect"

    # Add random items to be tested
    test_item_1 = list_items[random.randint(1, 50)]
    test_item_2 = list_items[random.randint(1, 50)]
    test_inputs.append(test_item_1[2])
    test_inputs.append("garbage")
    test_inputs.append(test_item_2[2])
    test_inputs.append("STOP")

    source.main()
    captured = capsys.readouterr()
    output = captured.out.split('\n')
    output.pop() # Remove last blank line since split by \n

    tc = unittest.TestCase()

    # Test: Ensure 4 lines of output
    assert len(output) == 4, "Incorrect overall output"

    # Test: Ensure first test email matches test name
    assert output[1] == test_item_1[0]

    # Test: Ensure failed search returns "Not found"
    assert output[2] == "Not found"

    # Test: Ensure second test email matches test name
    assert output[3] == test_item_2[0]

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################
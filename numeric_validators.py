import string
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

valid_hex_chars = [str(x) for x in range(10)] + list(string.ascii_lowercase)[0:6]
logging.debug(valid_hex_chars)
def is_hex(ui):
	return is_valid(valid_hex_chars, ui)
	
valid_binary_chars = ["0", "1"]
def is_binary(ui):
	return is_valid(valid_binary_chars, ui)
	
valid_decimal_chars = [str(x) for x in range(10)]
def is_decimal(ui):
	return is_valid(valid_decimal_chars, ui)	

def is_valid(vals, ui):
    for char in str(ui).lower():
        if char not in vals:
            return False
    return True
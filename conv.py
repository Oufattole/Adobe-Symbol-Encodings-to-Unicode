import csv
from unicodedata import *
import codecs
class Adobe_Symbol_Encoding_To_Unicode():
    def __init__(self):
        """
        load Adobe symbol to unicode char mapping from txt file
        """
        self.symbol_to_unicode = load_conversion()

    def convert_symbol(self, symbol):
        """
        symbol is a char encoded with adobe symbol encoding,
        
        returns the cooresponding char in unicode if a mapping is found
        otherwise returns the same char
        """
        char = symbol
        hex_char = hex(ord(symbol))[4:]
        # the hex(ord(char)) looks like this "0xf061", I
        # end up taking the two least significant hex digits,
        # so in this case 61. This may have bad consequences
        # but it should be fine
        if hex_char in self.symbol_to_unicode:
            char = self.symbol_to_unicode[hex_char]  
        return char

def load_conversion():
    """
    loads mapping from symbol.txt file
    returns dictionary mapping
    Adobe symbol hex value (str) =>  unicode char (str)
    """
    mapping = {}
    with open('symbol.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        line_count = 0
        for row in csv_reader:
            if len(row) and row[0][0] != "#":
                
                try:
                    unicode_name = row[2][2:]
                    #if python's unicodedata class doesn't know a unicode_name
                    #then the lookup function below fails and we skip it
                    unicode_char = lookup(unicode_name)
                    adobe_hex_value = row[1] #added [1:]
                    mapping[adobe_hex_value] = unicode_char

                except:
                    pass
    return mapping

if __name__ == "__main__":
    text = ""
    decoder = Adobe_Symbol_Encoding_To_Unicode()
    converted = ""
    for char in text:
        converted += decoder.convert_symbol(char)
    print(converted)
    

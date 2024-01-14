#quiz 035

class Convert:
    def __init__(self):
        self.roman_symbols = {
            100: 'C',
            90 : 'XC',
            50: 'L',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def convert_to_romans(self, decimal:int) -> str:
        if decimal > 0 and decimal < 101:
            output=''
            for k,v in self.roman_symbols.items():
                q = decimal//k
                output += q **v
                decimal = decimal%k
        return  output

class Solution:
    def intToRoman(self, dec):
        unit = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousand = ["", "M", "MM", "MMM", "MV"]
        i=dec
        roman = ""
        roman = unit[dec%10]+roman;
        dec/=10
        roman = tens[dec%10]+roman
        dec/=10
        roman = hundreds[dec%10]+roman
        dec/=10
        roman = thousand[dec%10]+roman
        return roman


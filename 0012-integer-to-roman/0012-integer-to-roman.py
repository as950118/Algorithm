class Solution:
    def intToRoman(self, num: int) -> str:
        ret = ""
        while num:
            if num >= 1000:
                ret += "M"
                num -= 1000
            elif num >= 900:
                ret += "CM"
                num -= 900
            elif num >= 500:
                ret += "D"
                num -= 500
            elif num >= 400:
                ret += "CD"
                num -= 400
            elif num >= 100:
                ret += "C"
                num -= 100
            elif num >= 90:
                ret += "XC"
                num -= 90
            elif num >= 50:
                ret += "L"
                num -= 50
            elif num >= 40:
                ret += "XL"
                num -= 40
            elif num >= 10:
                ret += "X"
                num -= 10
            elif num >= 9:
                ret += "IX"
                num -= 9
            elif num >= 5:
                ret += "V"
                num -= 5
            elif num >= 4:
                ret += "IV"
                num -= 4
            else:
                ret += "I"
                num -= 1
        return ret

def Summer(number):
    if not type(number) is int:
        raise TypeError("Only integers are allowed")
    if number == 0:
        return 0
    return number % 10 + Summer(int(number / 10))


# def SummerPlusString(number, V_str = None):
#     if V_str == None:
#         V_str = str(number% 10) + ")"
#         print("None")
#     elif number != 0:
#         V_str = str(number% 10)+'+'+V_str
#         print("Plus")
#
#     if number == 0:
#         V_str ="(=" + V_str
#         print("end")
#         return 0, V_str
#
#     return number % 10 + SummerPlusString(int(number / 10), V_str)[0],SummerPlusString(int(number / 10), V_str)[1]


if __name__ == '__main__':
    number = 2347623
    print(Summer(number))
    #print(SummerPlusString(number))


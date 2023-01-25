
#1 5 42 -376 5 19 5 3 42 2 0

def Sequencer(max_num = None, count = None):
    try:
        print("please insert a number")
        input_num = int(input())

        if input_num == 0:
            return max_num, count

        if max_num == None:
            max_num = input_num
            count = 1

        elif max_num == input_num:
            count += 1

        elif max_num < input_num:
            max_num = input_num
            count = 1

        return Sequencer(max_num, count)

    except:
        print("Wrong input! Please insert a number.")
        #raise TypeError("Wrong input!")


if __name__ == '__main__':

    print(Sequencer())


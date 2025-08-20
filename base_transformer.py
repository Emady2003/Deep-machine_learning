def mapp(mapeble):
    mapeble = str(mapeble).upper()
    mapping = {'0':0, '1':1 , '2':2 ,'3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9 ,'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G':16, 'H':17 ,'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35 }
    return(mapping[mapeble])

def mapprev(mapeble):
    mapping = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
    return(mapping[mapeble])

def format_check_number(full_number):
    
    if "." not in list(full_number):
        listi = list(full_number)
        listi.append('.')
        full_number = ''.join(listi)

    if full_number.count(".") > 1:
        print("number formateition should be correct !")
        main()
    
    str_number = (str(full_number).split("."))
    integer_list = list(str_number[0])
    decimal_list = list(str_number[1])
    return(integer_list,decimal_list)

def format_check_base(number,num_list):
    try:
        number = int(number)
    except ValueError:
        print(" 1 --> number should be integer")
    if number > 36:
        print("the base number should be lower than 36 !")
        main(num_list)
    for item in num_list:
        for i in item:
            if mapp(i) >= number :
                print(" 2--> The number cannot contain characters greater than the base")
                main(num_list)
    return(int(number))
def format_check_goingto_base(number,base,num_list):
    try:
        number = int(number)
    except ValueError:
        print(" 1 --> number should be integer")
    if number == base:
        print("the going to base nmber shouldnt be the same with base !")
        main(num_list)
    if number < 2:
        print("its not possible ")
        main(num_list)
    
    return(int(number))


def integer_10(num_list,base):
    int_10 = 0
    counter = 1
    while counter != len(num_list)+1:
        int_10 = int_10 + num_list[-(counter)]*(base**(counter-1))
        counter += 1
    return(int_10)

def decimal_10(num_list,base):
    dec_10 = 0
    counter = 0
    while counter != len(num_list):
        dec_10 = dec_10 +num_list[counter]/(base**(counter+1))
        counter += 1
    return(dec_10)

def int10_toBase(number,base):
    number_list =[]
    if number//base < base:
            number_list.append(number//base)
    while number >= base:
        number_list.append(number%base)
        if number//base < base:
            number_list.append(number//base)
        number = number//base
    final_list = []
    count = 1
    while count != len(number_list)+1:
        final_list.append(number_list[-count])
        count += 1
    veryfinall_list=[]
    for item in final_list:
        veryfinall_list.append(mapprev(item))
    base_str = ''
    result = base_str + ''.join(map(str, veryfinall_list))
    return(result)

def dec10_toBase(number,base):
    decimal_list =[]
    counter = 0
    while number != 0.0 and counter < 10:
        number = number*base
        if number > 1:
            numberMod = (number//1)
            number = number - numberMod
            decimal_list.append(int(numberMod))
        else :
            decimal_list.append(0)
        counter += 1
    finall_list = []
    for item in decimal_list:
        finall_list.append(mapprev(item))
    base_str = '.'
    result = base_str + ''.join(map(str, finall_list))
    return(str(result))

def main(checked_number=None,):
    if checked_number == None:
        number = input("please enter your number : ")
        checked_number = format_check_number(number)
    base_number = input("please enter your number base : ")
    checked_base = format_check_base(base_number,checked_number)
    going_to_base = input("please enter your number going to base : ")
    checked_going_to_base = format_check_goingto_base(going_to_base,checked_base,checked_number)
    
    integer_num = []
    for item in checked_number[0]:
        integer_num.append(mapp(item))

    decimal_num = []
    for item in checked_number[1]:
        decimal_num.append(mapp(item))
    

        
    int_10 = integer_10(integer_num,checked_base)
    dec_10 = decimal_10(decimal_num,checked_base)

    if checked_going_to_base == 10:
        return(str(int_10) + ''.join(map(str, str(dec_10).lstrip('0'))),None)

    a = int10_toBase(int_10,checked_going_to_base)
    b = dec10_toBase(dec_10,checked_going_to_base)
    print(a)
    print(b)
    if b == '.':
        b = '.0'


    return(a + ''.join(map(str, b)),str(int_10) + ''.join(map(str, str(dec_10).lstrip('0'))))


a , b  = main()
print("number is :",a)
if b != None:
    print("decimall is :",b)
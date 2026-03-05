# ThepiMaleBye Fixing the parameter

## Code
try:
    input_num = int(input("Credit Card Number: "))
except Exception as e:
    print("Credit card number must be numeric", e)

# credit_num=str(input_num)
def Is_Valid_Credit_card(x:str):
    try:
        sum = 0
        parity = len(x) % 2
        i = 0
        for i in range(len(x)-1, -1, -1):
            current = int(x[i])
            if(i + 1) % 2 == parity:
                sum += current
            elif(current > 4):
                sum += 2*current-9
            else:
                sum += 2*current
        return sum % 10 == 0
    except Exception as e:
        print("Credit card number must be numeric", e)

#print(Is_Valid_Credit_card(credit_num))
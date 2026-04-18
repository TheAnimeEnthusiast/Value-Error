try:
    a = int(input("What number do you want as the dividend?"))

    b = int(input("What number do you want as the divisor?"))

    if a%b==0:
        print("It is evenly dividible.")
    else:
        print("It is not divisible.")

except Exception as c:
    print('There was an exception,',c)


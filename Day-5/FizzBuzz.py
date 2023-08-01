for i in range(1, 101):
    isBoth = 0
    if(i % 3 == 0):
        isBoth += 1
    if (i % 5 == 0):
        isBoth += 2
    match isBoth:
        case 0:
            print(i)
        case 1:
            print("Fizz")
        case 2:
            print("Buzz")
        case 3:
            print("FizzBuzz")

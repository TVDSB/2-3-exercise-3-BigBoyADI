def main():
    number = float(input("Enter a number "))

    if number%15 == 0:
       print("fizzbuzz")
    elif number%5 == 0:
       print("buzz")
    elif number%3 == 0:
       print("fizz")
    else:
       print("none of the cases are true")#your code goes here
    print("0")

if __name__ =='__main__':
    main()

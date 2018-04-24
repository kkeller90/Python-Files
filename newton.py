# newtons method
# compute square root of 2

def main():
    print("This program evaluates the square root of 2 using Newton's Method")
    root = 2
    x = eval(input("Enter number of iterations: "))
    for i in range(x):
        root = root - (root**2 - 2)/(2*root)
        print(root)


main()         
             

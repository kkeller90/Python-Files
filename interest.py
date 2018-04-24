# interest.py
# compute compounded interest over 10 years

def main():

    print("Progam to compute compound interest over 10 years")

    principle = eval(input("Enter principle amount? "))
    apr = eval(input("Enter annual percentage rate? "))
    amount = principle

    for i in range(10):
        amount = amount*(1 + apr/100)
        
    print("Total Amount is: ", amount)

main()           

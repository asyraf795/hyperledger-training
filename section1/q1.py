def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1) 
  

while True:
    print("Please input a positive whole number:")
    num = int(input()) 
    print("Factorial("+str(num)+"):", fact(num), "\n")  

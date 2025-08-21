# Problem-2: Print first 'a' odd numbers

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    odd = 2 * i - 1
    print(odd, end="")
    if i < n:   
        print(", ", end="")

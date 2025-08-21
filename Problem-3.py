# Problem-3: Print odd number series depending on even/odd input

n = int(input("Enter a number: "))


if n % 2 == 0:
    limit = n - 1
else:
    limit = n

for i in range(1, limit + 1):
    print(2 * i - 1, end=" ")  
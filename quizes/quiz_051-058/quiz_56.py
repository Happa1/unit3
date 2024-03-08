# code = input(int())
code = 9
binary=""

while code !=1:
    left =str(code%2)
    code=code//2
    binary+=left

binary+=str(code)
binary=binary[::-1]
print(binary)
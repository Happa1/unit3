code = int(input("please enter the number between 1 - 31"))
binary =''

while code!=0:
    left = str (code%2)
    code = code//2
    binary+=left

binary = int(binary[::-1])

action_d ={1:"wink", 10: "double blink", 100: "close your eyes", 1000: "jump"}
digit=0
out=[]

while binary!=0:
    remain = binary % 10
    binary = binary//10
    action_num = remain*10**digit
    digit+=1
    if action_num in action_d:
        out.append(action_d[action_num])
    if action_num == 10000:
        out.reverse()

print(out)
import re
judge = True
print("Enter quit to exit\n")
def calculate(f):
    global judge
    if f=='quit':
        judge = False
    else:
        f = re.sub('[a-zA-Z,\" "]','',f)
        if f == "":
            print("Please try again!")
        else:
            print(eval(f))

while judge:
    f = input(str("Enter your formula : \n"))
    calculate(f)
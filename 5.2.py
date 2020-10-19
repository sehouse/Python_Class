num = 0
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        numb = int(num)
    except :
        print('Invalid input')
    if largest is None :
        largest = numb
    elif smallest is None:
        smallest = numb
    elif largest < numb :
        largest = numb
    elif smallest > numb :
        smallest = numb

print("Maximum is", largest)
print("Minimum is", smallest)

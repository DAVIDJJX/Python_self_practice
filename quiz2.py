name=input('pick up name for file:')
f=open(f'{name}file.txt','w+')
nums = list()
cnt = 1

    # Take in numbers
while True:
    entered = input(f"Enter the {cnt} number, or enter f when you are finished: ")
    cnt += 1

    if entered == 'f' or entered == '':
        break
    else:
        try:
            n = float(entered)
            nums.append(n)
        except ValueError:
            print("The input is not a valid float") 
print(nums,file=f)
f.close()
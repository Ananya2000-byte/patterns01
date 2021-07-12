lines = int(input())
first = 0
last = lines - 1
for i in range(lines):
    if i == first or i == last:
        for j in range(lines):
            print('0', end=" ")
        print("\n")
    else:
        for k in range(lines):
            if k == first or k == last:
                print("0", end=' ')
            else:
                print("1", end=" ")
        print("\n")
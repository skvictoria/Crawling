data = [ 1,2,5,6,43 ]
i = 0
length = len(data)

usr = int(input("그만하고 싶으면 0, 검색은 -를 눌러주세요"))

while(True):
    
    if (usr == 0):
        print("stop")
        break
    elif (usr > 0):
        if (length == 0):
            data.append(usr)
            break
        else:   
            while ( i < length):
                if (data[i] == usr):
                    print('repeated num')
                    break
                elif (data[i] > usr):
                    data.insert(i, usr)
                    break
                else:
                    if (i == length-1):
                        data.append(usr)
                        break
                i = i+1
            break


print(data)

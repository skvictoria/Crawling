lst = [0, 1, 2, 3, 4, 6,7,8,9,24,33,55,66,99]

want = 99
start = 0
end = len(lst)-1

cnts = 0

while(start <=end):
    key = int((start+end)/2)
    cnts = cnts+1
    
    if lst[key]<want:
        start = key+1
    elif lst[key]>want:
        end = key -1
    elif lst[key]==want:
        print('찾았다, ',key+1,'번째에 있습니다')
        break
        

        
print(cnts)

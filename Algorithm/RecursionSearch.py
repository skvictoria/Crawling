lst = [0, 1, 2, 3, 4, 6,7,8,9,24,33,55,66,99]

want = 99 #change this

def search(lst, start, end, want):
    key = int((start + end) / 2)
    if(lst[key] < want):
        return search(lst, key+1, end, want)
    elif(lst[key] > want):
        return search(lst,start, key-1, want)
    elif(lst[key] == want):
        print('찾았다, ',key+1,'번째에 있습니다')
        return key

search(lst, 0, len(lst)-1 , want)

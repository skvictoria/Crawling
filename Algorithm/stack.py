class stack:
    def __init__(self):
        self.arr = []
        if num != None:
            self.arr.append(num)
            
    def push(self, num):
        self.arr.append(num)
        
    def pop(self):
        if len(self.arr)>0:
            return self.arr.pop()
        else:
            print("no data here")

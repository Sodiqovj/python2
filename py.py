class Numbers:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, value):
        return Numbers(self.x + value.x, self.y + value.y)
    
    def __repr__(self):
        return f"X ning qiymati {self.x} va Y ning qiymati {self.y}"
    
n1 = Numbers(20,20)  
n2 = Numbers(20,20)        
n3 = Numbers(20,20)

result = n1 + n2 + n3

print(result)
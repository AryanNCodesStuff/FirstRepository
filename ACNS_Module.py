
"""DATA STRUCTURES:"""
"""Stack"""
class Stack:
    def __init__(self,cap=None):
        self.contents=[]
        self.capacity=cap
    def push(self,x):
            if self.capacity is not None and len(self.contents)>=self.capacity:
                print("Overflow")
                print(self.capacity)
            else:  self.contents.append(x)
    def pop(self):
        if len(self.contents)==0: 
            print("underflow ") 
            return None
        else: 
             return self.contents.pop()  
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.contents[-1]
    def is_empty(self):
        if len(self.contents)==0:return True
        else:return False
    def __len__(self):
        return len(self.contents)
    def isontop(self,x):
        return x==self.peek()
    def __str__(self):
        out=''
        for i in self.contents:
            out+=','+str(i)
        out=out[1:]
        return f"[{out}*]"
    def cap(self):
        return self.capacity
    def __getitem__(self, index):
        return self.contents[index]

    """Queue"""
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,x):
        self.items.append(x)
    def dequeue(self):
        if self.size()==0: return "Underflow"
        else: 
            l,self.items=self.items[0],self.items[1:]
            return l
    def peek(self):
        if self.isempty():
                    print("Stack is empty")
        else: return self.items[0]
    def size(self):
        return len(self.items)
    def isempty(self):
        return self.items==0
    def view(self):
        v=''
        for e in self.items:
            v+=f'{e}<=='
        print(v)
    def __str__(self):
            return '[*' + ', '.join(map(str, self.items)) + ']'
    def empty(self):
        self.items=[]

"""IEEE Converters"""
"""IEEE 64"""
def IEEE64(n):
    if n<0:
        s='1'
        n*=(-1)
    else: s='0'
    e=0
    while n>=2:
        n=n/2
        e+=1
    while n < 1 and n != 0:
        n=n*2
        e-=1
    f,e=n-1,e+1023
    def int2bin(n):
        if n==0: return '0'
        b=''
        while n>0:
            b= str(n%2)+b
            n=n//2
        return b
    def f2bin(n):
        r=''
        c=0
        while n!=0 and c<53:
            n=n*2
            r+=str(int(n))
            n=n-int(n)
            c+=1
        return r
    f=f2bin(f)
    f=f.ljust(52,'0')
    e=int2bin(e)
    e=e.rjust(11,'0')
    return(s,e,f)

"""IEEE 32"""
def IEEE32(n):
    if n<0:
        s='1'
        n*=(-1)
    else: s='0'
    e=0
    while n>=2:
        n=n/2
        e+=1
    while n < 1 and n != 0:
        n=n*2
        e-=1
    f,e=n-1,e+127
    def int2bin(n):
        if n==0: return '0'
        b=''
        while n>0:
            b= str(n%2)+b
            n=n//2
        return b
    def f2bin(n):
        r=''
        c=0
        while n!=0 and c<24:
            n=n*2
            r+=str(int(n))
            n=n-int(n)
            c+=1
        return r
    f=f2bin(f)
    f=f.ljust(23,'0')
    e=int2bin(e)
    e=e.rjust(8,'0')
    return(s,e,f)
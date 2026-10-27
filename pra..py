# a="my name is aryan im testing github"
# for i in a.split():
#     print (i)

# def sam(n):
#     if n<=1:
#         return n
#     return sam(n-1)+n
# print(sam(int(input('number'))))

# def ab(a,b=3):
#     if b<=1:
#         return a
#     return a*ab(a,b-1)

# print(ab(int(input('number'))))

# from array import array
# x=array('l',[2,3,4,5])
# print(type(x), x)

# l=[1,2,3,44,5]
# print(dir(l))

# def rdpo(t):
#     alr=[]
#     ret=''
#     for ch in t:
#         if ch in alr:
#             pass
#         elif ch==' ':
#             ret=ret+ch
#         else:
#             ret=ret+ch
#             alr.append(ch)
#     return ret
# print(rdpo('programming'))
# print(rdpo('mississippi'))

# names = ["Amit", "Ramesh", "Raj", "Priyanka", "Om"]
# print(list(map(lambda x: x.upper(),names)))
# print(list(filter(lambda x: len(x)>4,names)))

# def tag(t, p="[", s="]"):
#     return p + t + s  
# print(tag('python'))
# print(tag('python','<','>'))
# print(tag('python',s='!'))
# print(tag('data','{','}'))

'''
Q Write a recursive function count_char_recursive(text, ch) that counts the number of occurrences of
character ch in text using recursion only, no loops and no .count(). Slicing to shorten the string, e.g., text[1:], is
allowed; ch is exactly one character; the comparison is case-sensitive; and the empty string is the base case, returning 0.
'''
# def ccr(t,ch):
#     if t=='':
#         return 0
#     else:
#         if t[0]==ch:
#             return 1+ccr(t[1:],ch)
#         else: return ccr(t[1:], ch)

'''
Two strings are anagrams of each other if one can be rearranged to form the other — that is, both contain the same
letters, each appearing the same number of times, only in a different order. For example, "eat" and "tea" are anagrams,
whereas "eat" and "tee" are not. Write a function is_anagram(s1, s2) that returns True if two strings are
anagrams of each other, ignoring case and all whitespace. Do not remove other characters; assume the inputs contain
only letters and spaces. 
'''

# print(dir(str))
# def is_anagram(s1,s2):
#     s1=s1.lower().replace(' ','')
#     s2=s2.lower().replace(' ','')
#     l1=list(s1)
#     l2=list(s2)
#     if sorted(l1)==sorted(l2):
#         return True
#     else: return False
# print()

"""
convert integer to binary
"""

b=''
def int2bin(n):
    if n==0: return '0'
    b=''
    while n>0:
        b= str(n%2)+b
        n=n//2
    return b

# def int2bin_bitwise(n):
#     if n==0: return '0'
#     b=''
#     while n>0:
#         b=str(n&1)+b
#         n=n>>1
#     return b

"""
IEEE forms conversion
"""
# def IEEE64(n):
#     if n<0:
#         s='1'
#         n*=(-1)
#     else: s='0'
#     e=0
#     while n>=2:
#         n=n/2
#         e+=1
#     while n < 1 and n != 0:
#         n=n*2
#         e-=1
#     f,e=n-1,e+1023
#     def int2bin(n):
#         if n==0: return '0'
#         b=''
#         while n>0:
#             b= str(n%2)+b
#             n=n//2
#         return b
#     def f2bin(n):
#         r=''
#         c=0
#         while n!=0 and c<53:
#             n=n*2
#             r+=str(int(n))
#             n=n-int(n)
#             c+=1
#         return r
#     f=f2bin(f)
#     f=f.ljust(52,'0')
#     e=int2bin(e)
#     e=e.rjust(11,'0')
#     return(s,e,f)

# t=IEEE64(0.15625)
# print(' '.join(t))


# def IEEE32(n):
#     if n<0:
#         s='1'
#         n*=(-1)
#     else: s='0'
#     e=0
#     while n>=2:
#         n=n/2
#         e+=1
#     while n < 1 and n != 0:
#         n=n*2
#         e-=1
#     f,e=n-1,e+127
#     def int2bin(n):
#         if n==0: return '0'
#         b=''
#         while n>0:
#             b= str(n%2)+b
#             n=n//2
#         return b
#     def f2bin(n):
#         r=''
#         c=0
#         while n!=0 and c<24:
#             n=n*2
#             r+=str(int(n))
#             n=n-int(n)
#             c+=1
#         return r
#     f=f2bin(f)
#     f=f.ljust(23,'0')
#     e=int2bin(e)
#     e=e.rjust(8,'0')
#     return(s,e,f)

# t=IEEE32(0.15625)
# print(' '.join(t))

"""
Write a function remove_duplicates_preserve_order(text) that returns a new string with duplicate
characters removed, keeping only the first occurrence of each character, without using set(), frozenset(),
dict, or dict.fromkeys(); use a list or a string to record the characters already seen. The comparison is
case-sensitive.
Test it on: "programming" and "mississippi", which should give "progamin" and "misp".
"""
# d={}
# def remove_duplicates(text):
#     t=''
#     for ch in text:
#         if ch in d.keys():
#             d[ch]+=1
#         else: 
#             d[ch]=1
#             t+=ch
#     return t
# print(remove_duplicates('mississippi'))

"""
find max using recursion
"""

def find_max(lst):
    if len(lst) == 1:
        return lst[0]

    rest_max = find_max(lst[1:])

    if lst[0] > rest_max:
        return lst[0]
    else:
        return rest_max
print(find_max([3, 7, 2, 9, 4]))

"""count number of occurrences of each character in a string and return the character(s) with the maximum count."""
input = 'Student ID is XX26. The Python (IC152) exam is scheduled on 25/09/2026 at 10:00 AM in ROOM-YY.'
input=input.split(' ')
input=''.join(input)
def count(text):
    d={}
    for ch in text:
        if ch in d.keys():
            d[ch]+=1
        else: 
            d[ch]=1
    r,s=0,[]
    for i in d.keys():
        if d[i]>r:
            r=d[i]
            s.append(i)
    return s
print(count(input))
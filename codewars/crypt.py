'''

Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

decrypt(S, N) 還原 encrypt 

'''
def encrypt(S, N):
    for i in range(N):
        even = [S[i] for i in range(len(S)) if i % 2 == 0]
        odd = [S[i] for i in range(len(S)) if i % 2 == 1]
        S = "".join(odd + even)
        
    return S    

def decrypt(S, N):
    for i in range(N):
        origin = []
        if len(S) % 2 != 0:
            mid = len(S) // 2
        else:
            mid = int(len(S) / 2)     
        print(len(S))
        print(mid)    
        odd = S[:mid]
        even = S[mid:]
        x = 0
        y = 0
        for j in range(len(S)):
            if j % 2 == 1:
                origin.append(odd[x])
                x = x + 1  
            else:
                origin.append(even[y])  
                y = y + 1  
        S = "".join(origin)
        
    return S
         

# test = encrypt("This is a test!", 3)
dep = decrypt("hskt svr neetn!Ti aai eyitrsig", 1)
print(dep)
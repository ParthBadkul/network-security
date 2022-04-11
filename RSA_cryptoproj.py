#Select three unique and large prime numbers 
#Compute n
#Calculate phi(n)
#An integer e is chosen, such that 1<e<f(n) and GCD(e,f(n))=1; e and f(n) are co-primes of each other.
#Compute d as the multiplicative inverse of e mod (f(n))(e*d) mod f(n)=1.
#encrypted text: C=M^e(mod n)
#decrypted text: M=C^d(mod n)

#taking input from the user for 3 prime numbers 

p=int(input("Enter prime 1 \n"))
q=int(input("Enter prime 2 \n"))
r=int(input("Enter prime 3 \n"))

#calculationg n
n=p*q*r
print("n = p * q * r = " + str(n) + "\n")

#calculation Euler's Totient function 
phi=(p-1)*(q-1)*(r-1)
print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")

#function for calculating GCD
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

#euclidian algorithm for calculating GCD
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
    
    
#function for calculating modular inverse   
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        #raise Exception('modular inverse does not exist')
        return -1
    else:
        return x % m
    
    
#function for calculating co-primesand storing it in an array
def coprimes(a):
    l = []
    for x in range(2, a):                                       # for checking that e greater than 1 and less than phi.
        if gcd(a, x) == 1 and modinv(x,phi) != None:            #for checking that gcd of e and phi is 1.
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l


#storing all the co-primes of phi in an array
l=coprimes(phi)

#selecting an integer e which is a co-prime
e=l[int(len(l)//4)]

#calculating d such that it is the multiplicative inverse of (e mod phi)
d=modinv(e,phi)
print(d)

#encrypt function
def encrypt_block(m):
    c = modinv(m**e, n)                             #C=M^e(mod n)
    if c == -1:
        return ord('o')
    return c

#decrypt function
def decrypt_block(c):
    m = modinv(c**d, n)                             #M=C^d(mod n)
    if m == -1:
        return ord('o')
    return m


def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])

#printing public and private key

print("public key = ",e,n)
print("private key= ",d,n)

s = input("Enter a message to encrypt: ")
print("\nPlain message: " + s + "\n")

enc = encrypt_string(s)
print("Encrypted message: " + enc + "\n")

dec = decrypt_string(enc)
print("Decrypted message: " + dec + "\n")

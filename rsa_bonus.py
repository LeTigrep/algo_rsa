import math

def is_prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    
    max_divisor = math.isqrt(n) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True


def euclidien_algorithm(phi,e):
    res_bool=True
    a=phi
    b=e
    while res_bool:
        res=a-((a//b)*b)
        if res==0:
            return b
            break
        a=b
        b=res
        
        
def reverse_euclidien_algorithm(phi,e):
    rest_bool=True
    uv=[]
    u=[]
    v=[]
    a=phi
    b=e
    i=0
    while rest_bool:
        u.append(1)
        v.append((a//b)*(-1))
        rest=(a*u[i]+(v[i]*b))
        if(i==0):
            uv.append((1,v[0]))
        elif(i==1):
            uv.append(((v[1]*uv[0][0]),(v[1]*uv[0][1]+u[1])))
        else:
            uv.append(((uv[i-2][0]*u[i]+uv[i-1][0]*v[i]),(uv[i-2][1]*u[i]+uv[i-1][1]*v[i])))
        if rest ==1:
            rest_bool=False
            return uv[i][1]
            break
        a=b
        b=rest
        i=i+1

   
def key_generation():
  pbool=True
  qbool=True
  while(pbool):
      p=int(input("give a prime number"))
      if is_prime(p):
          pbool=False
  while(qbool):
      q=int(input("give a prime number"))
      if is_prime(q):
          qbool=False
  phi=(p-1)*(q-1)
  e_bool=True
  while e_bool:
     try:
          e=int(input(f"give a integer e>1 and co-prime with {phi} "))
          if e<1:
              print(f"{e} is that not superior to 1 ")
              continue
          elif euclidien_algorithm(e,phi)!=1:
              print(f"{e} and {phi} are not co-prime! ")
              continue
          else:
              e_bool=False
     except:
          print("give an integer please!")
  d=reverse_euclidien_algorithm(phi,e)
  if d<0:
       d=d+phi
  public_key=e,p*q
  private_key=d,p,q
  print(f"your public key is {public_key}")
  print(f"your private key is {private_key}")
  return public_key,private_key



def encryption(M):
    public_key_str = input("give your public key in this format (e n ): ")

    public_key = tuple(map(int, public_key_str.split()))
    
    ciphertext=pow(M,int(public_key[0]),int(public_key[1]))
    
    return ciphertext


def decryption(C):
    private_key_str=input("give your public key in this format (d p q): ")

    private_key = tuple(map(int, private_key_str.split()))
    
    plaintext=pow(C,private_key[0],private_key[1]*private_key[2])
    
    return plaintext



    
                



          

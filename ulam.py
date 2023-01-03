def isprime(n):
  if n < 2:
   return False
  if n == 2 or n == 3:
   return True
  if n % 2 * n % 3 == 0:
   return False
  i = 5
  d = 2
  while i**2 <= n:
   if n % i == 0:
    return False
   i += d
   d = 6 - d
  return True


zp = lambda x: f"*"
L = lambda x,y: (y + abs(x))**2 - x + 1 if y >= 0 else (y-abs(x-1))**2+x

s = lambda x,n : '\033[91m' + zp(x) + '\033[0m' if x % n == 0 else zp(x)
p = lambda x : '\033[91m' + zp(x) + '\033[0m' if isprime(x) else zp(x)

N = 60
print()
for y in range(N,-(N+1),-2):
  print( "\t" + "".join([p(L(x,y)) for x in range(-N,N+1, 2)]) )

 


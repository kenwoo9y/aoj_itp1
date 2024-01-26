import math

a,b,C = map(int, input().split())

rad = math.radians(C)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(rad))

S = 0.5 * a * b * math.sin(rad)
L = a + b + c
h = 2 * S / a

print(f"{S:.8f}", f"{L:.8f}", f"{h:.8f}", sep="\n")
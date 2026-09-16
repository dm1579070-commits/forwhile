X=float(input("Вещественное число: "))
N=int(input("Целое число: "))
total_sum=X
factorial=1.0
sign=-1
for i in range(0,N+1):
   w=2*i+1
   factorial*=w
   c=X**w/factorial
   total_sum+=c
   sign=-sign

print(f"Значение выражения {total_sum}")

def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)

num = 5
res = fact_rec(num)
print("the fact of {} is {}".format(num,res))
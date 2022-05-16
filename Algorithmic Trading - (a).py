def Max_Profit(A):
  min = A[0]
  profit = A[0]-A[1]
  for i in range(1,len(A)):
    if(A[i]-min>profit):
      profit=A[i]-min
    if(A[i]<min):
      min=A[i]
  return profit

print(Max_Profit(A))
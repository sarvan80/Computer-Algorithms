#Verification of the Matrix Multiplication code
T=c(0,0,0)
T1=c(1,1,0)
f=rbind(T,T1)
u1=c(1,1)
u2=c(1,1)
u3=c(0,0)
uf=rbind(u1,u2,u3)
uf
Check=f %*% uf
Check


clear()
C=Entities.Cactus
s=swap
p=plant
M=measure
N=North
E=East
n=100
while n:
	n-=move(N)
	i=till(),n%10 or move(E)
while (p(C),s(N),p(C),s(E),p(C),M()>M(E) and s(E),p(C),M()>M(N) and s(N)):
	harvest()

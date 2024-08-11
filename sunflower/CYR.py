clear()

n=100
s=Entities.Sunflower
p=plant
u=use_item
f=Items.Fertilizer
while n:
	if(till(),p(s),measure()==7)[2]:
		x,n=n%10 or move(East),n-move(North)
while(harvest(),p(s),u(f),u(f)):
	u(f)

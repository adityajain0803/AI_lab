total=3000 

distance=1000 

capacity=1000 

lose=0

start=total

for i in range(distance):

    while start>0:

        start=start-capacity

        if start==1:

            lose=lose-1

        lose=lose+2

    lose=lose-1

    start=total-lose

    if start==0:

        break

print(start)

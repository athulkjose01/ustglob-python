from collections import Counter


n = int(input("input no of shoes: "))
shoe = input("enter shoe sizes: ")
sshoes = shoe.split(",")
shoes = []
for i in sshoes:
    shoes.append(int(i))
countershoes = dict(Counter(shoes))

print(shoes)
print(countershoes)


c = int(input("enter no of customers: "))
sp = []
for i in range(c):
    x = input("enter shoe size and price: ")
    size, price = map(int, x.split(" "))
    for j in shoes:
        if j == size:
            if countershoes[j] > 0:
               countershoes[j] = countershoes[j] - 1
               if countershoes[j] >= 0:
                  sp.append((size, price))
                  print(countershoes)
                  break
            break

print(sp)
    

sum = 0
for i in sp:
    sum = sum + i[1]

print(sum)


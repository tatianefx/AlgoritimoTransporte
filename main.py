factory = 0
transport = 0
artificial_variable = False
matrix = []
offer = []
capacity = []


def read_inputs():
    print('Número de fábricas: ')
    global factory
    factory = int(input())

    print('Número de transportes: ')
    global transport
    transport = int(input())

    for i in range(factory):
        print('Insira a oferta da fábrica {}'.format(i))
        global offer
        offer.append(int(input()))

    for j in range(transport):
        print('Insira a capacidade de escoamento do transporte {}'.format(j))
        global capacity
        capacity.append(int(input()))

    total_offer = sum(offer)
    total_capacity = sum(capacity)

    if total_offer < total_capacity:
        global artificial_variable
        offer.append(total_capacity - total_offer)
        artificial_variable = True
        factory += 1

read_inputs()

# initialize matrix
for x in range(factory):
    row = []
    if artificial_variable and (x == factory - 1):
        for y in range(transport):
            row.append(0)
    else:
        print('Insira os custos da linha {}'.format(x))
        for y in range(transport):
            row.append(int(input()))

    matrix.append(row)

print('Matriz: ')
print(matrix)

print('Oferta: ')
print(offer)

print('Capacidade: ')
print(capacity)

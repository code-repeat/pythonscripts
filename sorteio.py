from random import choices

#  Capa do Programa
print("*"*50)
print("-------------SORTEIO SIMPLES----------------------")
print("*"*50)

quant_names = ''
while type(quant_names) != int:
    print("Quantos nomes deseja adcionar na lista? ")
    quant_names = input()
    try:
        int(quant_names)
        break
    except ValueError:
        print("Somente números")

box_itens = []

for i in range(int(quant_names)):
    item = input(f"Item {i}: ")
    box_itens.append(item)

draw_numbers = ''
while True:
    print("Quantos itens você deseja sortear? ")
    draw_numbers = int(input())
    if draw_numbers > len(box_itens):
        print("Digite um valor menor")
    else:
        break

selected = choices(box_itens, k=int(draw_numbers))
print(', '.join(selected))


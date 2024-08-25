print("Bem vindo a Loja do Bruno Silva.")

valor_unitario = float(input("Entre com o valor do produto: "))
quantidade = int(input("Entre com a quantidade de produtos: "))

valor_total_sem_desconto = valor_unitario * quantidade

if valor_total_sem_desconto < 2500:
    desconto = 0
elif valor_total_sem_desconto < 6000:
    desconto = 4
elif valor_total_sem_desconto < 10000:
    desconto = 7
else:
    desconto = 11

valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto / 100)

print(f"Valor total sem desconto: R$ {valor_total_sem_desconto:.2f}")
print(f"Desconto aplicado: {desconto}%")
print(f"Valor total com desconto: R$ {valor_total_com_desconto:.2f}")

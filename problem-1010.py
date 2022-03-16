

id1, n1, preco1 = map(float, input().split())
id2, n2, preco2 = map(float, input().split())


print("VALOR A PAGAR: R$ %.2f"%(n1*preco1 + n2*preco2))
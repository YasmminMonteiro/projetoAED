
def aprovaCompra():
    cardNumber = input("Informe o número do cartão: ")
    localCompra = input("Informe o nome do estabelecimento: ")
    valorCompra = input("Valor da compra: R$ ")
    estabelecimento = arvore.buscar(localCompra)
    if estabelecimento is None:
        return "Compra negada. O estabelecimento não está cadastrado"
    cartao = arvore.buscar(cardNumber)
    if cartao is None:
        return "Cartão não idenficado!"
    if cartao.limiteTotal() <= valorCompra:
        #sub
        return "Transação Aceita!\n",cartao
    else:
        return "Compra negada. O valor da compra (%.2f) excede o limite disponível (%.2f)"
        %(valorCompra, cartao.limiteTotal())

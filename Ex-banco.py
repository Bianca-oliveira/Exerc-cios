class Banco:
    def __init__ (self, nome, idade, saldo):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos, Saldo: {self.saldo} reais"
    def saque (self, valor):
        self.valor = valor  
        if self.valor > 1000 and self.saldo < self.valor: 
          return 'Não poderá ser realizado o saque'
        else:
          return 'Poderá realizar o saque'
    def deposito (self, valor):
        self.valor = valor
        if self.valor > 5000:
          return 'Não é permitido realizar o depósito'
        else:
          return 'Adicionar ao saldo o valor do depósito'
    def emprestimo (self, valor):
        self.valor = valor
        if self.idade > 21:
          return 'Pode solicitar o empréstimo'
        else:
          return 'Empréstimo recusado'
        if self.saldo >= 1000 and self.valor < self.saldo*15:
          return f'Aprovado. Saldo em conta = R${self.saldo}'


cliente = Banco(str(input('Nome completo: ')), int(input('Idade: ')), saldo = 3.000)
print('''Qual opção deseja realizar?:
Digite (1) para saque
Digite (2) para depósito
Digite (3) para empréstimo
Digite (4) para vizualizar informações
Digite (Qualquer outro texto ou número) para sair''')

cliente = input('Digite a opção: ')
if cliente == '1':
  print(cliente.saque(str(input('Digite o valor do saque: R$'))))
elif cliente == '2':
  print(cliente.deposito(str(input('Digite o valor do depósito: R$'))))
elif cliente == '3':
  print(cliente.emprestimo(str(input('Digite o valor do empréstimo'))))


from models.cliente import Cliente
from models.conta import Conta

luis: Cliente = Cliente('Luís Henrique', 'oluishenriqueluciani@gmail.com', '123.456.789-00', '21/03/1990')
joao: Cliente = Cliente('João Arthur', 'jarthurluciani@gmail.com', '987.654.321-01', '06/03/1992')

# print(luis)
# print(joao)

contaf: Conta = Conta(luis)
contaa: Conta = Conta(joao)

# print(contaf)
# print(contaa)

import requests

# print(dados)
print("\n\tBem vindo ao Busca CEP\n\tAqui você pode procurar o lugar em que você quer chegar!")
cep = input("\nPor favor, digite o CEP que deseja localizar:")
url = f"https://viacep.com.br/ws/{cep}/json/"
res = requests.get(url)
dados = res.json()

#Print feito em aula
# print(f"A sua rua é {dados['logradouro']}.\nA sua cidade é {dados['localidade']}.\nO seu bairro é {dados['bairro']}.\nO estado é {dados['estado'], dados['uf']}.\nO complemento é {dados['complemento']}.\nE o CEP é {dados['cep']}.")

#Print do exercício
print("\n-----------DADOS BUSCADOS-----------\n")
print(f"CEP: {dados['cep']}\nRua: {dados['logradouro']}\nBairro: {dados["bairro"]}\nCidade: {dados["localidade"]}\nEstado: {dados["estado"]} ")
print("----"*10)
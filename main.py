# Este trecho "carrega" (cria uma conexão com) o arquivo que contem os dados
import pandas as pd

# https://drive.google.com/file/d/1sOawaIywxPo_uywYRWF1VBGZL5zq2vye/view?usp=sharing
codigo = "1sOawaIywxPo_uywYRWF1VBGZL5zq2vye"
arquivo = "https://drive.google.com/u/3/uc?id=" + codigo + "&export=download"

# note que sep=","  abaixo indica que o separador utilizado é ","
paises = pd.read_csv(arquivo, sep=",")

# QUANTAS LINHAS E COLUNAS tem
print(paises.shape)

# Nome das Colunas
print(paises.columns)

# Quais as informações do DataFrame ?
print(paises.info())

# Quantas linhas com dados (não nulos) existem na tabela para cada atributo
print(paises.count())

for ind in paises.index:  ## index contém range (de, até passo)
    pais = paises.loc[ind]  # usa o loc para obter os dados da linha ind
    print("ind:", ind, "Nome do País:", pais.Country, "Continente: ", pais.Region)

print("==>", paises.index)


##Carregando Dados em um Vetor

# função que carrega a população do "arquivo" para um vetor
def CarregaPopulacao(Vet, paises):
    for ind in paises.index:  # index contém o range (de, até, step)
        pais = paises.loc[ind]  # usa o loc para obter os dados da linha ind
        Vet.append(pais.Population)  # guarda a população no vetor Vet


# função que imprime o vetor com os dados da população
def ImprimePopulacao(Vet):
    print("As Populações armazenadas no vetor são:")
    N = len(Vet)
    for ind in range(N):
        print(Vet[ind], end=" |")


VetPopulacao = []
CarregaPopulacao(VetPopulacao, paises)
ImprimePopulacao(VetPopulacao)


# função que carrega a Birthrate do "arquivo" para um vetor
def CarregaBirthrate(Vet, paises):
    for ind in paises.index:  # index contém o range (de, até, step)
        pais = paises.loc[ind]  # usa o loc para obter os dados da linha ind
        Vet.append(pais.Birthrate)  # guarda o Birthrate no vetor Vet


# função que imprime o vetor com os dados da Taxa de Natalidade (Birthrate)
def ImprimeBirthrate(Vet):
    print("A taxa de natalidade armazenadas no vetor são:")
    N = len(Vet)
    for ind in range(N):
        print(Vet[ind], end=" |")




VetBirthrate = []
CarregaBirthrate(VetBirthrate, paises)
ImprimeBirthrate(VetBirthrate)



# Média da População dos primeiros 20 Países em ordem alfabética

Total = 0

def CalculaMedia(VetPopulacao, Total):
    for i in range(20):
        Total = VetPopulacao[i] + Total
    media = Total / 20
    return media
media = CalculaMedia(VetPopulacao, Total)
# Imprime Média
def ImprimeMedia(media):
    print("")
    print("A média das populações dos 20 primeiros países armazenadas no vetor são:")
    print(media)

ImprimeMedia(media)

soma = 0
VetBirthratePoint = []
for i in range(20):
    VetBirthratePoint.append(VetBirthrate[i].replace(',', '.'))
    VetBirthratePoint[i] = float(VetBirthratePoint[i])
    soma = soma + VetBirthratePoint[i]

def CalculaMediaB(VetNetMigrationPoint, soma):
    for i in range(20):
        soma = VetNetMigrationPoint[i] + soma
    mediaB = soma / 20
    return mediaB
mediaB = CalculaMediaB(VetBirthratePoint, soma)
# Imprime Média
def ImprimeMediaB(mediaB):
    print("")
    print("A média da natalidade dos 20 primeiros países armazenadas no vetor são:")
    print("%.2f"%mediaB)


ImprimeMediaB(mediaB)
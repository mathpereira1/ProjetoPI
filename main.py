# Este trecho "carrega" (cria uma conexão com) o arquivo que contem os dados
import pandas as pd

##---------------------------Função menu---------------------------##
# Organiza as perguntas a serem respondidas ao usuário
# Programa só encerra quando o usuário digita o comando '7'
def menu(paises):
  comando = int(input("1 - Densidade demográfica\n2 - Região\n3 - População\n4 - PIB per capita\n5 - Mortalidade\n6 - Natalidade na América Latina e Caribe\n7 - Encerrar\n"))
  if comando != 7:
    if comando == 1:
      MediaDensidade(paises)
      return
    elif comando == 2:
      pesquisa = input("Informe o país a ser pesquisado: ") + ' '
      PesquisaPais(pesquisa)
    elif comando == 3:
      ClassificaAPopulacaoDeUmPais(paises)
    elif comando == 4:
      PIBPerCapitaDosPaises(paises)
    elif comando == 5:
      TaxaDeMortalidade(paises)
    elif comando == 6:
      A = []
      B = []
      CarregaLatinAmerCarib(A,B)
      ImprimeMaiorNatLatin(A, B)
    else:
      print("Comando inválido. Redigite!")
    menu(paises)

##---------------------------Questão 1---------------------------##
# Dada uma região, calcula a média da densidade demográfica dos países dessa região
def MediaDensidade(paises):
  regioes = ['ASIA (EX. NEAR EAST)         ', 'EASTERN EUROPE                     ', 'NORTHERN AFRICA                    ',
             'OCEANIA                            ', 'WESTERN EUROPE                     ', 'SUB-SAHARAN AFRICA                 ',
             'LATIN AMER. & CARIB    ', 'C.W. OF IND. STATES ', 'NEAR EAST                          ', 'BALTICS                            ',
             'NORTHERN AMERICA                   ']
  regiao = int(input("""Digite a região cuja média da densidade demográfica deseja conhecer:
1 - ASIA (EX. NEAR EAST)
2 - EASTERN EUROPE
3 - NORTHERN AFRICA
4 - OCEANIA
5 - WESTERN EUROPE
6 - SUB-SAHARAN AFRICA
7 - LATIN AMER. & CARIB
8 - C.W. OF IND. STATES
9 - NEAR EAST
10 - BALTICS
11 - NORTHERN AMERICA
12 - Mundo
"""))
  if regiao >= 1 and regiao <= 11:
    soma = 0.0
    paises_desta_regiao = 0
    for j in range(227):
      if paises.loc[j][1].replace(' ', '') == regioes[regiao - 1].replace(' ', ''):
        soma = soma + ConverterParaFloat(paises.loc[j][4])
        paises_desta_regiao = paises_desta_regiao + 1
    print("Região " + regioes[regiao-1])
    print("Média da densidade demográfica: %.2f hab/mi²" %(soma/paises_desta_regiao))
  elif regiao == 12:
    soma = 0.0
    for j in range(227):
      soma = soma + ConverterParaFloat(paises.loc[j][4])
    print("Mundo")
    print("Média da densidade demográfica: %.2f hab/mi²" %(soma/227))
  else:
    print("Comando inválido. Digite novamente:")
    MediaDensidade(paises)

def ConverterParaFloat(string): # converte uma string com vírgula como separador de casas decimais para float
  return float(string.replace(",", "."))

##---------------------------Questão 2---------------------------##
# Função que padroniza a string de entrada, de forma que o programa leia primeiras letras maiusculas ou minusculas
def PadronizaPrimeiraLetra(s):
    return s[0].upper() + s[1:]
# função que recebe o país pesquisado e imprime sua respectiva região
def PesquisaPais(pesquisa):
    for ind in paises.index:  # index contém o range (de, até, step)
        pais = paises.loc[ind]  # usa o loc para obter os dados da linha ind
        paisLinha = pais.Country
        regiao = pais.Region
        pesquisa = PadronizaPrimeiraLetra(pesquisa)
        if pesquisa == paisLinha:
            print("O(a)", paisLinha, " pertence à seguinte região:", regiao)

##---------------------------Questão 3---------------------------##
# Dado um país, informa em qual posição o país se encontra na sua região e no mundo em termos de população
def ClassificaAPopulacaoDeUmPais(paises):
  pais = input("Digite o pais cuja populacao deseja saber: ") + ' '
  linha_do_pais = 0
  while (paises.loc[linha_do_pais][0] != pais):
    linha_do_pais = linha_do_pais + 1
    if linha_do_pais == 227:
      print("Nome de país inválido. O nome deve ser em inglês. Redigite:")
      ClassificaAPopulacaoDeUmPais(paises)
      return
  paises_na_mesma_regiao_com_populacao_maior = 0
  paises_no_mundo_com_populacao_maior = 0
  for j in range(227):
    if paises.loc[j][2] > paises.loc[linha_do_pais][2]:
      paises_no_mundo_com_populacao_maior = paises_no_mundo_com_populacao_maior + 1
      if paises.loc[j][1] == paises.loc[linha_do_pais][1]:
        paises_na_mesma_regiao_com_populacao_maior = paises_na_mesma_regiao_com_populacao_maior + 1
  print(pais, "tem uma população de", paises.loc[linha_do_pais][2], "habitantes")
  print("É a", paises_na_mesma_regiao_com_populacao_maior + 1, "maior população da região", paises.loc[linha_do_pais][1])
  print("E é a", paises_no_mundo_com_populacao_maior + 1, "maior população do mundo")

##---------------------------Questão 4---------------------------##
# Dado um país, informa todos os países que possuem PIB per capita próximo
# PIB per capita alto: acima de 20 mil dólares
# PIB per capita médio: entre 10 mil e 20 mil dólares
# PIB per capita baixo: entre 3 mil e 10 mil dólares
# PIB per capita baixíssimo: abaixo de 3 mil dólares
def PIBPerCapitaDosPaises(paises):
  pais = input("Digite o pais cujo PIB per capita deseja saber: ") + ' '
  linha_do_pais = 0
  while (paises.loc[linha_do_pais][0] != pais):
    linha_do_pais = linha_do_pais + 1
    if linha_do_pais == 227:
      print("Nome de país inválido. O nome deve ser em inglês. Redigite:")
      PIBPerCapitaDosPaises(paises)
      return
  if paises.loc[linha_do_pais][8] < 3000: # baixíssimo
    print(pais, "tem um PIB per capita, em dólares, de %.0f (baixíssimo)" % paises.loc[linha_do_pais][8])
    print("Todos os países com PIB per capita baixíssimo (abaixo de 3 mil dólares) são:")
    for i in range(227):
      if paises.loc[i][8] < 3000:
        print(paises.loc[i][0])
  elif paises.loc[linha_do_pais][8] >= 3000 and paises.loc[linha_do_pais][8] < 10000: # baixo
    print(pais, "tem um PIB per capita, em dólares, de %.0f (baixo)" % paises.loc[linha_do_pais][8])
    print("Todos os países com PIB per capita baixo (entre 3 mil dólares e 10 mil dólares) são:")
    for i in range(227):
      if paises.loc[i][8] >= 3000 and paises.loc[i][8] < 10000:
        print(paises.loc[i][0])
  elif paises.loc[linha_do_pais][8] >= 10000 and paises.loc[linha_do_pais][8] <= 20000:  # médio
    print(pais, "tem um PIB per capita, em dólares, de %.0f (médio)" % paises.loc[linha_do_pais][8])
    print("Todos os países com PIB per capita médio (entre 10 mil dólares e 20 mil dólares) são:")
    for i in range(227):
      if paises.loc[i][8] >= 10000 and paises.loc[i][8] <= 20000:
        print(paises.loc[i][0])
  else: # alto
    print(pais, "tem um PIB per capita, em dólares, de %.0f (alto)" % paises.loc[linha_do_pais][8])
    print("Todos os países com PIB per capita alto (acima de 20 mil dólares) são:")
    for i in range(227):
      if paises.loc[i][8] > 20000:
        print(paises.loc[i][0])

##---------------------------Questão 5---------------------------##
# Função que informa os países com as menores e maiores taxas de mortalidade de cada região e do mundo
def TaxaDeMortalidade(paises):
  regioes = ['ASIA (EX. NEAR EAST)         ', 'EASTERN EUROPE                     ', 'NORTHERN AFRICA                    ',
             'OCEANIA                            ', 'WESTERN EUROPE                     ', 'SUB-SAHARAN AFRICA                 ',
             'LATIN AMER. & CARIB    ', 'C.W. OF IND. STATES ', 'NEAR EAST                          ', 'BALTICS                            ',
             'NORTHERN AMERICA                   ']
  primeira_taxa_de_mortalidade = [0, 1, 2, 3, 4, 5, 6, 9, 15, 64, 80] # linha onde aparece cada regiao (na ordem do vetor regioes) pela primeira vez
  # Para cada uma das 11 regiões
  for i in range(11):
    ind_menor_mort = primeira_taxa_de_mortalidade[i]
    ind_maior_mort = primeira_taxa_de_mortalidade[i]
    for j in range(227):
      if paises.loc[j][1].replace(" ", "") == regioes[i].replace(" ", ""):
        if j == 47 or j == 181 or j == 221 or j == 223: # ignora células não preenchidas na base de dados
          continue
        elif ConverterParaFloat(paises.loc[ind_menor_mort][16]) > ConverterParaFloat(paises.loc[j][16]):
          ind_menor_mort = j
        elif ConverterParaFloat(paises.loc[ind_maior_mort][16]) < ConverterParaFloat(paises.loc[j][16]):
          ind_maior_mort = j
    print("Região", regioes[i])
    print("Menor taxa de mortalidade: " + paises.loc[ind_menor_mort][0] + "(%.2f)" % ConverterParaFloat(paises.loc[ind_menor_mort][16]))
    print("Maior taxa de mortalidade: " + paises.loc[ind_maior_mort][0] + "(%.2f)" % ConverterParaFloat(paises.loc[ind_maior_mort][16]))
  ind_menor_mort_mundo = 0
  ind_maior_mort_mundo = 0
  # Para o mundo
  for j in range(227):
    if j == 47 or j == 181 or j == 221 or j == 223: # ignora células não preenchidas na base de dados
      continue
    elif ConverterParaFloat(paises.loc[ind_menor_mort_mundo][16]) > ConverterParaFloat(paises.loc[j][16]):
      ind_menor_mort_mundo = j
    elif ConverterParaFloat(paises.loc[ind_maior_mort_mundo][16]) < ConverterParaFloat(paises.loc[j][16]):
      ind_maior_mort_mundo = j
  print("Mundo:")
  print("Menor taxa de mortalidade: " + paises.loc[ind_menor_mort_mundo][0] + "(%.2f)" % ConverterParaFloat(paises.loc[ind_menor_mort_mundo][16]))
  print("Maior taxa de mortalidade: " + paises.loc[ind_maior_mort_mundo][0] + "(%.2f)" % ConverterParaFloat(paises.loc[ind_maior_mort_mundo][16]))
 
##---------------------------Questão 6---------------------------##
# Função que carrega os países pertencentes a latino america e caribe, com suas respectivas taxas de natalidade
def  CarregaLatinAmerCarib(A, B):
    LatinAmerCarib = 'LATIN AMER. & CARIB    '
    for ind in paises.index:  # linhas
        pais = paises.loc[ind]
        regiao = pais.Region
        if LatinAmerCarib == regiao:
            A.append(pais.Country)
            B.append(pais.Birthrate.replace(',', '.'))
def ImprimeMaiorNatLatin(VetPais, VetNat):
    x = len(VetPais)
    i = 0
    maior = -999
    pais = ''
    for i in range(x):
        VetNat[i] = float(VetNat[i])
        if VetNat[i] > maior:
            maior = VetNat[i]
            pais = VetPais[i]
    print("A maior taxa de natalidade de um país pertencente à região latino americana & Caribe é %.2f" % maior,
          " do(da)", pais)

##---------------------------Função principal---------------------------##
# https://drive.google.com/file/d/1sOawaIywxPo_uywYRWF1VBGZL5zq2vye/view?usp=sharing
codigo = "1sOawaIywxPo_uywYRWF1VBGZL5zq2vye"
arquivo = "https://drive.google.com/u/3/uc?id=" + codigo + "&export=download"
# note que sep=","  abaixo indica que o separador utilizado é ","
paises = pd.read_csv(arquivo, sep=",")
menu(paises)

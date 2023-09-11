print ( "\"ola, mundão\" ", end='\n') #quebra de linha

##########################################################################################################################################################################################################################

print ("ola", "mundão", sep="-") # mudando o separador

##########################################################################################################################################################################################################################

print (type (1.1)) #identifica o tipo da informacao

##########################################################################################################################################################################################################################

print (10 == 10)  # == operador logico. booleano (True/False)

##########################################################################################################################################################################################################################

print (type (1 == 1)) 

##########################################################################################################################################################################################################################

print (float('1'),  type('1')) #uma class dentro de uma funcao ( o FLOAT esta mudando um INT para FLOAT)

##########################################################################################################################################################################################################################

print (type(float('1') + 1)) #convertendo um numero INT em FLOAT, sempre retornar um FLOAT

##########################################################################################################################################################################################################################

print ( str(11) + 'b' ) #convertendo um INT em STR

##########################################################################################################################################################################################################################

nome = 'Gabriel Zanata'
idade = 33
maior_de_idade = idade >= 18
print ( 'Nome:', nome, '\n' 'Idade:', idade, '\n' 'É maior de idade?:', maior_de_idade,)

##########################################################################################################################################################################################################################

nome_1 = 'Gabriel Zanata'
idade_1 = 33
maior_de_idade_1 = idade_1 >= 18
nome_2 = 'Fernanda Avilez'
idade_2 = 17
maior_de_idade_2 = idade_2 >= 18
print ( 'Nome:', nome_1, '\n' 'Idade:', idade_1, '\n', 'É maior de idade?', maior_de_idade_1) 
print ( 'Nome:', nome_2, '\n' 'Idade:', idade_2, '\n', 'É maior de idade?', maior_de_idade_2) #variaveis com um unico printe quebra de linhas

##########################################################################################################################################################################################################################

nome = ('Fernanda')
sobrenome = ('Avilez')
apelido = ('Nandinha Pink Star')
idade = 33
ano_de_nascimento = 2023 - idade
cidade_natal = ('São Paulo')
altura_em_metros = 168.5
maior_de_idade = idade>=18
estado_civil = ('Casada com Gabriel Zanata')
print ('Nome:', nome)
print ('Sobrenome:', sobrenome)
print ('Apelido:', apelido)
print ('Idade:', idade)
print ('Ano de nascimento:', ano_de_nascimento)
print ('Cidade Natal:', cidade_natal)
print ('Altura em metros:', altura_em_metros)
print ('É maior de idade?', maior_de_idade)
print ('Estado civil:', estado_civil)

##########################################################################################################################################################################################################################

divisao = 10 / 3 # divisao com numeros decimais
divisao = 10 // 3 # divisao com numeros inteiros
print ( divisao )
multiplicacao = 1024 * 10 #multiplicacao simples
exponenciacao = multiplicacao ** 68 # exponenciacao, é elevar um numero ao outro
print ( multiplicacao )
print ( exponenciacao )
modulo  =  55  %  2   # resto da divisão ou para saber se um numero e divisivel por outro
print ( 'Módulo' , modulo )
print ( 10  %  8  ==  0 )
print ( 16  %  8  ==  0 )
print ( 10  %  2  ==  0 )
print ( 15  %  2  ==  0 )
print ( 16  %  2  ==  0 )

##########################################################################################################################################################################################################################

concatenacao = 'Gabriel' + ' ' + 'Zanata'  # o sinal de + concatena string, tomar cuidado para nao colocar numero junto, para isso tenho que transforma o numero em STR
print (concatenacao)
concatenacao_1 = 'zZ' * 10
concatenacao_2 = 'Gabriel ' * 10  
print (concatenacao_1)
print (concatenacao_2)

##########################################################################################################################################################################################################################

conta_1  = ( 1  +  int ( 0.5  +  0.5 )) ** ( 5  +  5 )
print ( conta_1 ) # PROCEDENCIA DE OPERADORES... 1º sao os ()... 2º sao os **... 3º sao os * / // %... 4º sao os + -... Os parentese sempre resolvem de dentro para fora

##########################################################################################################################################################################################################################

# Indice de Massa Corporea
nome = 'Gabriel Zanata'
altura = 1.86 
peso = 159
idade = 33
imc = peso / (altura * altura)
Dado_1 = 66+(13.7 * peso)
Dado_2 = 5.0 * int(altura)
Dado_3 = 6.8 * idade
taxa_metabolica_basal = Dado_1 + Dado_2 - Dado_3
linha_1 = f'{nome} tem {altura} de altura, pesa {peso}kg. \nSeu IMC é de {imc:.2f} e a sua taxa metabolica basal é de {taxa_metabolica_basal}'
print ('Seu IMC é de:', imc)
print ('Sua taxa metabolica basal é de:', taxa_metabolica_basal)
print()
print (linha_1)
# a funcao f'{} permite que eu modifique a fora que eu vou ditar as informacoes. No IMC eu coloquei :.2f pq eu so queria 2 casa decimais dps do numero inteiro

##########################################################################################################################################################################################################################

input("Qual é o seu nome? ") #nesse caso o o dado colocado no input nao alterara o codigo programado
#-------------------------------------------------------------------------------------------------------------------#
nome = input("Qual é o seu nome? ")
print ("Seu nome é: ", nome) # nesse caso, eu nomeei a funcao do input, e logo em seguida mandei printar essa funcao segundo os parametros de STRING
#-------------------------------------------------------------------------------------------------------------------#
numero_1 = input ("Digite um número: ")
numero_2 = input ("Digite outro número: ")
print (f' A soma dos números são: {numero_1 + numero_2}') # a funcao INPUT sempre retorna o tipo STRING, nesse casso o sinal de + esta fazendo uma cocatenacao dos numeros escolhidos e nao esta somando de fato
#-------------------------------------------------------------------------------------------------------------------#
numero_1 = int(input ("Digite um número: "))
numero_2 = int(input ("Digite outro número: "))
print (f' A soma dos números são: {numero_1 + numero_2}') #aqui estou transformando o STR da funcao INPUT em numeros inteiros
#-------------------------------------------------------------------------------------------------------------------#
numero_1 = input ("Digite um número: ")
numero_2 = input ("Digite outro número: ")
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2) # aqui estou fazendo uma checagem no meio do caminho do codigo para garantir que os valores oferecido sao permitidos pelo codigo!
print (f' A soma dos números são: {numero_1 + numero_2}')

##########################################################################################################################################################################################################################

entrada = input ('Você quer "entrar" ou "sair"? ')
if entrada == "entrar":
    print (' Você entrou no sistema.')
elif entrada == "sair":
    print (' VocÊ saiu do sistema.')
else:
    print ('Você nao digitou uma opção válida.')  #bloco condicional do IF ( nunca esquecer de colocar os 2 pontos no final de cada condicao) o else é sempre o ultimo a entrar no bloco! A condicao ELIF eu posso repetir quantas vezes eu quiser

##########################################################################################################################################################################################################################

maior = 2>1
maior_ou_igual = 2>=2
menor = 2<3
menor_ou_igual = 3<=3
igual = 3==4
diferente = 4!=4
print(diferente)
                 
##########################################################################################################################################################################################################################

primeiro_valor = input ('Digite um valor: ')
segundo_valor = input ('Digite outro valor: ')
if primeiro_valor < segundo_valor:
    print ('O primeiro valor', primeiro_valor ,'é menor que o segundo valor ',segundo_valor,'digitado')
elif primeiro_valor > segundo_valor:
        print ('O primeiro valor', primeiro_valor, 'é maior que o segundo valor', segundo_valor, 'digitado')
else:
    print ('O primeiro valor', primeiro_valor ,'é igual ao segundo valor', segundo_valor ,'digitado')
#-------------------------------------------------------------------------------------------------------------------#
# comparacao com IF
#-------------------------------------------------------------------------------------------------------------------#
primeiro_valor  =  input ( 'Digite um valor: ' )
segundo_valor  =  input ( 'Digite outro valor: ' )
if  primeiro_valor  >=  segundo_valor :
    print (
        f' { primeiro_valor = } é maior ou igual '
        f'ao que { segundo_valor = } '
    )
else:
    print (
        f' { segundo_valor = } é maior '
        f'do que { primeiro_valor = } '
    )

##########################################################################################################################################################################################################################

entrada = input ('[E]ntrada [S]air:') 
senha_digitada = input ('Senha: ') or 'Sem senha'
senha_permitida = '123456' 
#-------------------------------------------------------------------------------------------------------------------#
#IF TRUE - só avalia se a expressao a seguir for toda verdadeira.
#-------------------------------------------------------------------------------------------------------------------#
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: # como a primeira condicao esta em parenteses, ela sera avaliada primeiro
    print ('Entrar')
else:
    print ('Sair')
#-------------------------------------------------------------------------------------------------------------------#
senha = input('Senha: ') or 'Sem senha'
print (senha)
#-------------------------------------------------------------------------------------------------------------------#
senha = input ('Senha: ')
if senha == 'Arcobalenino':
    print("Essa é a melhor senha do mundo: ")
else:
    print('Senha incorreta')
#-------------------------------------------------------------------------------------------------------------------#
senha = input ('Digite sua senha: ')
valor_de_senha = 'Arcobalenino'
if senha == valor_de_senha:
    print("Essa é a melhor senha do mundo: ")
elif senha != valor_de_senha:
    print ( ' Senha incorreta')

##########################################################################################################################################################################################################################
#condicao NOT...
print (not True) #False
print (not False) #True

##########################################################################################################################################################################################################################

#Condicao IN e NOT IN
nome = 'Gabriel José Sanches Zanata'
print (nome [-14])
print (nome [4])
# A contagem de casa sempre deve comecar pelo numero 0 ( g-0, a-1, b-2, r-3........) Tambem podemos contar atraves de indices negativos, mas devemos sempre comecar de tras para frente 
print ('Z' in nome)
print ('U' in nome) # devo digitar o quie procurar primeiro antes de digitar aonde procurar
#-------------------------------------------------------------------------------------------------------------------#
nome = input ('Digite seu nome: ')
encontrar = input ('Qual letra ou sílaba deseja encontrar? ')
if encontrar in nome:
    print( f'{encontrar} está em {nome}' )
else:
    print (f'{encontrar} não está em {nome}') #aqui estou procurando uma determinada letra ou silaba em palavra escolhida pelo proprio usuario

##########################################################################################################################################################################################################################
# interpolação basica de strings
nome = 'Gabriel Zanata'
preco = 1234.5678
variavel = '%s, o preco é R$%.2f ' % (nome, preco)  # a %s ou %f esta realizando a interpolacao de STR e FLOAT, cada um relacionado respectivamente com sua determinada funcao. 
print (variavel)

##########################################################################################################################################################################################################################
#formatação basica de STRINGs
variavel = 'Amor'
print (f'{variavel}')
print (f'{variavel:@>10}') # acrescenta um numero (10) de cacaracteres a esquerda da variavel
print (f'{variavel:&<10}') # acrescenta um numero (10) de cacaracteres a direita da variavel
print (f'{variavel:%^10}') # acrescenta um numero (10) de cacaracteres no meio da variavel
print (f'{123456.13216549:,.2f}') # Nesse caso a (,) esta fazendo a separacao de mil... o (.2f) esta fazendo com que apenas 2 casas decimais sejam exibidas

##########################################################################################################################################################################################################################
#Fatiamento de String e funcao len
variavel = 'Gabriel José Sanches Zanata'
print (variavel [4:])  #nesse caso eu escolhi aonde eu quero que seja fatiado, como eu nao escolhi o fim do fatiamento, me devolveu como resultado o fim da frase toda.
print (variavel [1:11]) #nesse caso eu escolhi o caracter 1 para iniciar o fatiamento e parei no caracter 11 
print (variavel [:9]) #nesse caso estou omitindo de onde eu quero que comece (entao vai comecar pelo caracter 0) e estou escolhendo aonde eu quero que pare
print (variavel [0::2]) #nesse caso escolhi contar do inicio ao final, so que contar de 2 em 2 (Inicio:Fim:Passo)
print (len(variavel [5])) #aqui a funcao len esta contando quantos caracteres tem naquele espaco
print (len(variavel [0:]))#aqui esta contando quanto tem do comeco (0) ate o final da frase 
#nos fazemos contagem de caracteres a partir do 1 mesmo, apenas os indices começamos a contar do 0

##########################################################################################################################################################################################################################
#exercicio com tudo que aprendi ate o momento!
nome = input ('Digite seu nome: ')
idade = input ('Digite sua idade: ')
if nome and idade:
    print (f'Seu nome é {nome}')
    print (f'Seu nome invertido seria assim: {nome [::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome nao contém espaços')
    print (f'Seu nome tem { len ( nome ) } letras' )
    print (f'A primeira letrado seu nome é a: {nome[0]}')
    print (f'A ultima letra do seu nome é a: {nome[-1]}')
else:
    print('Desculpe, voçê deixou campos vazios')

##########################################################################################################################################################################################################################
# a funcao .ISDIGIT depois de determinar uma variavel
numero =  input ('Digite um numero para ser dobrado:')
numero_float = float(numero)
if numero.isdigit():
    print (f'O dobro do numero {numero} digitado é = {numero_float * 2:}')
else:
    print('Você nao digitou um numero inteiro.')

#########################################################################################################################################################################################################################
#Função TRY e EXCEPT
try: #ele tentar forcar executar um codigo (diferente do if que para de executar quando encontra um erro) 
    pass #permite que eu continue a programar linhas a seguir sem antes programar essa parte
except: #adciona uma execao para o TRY. Se ocorrer algum erro dentro do TRY, pula direto para o EXCEPT
    pass #permite que eu continue a programar linhas a seguir sem antes programar essa parte
#-------------------------------------------------------------------------------------------------------------------#
numero_str = input('Digite um numero: ')
try: 
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro do numero de {numero_str} é = {numero_float * 2:.2f}')
except:
    print('isso não é um numero')

#########################################################################################################################################################################################################################



































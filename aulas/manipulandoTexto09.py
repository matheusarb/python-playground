# Fatiamento de String
frase = "Trabalhando na gringa"
print(frase[0:])
# ANALISE DE STRING
# Length
print(len(frase)) #tamanho da string

# Count
print(frase.count("t")) #qntidade de vezes q o caracter foi encontrado
print(frase.count("t", 0, 10)) #qntidade de vezes q o caracter foi encontrado dentro do intervalo

# Find
print(frase.find("grin")) # encontrar cadeia de caracteres na string

#------------------------------------------------------------------------#
# TRANSFORMACAO DE STRING
# Replace
print(frase.replace("gringa", "zoropa"))

# Upper e Lower
print(frase.upper())
print(frase.lower())

# Capitalize -> Primeira letra da string em maiúsculo
print(frase.capitalize())

# Title -> vai transformar em maiúsculo a cada quebra de palavra por espaço vazio
print(frase.title())

# Strip -> remover os espaços em branco do início e final da string
fraseComEspacos = "    Olá, Matheus, tudo bom?       "
print(fraseComEspacos)
print(fraseComEspacos.strip())
print(fraseComEspacos.rstrip())
print(fraseComEspacos.lstrip())

#------------------------------------------------------------------------#
# DIVISÃO DE STRING
# Split -> divide a string em uma lista, onde cada palavra separada por espaço será um elemento
list = frase.split()
print(list)

# Join -> pega todos os elementos em um iterável e junta eles em uma string
frase9 = " ".join(list)
# frase9.join(list)
print(frase9)

#

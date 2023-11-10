# Fatiamento de String
frase = "Trabalhando na gringa"

# ANALISE DE STRING
# Length
print(len(frase)) #tamanho da string

# Count
print(frase.count("t")) #qntidade de vezes q o caracter foi encontrado
print(frase.count("t", 0)) #qntidade de vezes q o caracter foi encontrado dentro do intervalo

# Find
print(frase.find("grin")) # encontrar cadeia de caracteres na string

#-----------------------------------------------#
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
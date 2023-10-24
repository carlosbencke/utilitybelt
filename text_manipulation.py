#! /usr/bin/python3


text = """This is a sample text.
And this is another line.
I'm batman!"""

# Inverte o texto
def text_invert(text):
    return text[::-1]

# Caixas altas
def uppercase(text):
	return text.upper()

# Caixa baixa
def lowercase(text):
	return text.lower()

# Primeira letra em maiúsculo
def first_upper(text):
	return text.title()

#Remove  linhas iguais
def remove_duplicated_lines(text):
	raw_list = text.splitlines()
	print(raw_list)
	coocked_list = []

	for line in raw_list:
		if line not in coocked_list:
			coocked_list.append(line)
	return str(coocked_list)

# Coloca em ordem alfabética
def ordem_alfabetica(text):
	raw_list = text.splitlines()
	raw_list.sort()
	return raw_list

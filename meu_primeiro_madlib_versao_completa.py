seunome = input("Oi, como você gostaria de ser chamado(a)? ")

print(f"\n\nOlá {seunome.title()}, seja bem vindo(a) ao meu primeiro Madlib! Para que sua experiência seja a melhor possível peço que você insira respostas que possuam mais de 1 caractere e que não sejam números! Vamos lá?\n ")

while True:
    bebida = input(" Primeiro insira um apelido, se possível cômico, para bebida: ")
    if bebida.isdigit():
      bebida = False
      print("Não digite somente números")
    elif isinstance(bebida,str) and len(bebida) > 1:
        break
    else:
        print("Entrada inválida. Por favor, insira uma resposta com mais de 1 caractere e que não contenha números.")


while True:
    banda = input("\n Agora escolha uma banda ou grupo musical que você goste: ")
    if isinstance(banda, str) and len(banda) > 1:
        break
    else:
        print("Entrada inválida. Por favor, insira uma resposta com mais de 1 caractere e que não seja somente números.")


while True:
    cantorFav = input("\n Qual é o seu cantor ou cantora favorito?")
    if cantorFav.isdigit():
      cantorFav = False
      print("Não digite somente números")
    elif isinstance(cantorFav, str) and len(cantorFav) > 1:
        break
    else:
        print("Entrada inválida. Por favor, insira uma resposta com mais de 1 caractere.")


sexo_valido = False
while not sexo_valido:
    sexo = input("\n  O artista escolhido é homem ou mulher? (H/M): ").lower()
    if sexo == 'h':
        sexo = 'o'
        sexo_valido = True
    elif sexo == 'm':
        sexo = 'a'
        sexo_valido = True
    else:
        print("Entrada inválida. Por favor, informe H para homem ou M para mulher.")


while True:
    pCorpo = input("\n  Escolha uma parte do corpo humano: ")
    if pCorpo.isalpha() and len(pCorpo) > 1:
        break
    else:
        print("Entrada inválida. Por favor, insira uma resposta com mais de 1 caractere e que não contenha um número.")

genpCorpo = pCorpo[-1]
if genpCorpo == 'a':
    genpCorpo = 'a'
else:
    genpCorpo = 'o'

while True:
    adjNeg = input("\n  Escolha um adjetivo negativo: ")
    if adjNeg.isalpha() and len(adjNeg) > 1:
        break
    else:
        print("Entrada inválida. Por favor, insira uma resposta com mais de 1 caractere e que não seja um número.")


while True:
    munPar1 = input("\n Agora escolha um município paraense que não seja Belém: ")
    if munPar1.isdigit():
      munPar1 = False
      print("Não digite apenas números")
    elif isinstance(munPar1, str) and len(munPar1) > 1:
        break
    else:
        print("Entrada inválida. Por favor, insira uma resposta com mais de 1 caractere e que não seja um número.")


while True:
    munPar2 = input("\n Um segundo município paraense, por favor: ")
    if munPar2.isdigit():
      munPar2 = False
      print("Não digite apenas números")
    elif munPar2 == munPar1:
      print("\n Escolha um município diferente do anterior")
    elif isinstance(munPar2, str) and len(munPar2) > 1:
        break
    else:
        print("Entrada inválida. Por favor, insira uma resposta com mais de 1 caractere e que não seja um número.")


while True:
    ofensa = input("\n  Prometo que é o ultimo, digite uma ofensa no plural por favor")
    if ofensa.isdigit():
      ofensa = False
      print("Entrada inválida. Por favor, insira uma resposta que contenha apenas letras.")
    elif not ofensa.endswith("s"):
        print("Por favor, insira uma ofensa no plural.")
    elif isinstance(ofensa,str) and len(ofensa) >1 and ofensa.endswith("s"):
      break
    else:
      print("Por favor, insira uma resposta com mais de 1 caractere.")


madlib = (f" Olá {seunome.title()}, seja bem vindo ao meu primeiro madlib! Para ter uma melhor experiência, por favor não utilize apenas números em suas respostas. Vamos lá?\n\n\n Você conhece \
 a história após a queda de Tróia?\n\n    A pilhagem mítica de Troia foi acompanhada por uma grande festa, na qual, como de costume, os gregos encheram a cara com {bebida} \
e destruíram toda a louça. Entretanto, como nem tudo são flores,\n misteriosos invasores do Mar Negro, publicamente conhecidos como  {banda.title()}, se aproveitaram da farra \
e apagaram as luzes gregas. Isso conduziu a um período que ficara conhecido como a Idade das Trevas.\n Quando os gregos finalmente acenderam tudo de novo, por volta de 800 a.C., além \
de terem descoberto que toda a sua louça estava em péssimas condições, ainda descobriram\n que {sexo} {cantorFav.title()} tinha se aposentado e as cidades tinham sido completamente destruídas.\n \
Coçando {genpCorpo} {pCorpo.casefold()}, os arrependidos e {adjNeg.casefold()} dos gregos iniciaram a reconstrução.\n    A palavra grega para o novo estilo de cidade era polis e durante um longo tempo eles só \
puderam ter uma, já que ninguém conseguia descobrir qual era o plural da palavra.\n\n   Posteriormente descobriram que tinham surgido duas cidades principais dentro de seu território \
- {munPar1.title()} e {munPar2.title()} -, também conhecidas como Atenas e Esparta, que\n passavam um terço do tempo guerreando contra os persas, um terço do tempo lutando entre si e o resto do \
tempo brigando consigo mesmas.\n \
\
Ao longo dos anos, as duas cidades desenvolveram democracias, que têm origem nas palavras gregas kratos, que significa “governar por”, e demos, que significa povo, ou, “totais \
{ofensa} que se deixam governar por pessoas ainda mais {ofensa}, chamadas políticos”. Isso ainda propiciou a inspiração para o sistema político moderno mais aceito nos dias de \
hoje, a democracia, ou, governo do povo. ")

print(madlib)


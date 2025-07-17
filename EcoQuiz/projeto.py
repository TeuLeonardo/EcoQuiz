print("🌿 Bem-vindo ao EcoQuiz! 🌎")
print("\nVocê está prestes a testar seus conhecimentos sobre meio ambiente, sustentabilidade e hábitos ecológicos.")
print("\nO EcoQuiz é simples: você vai responder algumas perguntas de múltipla escolha e, ao final, descobrirá o seu nível de consciência ecológica.")
print("\n♻️ Cada resposta certa vale pontos. \n🚫 Respostas erradas não somam nada. \n✅ No final, você receberá uma avaliação do seu desempenho.")
print("\nPronto para o desafio? Vamos ver se você pensa verde mesmo! 💚")


nomeJogador = input("Para começar, informe seu nome: ")
print(f"\nOlá {nomeJogador} Vamos começar o QUIZ?")
pontos = 0

print("\nPergunta 1 valendo 1 ponto")
print("\nQual meio de transporte é mais sustentável?")
print("A) Carro particular \nB) Bicicleta \nC) Motocicleta \nD) Avião")
while True:
    resposta = input("\nQual alternativa você escolhe? ").upper()
    if resposta == "B":
        print("\nAcertou! Você ganhou 1 ponto 😀")
        pontos += 1
        if pontos == 1:
            print(f"Você tem {pontos} ponto")
        else:
             print(f"Você tem {pontos} pontos")
        break
    elif(resposta == "A" or resposta == "C" or resposta == "D"):
        print("Você errou! A resposta correta é a letra B")
        break
    else:
        print("Insira uma resposta válida!")
        continue

print("\nHora da pergunta de número 2 valendo 1 ponto")
print("\nQual material pode ser reciclado?")
print("A) Papel higiênico usado \nB) Espelho quebrado \nC) Garrafa PET \nD) Bituca de cigarro")
while True:
    resposta = input("\nQual alternativa você escolhe? ").upper()
    if resposta == "C":
        print("\nAcertou! Você ganhou 1 ponto 😀")
        pontos += 1
        if pontos == 1:
            print(f"Você tem {pontos} ponto")
        else:
             print(f"Você tem {pontos} pontos")
        break
    elif(resposta == "A" or resposta == "B" or resposta == "D"):
        print("Você errou! A resposta correta é a letra C")
        break
    else:
        print("Insira uma resposta válida!")
        continue

print("\nHora da pergunta de número 3 valendo 3 pontos")
print("\nQual setor é responsável pela maior parte da emissão de gases do efeito estufa no mundo?")
print("A) Transporte rodoviário \nB) Indústria de eletrônicos \nC) Agropecuária \nD) Uso doméstico de energia elétrica")
while True:
    resposta = input("\nQual alternativa você escolhe? ").upper()
    if resposta == "C":
        print("\nAcertou! Você ganhou 3 pontos 😀")
        pontos += 3
        if pontos == 1:
            print(f"Você tem {pontos} ponto")
        else:
             print(f"Você tem {pontos} pontos")
        break
    elif(resposta == "A" or resposta == "B" or resposta == "D"):
        print("Você errou! A resposta correta é a letra C")
        break
    else:
        print("Insira uma resposta válida!")
        continue

print("\nPergunta de número 4 valendo 1 ponto")
print("\nO que é Pegada Ecológica?")
print("A) Um símbolo usado em embalagens recicláveis  \nB) Tipo de solo usado na agricultura orgânica \nC) Marca dos pés de animais em trilhas ecológicas \nD) Medida do impacto das atividades humanas no meio ambiente")
while True:
    resposta = input("\nQual alternativa você escolhe? ").upper()
    if resposta == "D":
        print("\nAcertou! Você ganhou 1 ponto 😀")
        pontos += 1
        if pontos == 1:
            print(f"Você tem {pontos} ponto")
        else:
             print(f"Você tem {pontos} pontos")
        break
    elif(resposta == "A" or resposta == "B" or resposta == "C"):
        print("Você errou! A resposta correta é a letra D")
        break
    else:
        print("Insira uma resposta válida!")
        continue

print("\nÚltima Pergunta valendo 4 pontos")
print("\nO que é o Protocolo de Kyoto?")
print("A) Um acordo entre empresas para vender produtos sustentáveis \nB) Um plano nacional de reciclagem desenvolvido pelo Japão \nC) Um tratado internacional para reduzir a emissão de gases do efeito estufa \nD) Um programa de reflorestamento exclusivo da Ásia")
while True:
    resposta = input("\nQual alternativa você escolhe? ").upper()
    if resposta == "C":
        print("\nAcertou! Você ganhou 4 pontos 😀")
        pontos += 4
        if pontos == 1:
            print(f"Você tem {pontos} ponto")
        else:
             print(f"Você tem {pontos} pontos")
        break
    elif(resposta == "A" or resposta == "B" or resposta == "D"):
        print("Você errou! A resposta correta é a letra C")
        break
    else:
        print("Insira uma resposta válida!")
        continue



print("\nParabéns, você completou o EcoQuiz! 🌿")
if pontos == 1:
    print(f"\n{nomeJogador}, você terminou o quiz com {pontos} ponto de 10 possíveis!")
else:
    print(f"\n{nomeJogador}, você terminou o quiz com {pontos} pontos de 10 possíveis!")


if pontos <=3:
    print("\nSua consciência ecológica ainda está germinando... Mas todo aprendizado começa assim! 🌱")
    print("\n💡 Dica: pequenas atitudes no dia a dia já fazem a diferença. Continue aprendendo!")
elif pontos <= 6:
    print("\nMuito bem! Você já tem uma boa noção sobre sustentabilidade. 🍀")
    print("🚀 Continue se informando e praticando ações ecológicas no seu dia a dia")
elif pontos <= 9:
    print("\nExcelente! Sua consciência ecológica está em ótimo nível! 🌳")
    print("✅ Você já faz a diferença e está no caminho certo para um mundo mais sustentável. ")
else:
    print("\nIncrível! Você é um verdadeiro guardião do planeta! 🌍")
    print("\n🌟 Sua consciência ecológica é digna de aplausos. Continue espalhando esse exemplo! 💚")



print("\nObrigado por participar do EcoQuiz! Até a Próxima 👋")
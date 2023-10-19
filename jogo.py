#esse é o código do jogo "Não encontre o nariz!"
import tkinter as tk

#início do jogo
janela = tk.Tk()
janela.title("--NÃO ENCONTRE O NARIZ!--")
janela.geometry("1500x400")
titulo_texto = tk.Label(text="--NÃO ENCONTRE O NARIZ!--", font=("Arial", "20"))
texto = tk.Label(janela, text="Você está em uma sala com dois corredores. Ao centro, há uma chave amarela. Ao pegá-la, você pode ir para o corredor esquerdo ou direito. Qual você escolhe?", font=("Arial", "12"))
frame_botoes = tk.Frame(janela)
botao = tk.Button(frame_botoes, text="corredor 1", command=lambda: escolher_corredor("corredor 1"))
botao2 = tk.Button(frame_botoes, text="corredor 2", command=lambda: escolher_corredor("corredor 2"))

#função de escolher o corredor
def escolher_corredor(corredor):
    texto.pack_forget()
    frame_botoes.pack_forget()

#escolhe corredor
    if corredor == "corredor 1":
       mensagem = tk.Label(janela, text="Você encontra uma porta com um cadeado amarelo. Ao abrí-la, você encontra um PARKOUR =D. Nele, você terá que escolher a porta certa para passar de fase.", font=("Arial", "12"))
       mensagem.pack()
       mensagem_parkour = tk.Label(janela, text="1° fase: [Porta branca | Porta azul]", font=("Arial", "12"))
       mensagem_parkour.pack()
       botao_azul.pack()
       botao_branco.pack()

    elif corredor == "corredor 2":
       mensagem = tk.Label(janela, text= "Você não encontra uma porta para usar a chave, mas encontra o tremendo nariz e ele te aspira. VOCÊ PERDEU MUAHAHA", font=("Arial", "12"))
       mensagem.pack()
       reset = tk.Label(janela, text="Deseja recomeçar?", font=("Arial", "14"))
       botao_reset = tk.Button(text="sim", command=reiniciar_jogo)
       reset.pack()
       botao_reset.pack()



#função de reiniciar o jogo
def reiniciar_jogo():
    for widget in janela.winfo_children():
        widget.pack_forget()
    
    titulo_texto.pack()
    texto.pack()
    frame_botoes.pack()


#função de limpar a tela
def limpar_tela():
    for widget in janela.winfo_children():
        widget.pack_forget()
        titulo_texto.pack() 

#função de voltar para a primeira fase do parkour
def reset_parkour():
    limpar_tela()
    mensagem_parkour = tk.Label(janela, text="Você encontrou o nariz...escolha a porta novamente \n"
                                "1° fase: [Porta branca | Porta azul] \n", font=("Arial", "12"))
    mensagem_parkour.pack()
    botao_azul.pack()
    botao_branco.pack()
    
# função da segunda fase do parkour
def segunda_fase_parkour():
   mensagem_parkour = tk.Label(janela, text="2° fase: [Porta roxa | Porta preta]", font=("Arial", "12"))
   mensagem_parkour.pack()
   botao_roxo.pack()
   botao_preto.pack()
   botao_branco.pack_forget()
   botao_azul.pack_forget()

#função da terceira fase do parkour
def terceira_fase_parkour():
   mensagem_parkour = tk.Label(janela, text="3° fase: [Porta de madeira | Porta de ferro]", font=("Arial", "12"))
   mensagem_parkour.pack()
   botao_madeira.pack()
   botao_ferro.pack()
   botao_roxo.pack_forget()
   botao_preto.pack_forget()

def voce_passou():
   limpar_tela()
   mensagem = tk.Label(janela, text="PARABÉNS! Você concluiu o parkour =D", font=("Arial", "12"))
   mensagem.pack()
   texto = tk.Label(janela, text=" Após concluí-lo, você encontra uma chave de cor roxa e, automaticamente, é redirecionado à mesma sala, porém, com 3 corredores. Qual corredor você escolhe?", font=("Arial", "12"))
   texto.pack()
   frame_botoes_corredor.pack()
   botao_corredor1.pack(side="left", padx=10)
   botao_corredor2.pack(side="left", padx=10)
   botao_corredor3.pack(side="left", padx=10)
   botao_ferro.pack_forget()
   botao_madeira.pack_forget()

def voce_perdeu():
   limpar_tela()
   mensagem = tk.Label(janela, text="PARABÉNS! Você VACILOU no finalzinho do parkour (as portas de ferro NÃO ABREM) \n"
                       "escolha as portas novamente...\n", font=("Arial", "12"))
   mensagem.pack()
   mensagem_parkour = tk.Label(janela, text="1° fase: [Porta branca | Porta azul]", font=("Arial", "12"))
   mensagem_parkour.pack()
   botao_azul.pack()
   botao_branco.pack()
   botao_ferro.pack_forget()
   botao_madeira.pack_forget()

   

#botoes do parkour 
botao_azul = tk.Button(janela, text="Porta azul", command= reset_parkour)
botao_branco = tk.Button(janela, text="Porta branca", command= segunda_fase_parkour)
botao_roxo = tk.Button(janela, text="Porta roxa", command= terceira_fase_parkour)
botao_preto = tk.Button(janela, text="Porta preta",command= reset_parkour)
botao_madeira = tk.Button(janela, text="Porta de madeira", command= voce_passou)
botao_ferro = tk.Button(janela, text="Porta de ferro", command=voce_perdeu)

# funções de escolher corredor novamente
def corredor1():
   limpar_tela()
   mensagem = tk.Label(janela, text='Você está caminhando no corredor 1, tranquilamente, até que encontra um gato preto falante. Ele olha para você e diz:"NÃO HÁ NADA AQUI...miau" \n'
                       "Então, você simplesmente dá a volta e retorna para a sala com os 3 corredores \n", font=("Arial", "12"))
   mensagem.pack()
   frame_botoes_corredor.pack()
 


def corredor2():
   limpar_tela()
   mensagem = tk.Label(janela, text="Você está caminhando no corredor 2, tranquilamente, até que acaba avistando uns olhos vermelhos. Eles se aproximam cada vez mais...CATAPIMBAS É O NARIZ!", font=("Arial", "12"))
   mensagem.pack()
   mensagem_2 = tk.Label(janela, text="Automaticamente, você é aspirado.", font=("Arial", "12"))
   mensagem_2.pack()
   botao_reset.pack()
   

def corredor3():
   limpar_tela()
   mensagem = tk.Label(janela, text="Você está caminhando no corredor 3, tranquilamente, até que encontra uma porta com um cadeado roxo. Logo, você usa sua chave nela e é surpreendido por algumas pergunta sobre Phyton! \n"
                       "QUIZ! Neste quiz, terá apenas perguntas sobre esta linguagem de programação bacaninha! \n", font=("Arial", "12"), wraplength=1300)
   mensagem.pack()
   botao_quiz = tk.Button(janela, text="começar quiz", command= primeira_pergunta)
   botao_quiz.pack()

#botoes dos corredores (parte 2) e do reset 
frame_botoes_corredor = tk.Frame(janela)
botao_corredor1 = tk.Button(frame_botoes_corredor, text="corredor 1", command=corredor1)
botao_corredor2 = tk.Button(frame_botoes_corredor, text="corredor 2", command= corredor2)
botao_corredor3 = tk.Button(frame_botoes_corredor, text="corredor 3", command= corredor3)
botao_reset = tk.Button(janela, text="recomeçar jogo", command= reiniciar_jogo)

#funções das perguntas do quiz
def primeira_pergunta():
   limpar_tela()
   quiz = tk.Label(janela, text= "1)Qual é a tag que cria um loop?", font=("Arial", "12"))
   quiz.pack()
   botao_if.pack()
   botao_while.pack()
   botao_python.pack()

def segunda_pergunta():
   limpar_tela()
   quiz = tk.Label(janela, text= "2)Quem criou essa linguagem de programação?", font=("Arial", "12"))
   quiz.pack()
   botao_guildo.pack()
   botao_dwayne.pack()
   botao_charles.pack()

def terceira_pergunta():
   limpar_tela()
   quiz = tk.Label(janela, text= "3)Quando surgiu o python?", font=("Arial", "12"))
   quiz.pack()
   botao_1991.pack()
   botao_1992.pack()
   botao_1993.pack()

def quarta_pergunta():
   limpar_tela()
   quiz = tk.Label(janela, text= "4)Qual é a tag que imprime na tela", font=("Arial", "12"))
   quiz.pack()
   botao_text.pack()
   botao_imprimir.pack()
   botao_print.pack()

#função de caixa de texto
def ler_caixa():
   limpar_tela()
   resultado.config(text="PARABÉNS! Você completou o quiz!", font=("Arial", "12"))
   resultado.pack()
   mensagem = tk.Label(janela, text="Assim, você acaba recebendo uma chave verde, juntamente com um recado sem assinatura: 'Você não irá embora tão cedo...' (Você é redirecionado a uma sala vazia)", font=("Arial", "12"))
   mensagem.pack()
   botao_sala = tk.Button(janela, text="sala vazia", command=sala_vazia)
   botao_sala.pack()


def caixa_de_texto():
   caixa_de_texto = tk.Entry(janela)
   caixa_de_texto.pack()
   botao_caixa = tk.Button(janela, text="enviar", command= ler_caixa)
   botao_caixa.pack()
resultado = tk.Label(janela, text="")
   

def quinta_pergunta():
   limpar_tela()
   quiz = tk.Label(janela, text= "5)O que é python para você? (em uma palavra)", font=("Arial", "12"))
   quiz.pack()
   caixa_de_texto()


#função quando a resposta estiver errada
def errou():
   limpar_tela()
   mensagem = tk.Label(janela, text="RESPOSTA ERRADA.", font=("Arial", "12"))
   mensagem.pack()
   reiniciar_quiz = tk.Button(janela, text="recomeçar", command= primeira_pergunta)
   reiniciar_quiz.pack()

#botoes do quiz
botao_if = tk.Button(janela, text="A) if", command= errou)
botao_while = tk.Button(janela, text="B) while", command= segunda_pergunta)  
botao_python = tk.Button(janela, text="C) python", command= errou)
botao_guildo = tk.Button(janela, text="A) Guildo van Rossum", command= terceira_pergunta)
botao_dwayne = tk.Button(janela, text="B) Dwayne Johnson", command= errou)
botao_charles = tk.Button(janela, text="C) Charles Babbage", command= errou)
botao_1991 = tk.Button(janela, text="A) 1991", command= quarta_pergunta)  
botao_1992 = tk.Button(janela, text="B) 1992", command= errou)  
botao_1993 = tk.Button(janela, text="C) 1993", command= errou)  
botao_text = tk.Button(janela, text="A) text", command= errou)  
botao_imprimir = tk.Button(janela, text="B) imprimir", command= errou)  
botao_print = tk.Button(janela, text="C) print", command= quinta_pergunta)  

#sala vazia 
def sala_vazia():
   limpar_tela()
   mensagem = tk.Label(janela, text="Ao entrar na sala vazia, você vê uma silhueta um pouco peculiar. Era enorme e tinha um formato de uma beterraba.Seus olhos vermelhos se aproximavam cada vez mais...e mais...\n"
                       "É O TREMENDO NARIZ!\n"
                       "'Eu estava te esperando...' Disse o grande. Aparentemente, ele queria conversar. \n"
                       "Você quer conversar com o nariz? \n", font=("Arial", "12"))
   mensagem.pack()
   frame_sala.pack()
   sim.pack(side="left", padx=20)
   nao.pack(side="left", padx=20)


#função do botão de conversar com o nariz(caso escolha ele)
def botao_sim():
   limpar_tela()
   mensagem = tk.Label(janela, text="Você decide conversar com o GRANDE, o PODEROSO, o ONIPOTENTE...Nariz \n"
                       "Ele estava chorando, pois se sentia sozinho e perdido nessa vida. \n"
                       "Então, o que irá fazer? \n", font=("Arial", "12"))
   mensagem.pack()
   valinhos.pack()
   ajuda.pack()
   rir.pack()

#funções das opções caso converse com o nariz
def valinhos_nariz():
   limpar_tela()
   mensagem = tk.Label(janela, text="Você manda o nariz ir para Valinhos. Ele fica confuso, pois não sabe o que é isso. \n"
                       "Você explica que Valinhos é uma cidade que vende bolos maravilhosos. O nariz fica encantado.\n"
                       "Assim, o nariz te acompanha até a porta de saída, e você utiliza a chave verde para abrí-la \n"
                       "Desde então, o nariz passou a viver em Valinhos, degustando de seus bolos. \n", wraplength= 1400, font=("Arial", "12"))

   mensagem.pack()
   concluido.pack()
   botao_reset.pack()

def ajuda_nariz():
   limpar_tela()
   mensagem = tk.Label(janela, text="Você ajuda o nariz, dando apoio emocional.\n"
                       "Depois de um chá com biscoitos e muita conversa, vocês ficaram amigos!"
                       "O nariz te leva até a porta da sala e você utiliza a chave verde para abrí-la. \n", font=("Arial", "12"))
   mensagem.pack()
   concluido.pack()
   botao_reset.pack()

def rir_nariz():
   limpar_tela()  
   mensagem = tk.Label(janela, text="Você começa a rir da cara do nariz depois de todo seu discurso. Ele fica ofendido. \n"
                       "Antes de você sair da sala, o grande nariz te aspira.\n", font=("Arial", "12"))
   mensagem.pack()
   nao_concluido.pack()  
   botao_reset.pack()

#botoes da conversa com o nariz
valinhos = tk.Button(janela, text="mandar ele ir para Valinhos", command= valinhos_nariz)
ajuda = tk.Button(janela, text="Ajudar o coitado do nariz", command= ajuda_nariz)
rir = tk.Button(janela, text="rir da cara dele e sair da sala", command=rir_nariz)

#função de não conversar com o nariz
def botao_nao():
   limpar_tela()
   mensagem = tk.Label(janela, text="Você simplesmente vaza da sala utilizando a chave verde, deixando o nariz confuso.", font=("Arial", "12"))
   mensagem.pack()
   concluido.pack()
   botao_reset.pack()
#botoes da sala vazia
frame_sala = tk.Frame(janela)
sim = tk.Button(frame_sala, text="sim", command= botao_sim)
nao = tk.Button(frame_sala, text="não", command=botao_nao)

#labels de conclusão e não-conclusão do jogo
concluido = tk.Label(janela, text="Você concluiu o jogo!", font=("Arial", "12"))
nao_concluido = tk.Label(janela, text="Você perdeu!", font=("Arial", "12"))

#variáveis do início do jogo
titulo_texto.pack()
texto.pack()
frame_botoes.pack()
botao.pack(side="left", padx=10)
botao2.pack(side="left", padx= 10)
janela.mainloop()
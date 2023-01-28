#########################################################
#PROJETO DE BOT PARA MENSAGENS EM MASSA NO WHATSAPP
#########################################################

#Descrição do projeto
#1- lista de números;
#2-enviar individualmente uma mensagem para cada pessoa - normalmente a mesma mensagem;
#3- pausar entre cada envio para o whatsapp não bloquear - entre uma mensagem e outra 300 segundos

#How to-do
#1- escolher um contato
#2- enviar a mensagem a esse contato
#3- repetir essa rotina a outros contatos

#Código padrão de envio de mensagens no whatsapp: https://api.whatsapp.com/send?phone=5561981942705
#veja que a parte final do código se trata do telefone para onde será encaminhada a mensagem, ou seja, para cada contato
#é necessário apenas a modificação do código padrão, com a inclusão do telefone do contato a quem encaminharemos a mensagem.


#Requerimentos
import webbrowser
import pyautogui
import pyperclip
from time import sleep

#Execução do projeto
#Existem duas formas de fazer esse projeto:
#2) a segunda é vc tendo um documento com os telefones e vc precisa extrair esses contatos com um laço de repetição.
#Exemplo: temos um bloco de notas que possui diversos contatos e vamos extreir as informações diretamente deste arquivo.
#Primeiro criamos uma lista vazia, que irá receber esses números
telefone = []
#agora vamos ler o arquivo com os telefones:
with open('fones.txt', 'r') as arquivo: #apelidamos a lista como arquivo
    for linha in arquivo: #para cada linha dentro do arquivo
        telefone.append(linha.split('\n')[0])#pegue essa linha e insira na lista vazia 'telefone', fazendo um split para retirar o \n de quebra de linhas
    print(telefone)

# #Functions
# #Função de caracteres especiais
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

#Agora vamos inserir a mensagem que queremos transmitir aos nossos contatos.
frase = pyautogui.prompt(text='Digite aqui a mensagem que vc espera que seja encaminhada aos seus contatos', title='mensagem a ser encaminhada aos contatos.')

for tel in telefone:
    webbrowser.open_new(f'https://api.whatsapp.com/send?phone={tel}')#o f é formatação para que possamos inserir a variável. É a mesma coisa do format
    sleep(4)
    pyautogui.click(x=1096,y=280, duration=0.5)#Vamos agora fechar a janela de aviso que aparece no app do whatsapp
    sleep(10)
    escrever_frase(frase)#escrevendo a frase com a função de caracteres especiais recebidas da variável de promp que declaramos para a mensagem
    sleep(3)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.hotkey('alt','F4')
    sleep(1)
    pyautogui.hotkey('alt','F4')
    sleep(30)
  


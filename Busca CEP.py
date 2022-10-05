import telebot
import requests

# Token do Bot do Telegram
token = '5780284825:AAFitvLWa9KF7jrZyu8oKscdd6bXagps7kE'
bot = telebot.TeleBot(token)

# Função para validar o CEP
def verificar(mensagem):
    cep = mensagem.text
    cep = cep.replace('-', '').replace('.', '').replace(' ', '')
    if cep.isdigit() == True:
        return True

# Função do Telegram para conectar com a API Via CEP e retornar o resultado
@bot.message_handler(func=verificar)
def funcao_cep(mensagem):
    print(mensagem.text)
    cep = mensagem.text
    cep = cep.replace('-', '').replace('.', '').replace(' ', '')
    if len(cep) == 8:
        api = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(api)
        dic_requisicao = requisicao.json()
        logradouro = dic_requisicao['logradouro']
        bairro = dic_requisicao['bairro']
        cidade = dic_requisicao['localidade']
        uf = dic_requisicao['uf']
        endereco = 'Endereço: ' + logradouro + ' \n' + 'Bairro: ' + bairro + ' \n' + 'Cidade: ' + cidade + ' \n' + 'UF: ' + uf
        print(endereco)
        bot.reply_to(mensagem, endereco)
    else:
        print('CEP Inválido')
        bot.reply_to(mensagem, 'CEP Inválido')

# Função do Telegram para responder mensagem
@bot.message_handler(content_types=['text'])
def responder(mensagem):
    bot.reply_to(mensagem, '''
Busca CEP

Digite o número do CEP para receber o endereço completo.''')

bot.polling()
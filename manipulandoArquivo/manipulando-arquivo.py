import telebot
import os
from supabase import create_client, Client

url: str = "https://dwpvbvlcoabbokzysjsh.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR3cHZidmxjb2FiYm9renlzanNoIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTEyNDg1MzksImV4cCI6MjAwNjgyNDUzOX0.yplD2Va_na7VsMFcQDB2A0l66O5l05NbRFxWHvmRd6A"
supabase: Client = create_client(url, key)


response = supabase.table('testeDB').select('*').eq('id',1).single().execute()
# response = list(response.data)[0]["menu_desc"]

print(response)

CHAVE_API = "6295709361:AAFShC9euTMCza02JEcP5wemHXUpP0_gYmo"


bot = telebot.TeleBot(CHAVE_API)

##VARIAVEIS DE LEITURA DE ARQUIVO !!!

menuzin = supabase.table('testeDB').select('description').eq('id',6).single().execute()

print(menuzin)

menu = menuzin.data["description"]
# with open(".\menu.txt", "r", encoding="utf-8") as arquivo:
#     menu = arquivo.read()
with open("tabelas.txt", "r", encoding="utf-8") as arquivo:
    var_tabelas = arquivo.read()

with open("lentidao_calculo.txt", "r", encoding="utf-8") as arquivo:
    var_lentidao_calculo = arquivo.read()


print(menu)

"""
RECEBER COMANDOS DO TELEGRAM !!!
"""
titulo = ""
desc_nota = ""

@bot.message_handler(commands=["nova_nota"])
def nova_nota(mensagem):
    titulo1 = mensagem.text

    desc_nota = mensagem.text
    desc_nota = desc_nota.replace("/nova_nota","")
    print(desc_nota)


    supabase.table('testeDB').insert({"description":desc_nota}).execute()

    # with open("controle_nota.txt", "w", encoding="utf-8") as arquivo:
    #     arquivo.write(titulo1)

    # with open("controle_nota.txt", "r", encoding="utf-8") as arquivo:
    #     titulo = arquivo.read()
    # titulo = titulo.split()
    # titulo3 = titulo[1]
    # print(titulo3)

    # with open(titulo3 + ".txt", "w", encoding="utf-8") as arquivo:
    #     arquivo.write(desc_nota)
    
    # with open("menu.txt", "r", encoding="utf-8") as arquivo:
    #     var_alterar_menu = arquivo.read()


    # with open("menu.txt", "a", encoding="utf-8") as arquivo:
    #     arquivo.write("\n/" + titulo3 )

    

    bot.reply_to(mensagem, "Nota adicionada!!!")
    pass


@bot.message_handler(commands=["inserir_nota"])
def nova_nota(mensagem):
    bot.reply_to(mensagem, var_inserir_nota)
    pass

@bot.message_handler(commands=["tabelas"])
def tabelas(mensagem):
    print(mensagem.text)
    bot.reply_to(mensagem, var_tabelas)
    pass

@bot.message_handler(commands=["lentidao_calculo"])
def lentidao_calculo(mensagem):
    bot.reply_to(mensagem, var_lentidao_calculo)
    pass

def verificar(mensagem):    
    return True
    
@bot.message_handler(func=verificar)
def responder(mensagem):
    
    bot.reply_to(mensagem, menu)


bot.polling()
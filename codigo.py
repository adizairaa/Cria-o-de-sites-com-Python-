# Hashzap
# botão de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat: Bem vindo ao Hashzap
    # caixa de texto: Escreva seu nome no chat 
    # botão: Entrar no chat 
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem


import flet as ft  # um só código pode ser usado no sistema inteiro (1 importar o flet, 2 criar uma função principal para rodar o seu app, 3 executar essa função com o flet)

def main(pagina):  # Título e botão inicial
    # título
    titulo = ft.Text("Hashzap")

    # criar o popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=lambda e: entrar_chat(e))
    #O e (ou evento) é um objeto que carrega informações sobre a interação do usuário com a interface. 
    # Ele é passado automaticamente pela biblioteca Flet quando um evento ocorre, e você pode usá-lo para reagir ao comportamento do usuário.

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=lambda e: enviar_mensagem(e))
    botao_enviar = ft.ElevatedButton("Enviar", on_click=lambda e: enviar_mensagem(e))
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    # botão inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clicou no botão")

    botao = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    # colocar elementos na página
    pagina.add(titulo)
    pagina.add(botao)

    chat = ft.Column()

    def entrar_chat(evento):
        # fechar o popup
        popup.open = False
        # sumir com o título
        pagina.remove(titulo)
        # sumir com o botão de iniciar chat
        pagina.remove(botao)
        # carregar o chat
        pagina.add(chat)
        # carregar campo de enviar mensagem e o botão enviar
        pagina.add(linha_enviar)
        # adicionar no chat a mensagem "Fulano entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = ft.Text(f"{nome_usuario} entrou no chat", size=12, italic=True, color=ft.colors.ORANGE_500)
        chat.controls.append(mensagem)

        pagina.update()

    # função enviar mensagem
    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = ft.Text(f"{nome_usuario}: {texto_campo_mensagem}")
        chat.controls.append(mensagem)
        # limpar a caixa de mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()

    # websocket - túnel de comunicação entre dois usuários
    def enviar_mensagem_tunel(mensagem):
        # executar tudo o que eu quero que aconteça para
        # todos os usuários receberem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

# deploy

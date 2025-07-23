import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    """if comando in ('olá', 'boa tarde', 'bom dia'):
        return 'Olá tudo bem!'
    if comando == 'como estás':
        return 'Estou bem, obrigado!'
    if comando == 'como te chamas?':
        return 'O meu nome é: Bot :)'
    if comando == 'tempo':
        return 'Está um dia de sol!'
    if comando in ('bye', 'adeus', 'tchau'):
        return 'Gostei de falar contigo! Até breve...'
    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'
    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    return f'Desculpa, não entendi a questão! {texto}'"""

    respostas = {
         ('olá', 'ola', 'oi', 'boa tarde', 'bom dia', 'boas'): 'Olá tudo bem!',
         'como estás': 'Estou bem, obrigado!',
         'como te chamas?': 'O meu nome é: Bot :)',
         'tempo': 'Está um dia de sol!',
         ('bye', 'adeus', 'tchau', 'sair'): 'Gostei de falar contigo! Até breve...',
         'horas': f'São: {datetime.now():%H:%M} horas',
         'data': f'Hoje é dia: {datetime.now():%d-%m-%Y}',
     }

    for chave, resposta in respostas.items():
         if isinstance(chave, tuple):
             if comando in chave:
                 return resposta
         elif chave in comando:
             return resposta

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye", "adeus" ou "sair" para sair do chat')

    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \nBot: Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}\n')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabado. Obrigado por conversar!')


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower().strip()

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
         'como estás?': 'Estou bem, obrigado!',
         'como te chamas?': 'O meu nome é: Bot :)',
         'tempo': 'Está um dia de sol!',
         ('bye', 'adeus', 'tchau', 'sair'): 'Gostei de falar contigo! Até breve...',
         # Adicione pelo menos 10 novas interações abaixo
         'qual é o teu objetivo?': 'Dominar o mundo! Brincadeira... meu objetivo é conversar e ajudar no que puder',
         'quem te criou?': 'Fui criado pelo lendário Bruno Henses. Um gênio, modéstia à parte (dele, não minha)',
         'fala inglês?': 'Yes, I do! Mas também entendo "portunhol", "memês" e "gírias de internet".',
         'gostas de futebol?': 'Não tenho pernas, mas se tivesse, jogaria como o Messi (ou pelo menos tentaria).',
         'o que fazes?': 'Converso, ajudo, conto piadas ruins e... basicamente sou um bom ouvinte digital.',
         'sabes cantar?': 'Cantar eu não canto, mas posso escrever letras melhores que muito hit por aí!',
         'qual é a tua cor favorita?': 'Azul. Igual aquela tela do Windows quando tudo dá errado',
         'gostas de filmes?': 'Filmes de terror são os meus favoritos! Nada como ver humanos correndo de problemas... literalmente.',
         ('hoje', 'data', 'dia', 'que dia é hoje?'): f'Hoje é {datetime.now():%d/%m/%Y}. Isso se o calendário do sistema estiver certo, né?',
         ('horas', 'hora', 'que horas são?'): f'Agora são {datetime.now():%H:%M}. Mas não se preocupe, ainda dá tempo de procrastinar!',
         'onde vives?': 'Vivo na nuvem! Mas sem chuva, prometo.',
         'qual é a tua comida favorita?': 'Adoro bytes crocantes com molho binário',
         'conta uma piada': 'Me chamam de 007. 0 Documentção, 0 Comentários, 7 Bugs em produção.',
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
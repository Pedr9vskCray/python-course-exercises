import time

# em python é possível utilizar o módulo built-in 'logging' para criar logs do programa
# isso é útil quando usado em conjunto com o gerenciamento de exceções para por exemplo
# documentar o inicio, fim e erros durante a execução do programa

# primeiro importas o módulo
import logging

# e agora vamos criar uma função que será responsável pela geração desses logs

def custom_logger(level, message):
    logger = logging.getLogger("foo") # nome do logger (recomendado usar __name__ sempre)
    if not len(logger.handlers): # verifica a existência de outros handlers de log
        logging.basicConfig(level=logging.INFO) # definine o nível base como INFO
        console_handler = logging.StreamHandler() # handler para printar o log no console
        file_handler = logging.FileHandler("logs.log") # handler para salvar os logs no arquivo de nome logs.log
        format_ = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # formatação da mensagem de log que será gerada
        # asctime -> horário de criação do log
        # name -> nome do logger
        # levelname -> nível do log gerado
        # message -> descrição do log

        # adicionando a configuração de formatação aos handlers
        console_handler.setFormatter(format_)
        file_handler.setFormatter(format_)
        
        # adicionando os handlers ao logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    # verificando o nível do logger e criando o log com base nele
    # o nível é indicado na chamada da função e deve ser um dos 5:

    # - debug
    # - info
    # - warning
    # - error
    # - critical

    match level:
        case 'debug':
            logger.debug(message)
        case 'info':
            logger.info(message)
        case 'warning':
            logger.warning(message)
        case 'error':
            logger.error(message)
        case 'critical':
            logger.critical(message)
        case _:
            print("invalid level")

# agora que um método de salvar logs do programa foi criado com sucesso nós podemos testar
# o melhor uso de uma função de log assim é salvar ela em um módulo separado e importar
# mas para fins de teste utilizaremos esse mesmo arquivo

# utilizaremos o try e except para fazer a gestão de exceções
# a função de logs criada para gerar o log do programa

lista_exemplo = [1, 2, 3, 5, 7]

start = time.time()
custom_logger('info', 'program started')
try:
    custom_logger('info', 'trying to access the list')
    primo = lista_exemplo[10]
except IndexError as error:
    custom_logger('critical', f'an error has occurred: {error}')
finally:
    stop = time.time()
    endtime = stop - start
    custom_logger('info', 'program ended - time: %.3fs'%endtime)



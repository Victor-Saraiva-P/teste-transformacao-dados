from data_transformation.pdf_extractor import extrair_dados_pdf
from logger_config import logger


def executar_data_transformation():
    """
    Executa o processo completo de transformação de dados: extrai dados do PDF,
    transforma em formato estruturado, salva em CSV e compacta o arquivo.

    Returns:
        bool: True se o processo foi concluído com sucesso, False caso contrário.
    """

    try:
        logger.info("Iniciando processo de Transformação de dados")
        # TODO: extrair dados
        dados_pdf = extrair_dados_pdf()
        print(dados_pdf)
        # TODO: transformar dados

        # TODO: salvar csv

        # TODO: compactar csv

        logger.info("Processo de web scraping concluído com sucesso.")
        return True

    except Exception as e:
        logger.error(f"Erro no processo de transformação de dados: {e}")
        return False

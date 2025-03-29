from data_transformation.compressor import compactar_arquivos
from data_transformation.pdf_extractor import extrair_dados_pdf
from data_transformation.to_csv import salvar_csv
from data_transformation.to_data_frame import transformar_dados_data_frame
from logger_config import logger


def executar_data_transformation():
    """
    Executa o processo completo de transformação de dados: extrai dados do PDF,
    transforma em formato estruturado, salva em CSV e compacta o arquivo.

    Returns:
        bool: True se o processo foi concluído com sucesso, False caso contrário.
    """

    try:
        logger.info("Iniciando processo de transformação de dados")

        # Extrai os dados do PDF
        dados_pdf = extrair_dados_pdf()

        if not dados_pdf:
            logger.error("Nenhum dado extraído do PDF.")
            return False

        # Transforma os dados extraídos em um DataFrame estruturado
        logger.info("Transformando dados em DataFrame estruturado")
        dados_data_frame = transformar_dados_data_frame(dados_pdf)

        # Salva o DataFrame em CSV
        caminho_csv = salvar_csv(dados_data_frame)
        if not caminho_csv:
            logger.error("Falha ao salvar o arquivo CSV.")
            return False

        # Compacta o arquivo CSV
        logger.info("Compactando arquivos gerados")
        caminho_compactado = compactar_arquivos()
        if not caminho_compactado:
            logger.warning("Não foi possível compactar os arquivos, mas o CSV foi gerado.")
        else:
            logger.info(f"Arquivo compactado gerado em: {caminho_compactado}")

        logger.info("Processo de transformação de dados concluído com sucesso.")
        return True

    except Exception as e:
        logger.error(f"Erro no processo de transformação de dados: {e}")
        return False
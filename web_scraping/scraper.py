from logger_config import logger
from web_scraping.downloader import baixar_arquivos
from web_scraping.extractor import extrair_links
from web_scraping.siteConnector import entrar_site


def executar_web_scraping():
    """
    Executa o processo completo de web scraping: acessa o site, extrai links,
    baixa os arquivos e realiza a compactação.

    Returns:
        bool: True se o processo foi concluído com sucesso, False caso contrário.
    """
    try:
        logger.info("Iniciando processo de web scraping")
        pagina_html = entrar_site()
        links = extrair_links(pagina_html)

        if not links:
            logger.error("Nenhum link encontrado para download.")
            return False

        arquivos_baixados = baixar_arquivos(links)

        if not arquivos_baixados:
            logger.error("Nenhum arquivo foi baixado.")
            return False

        return True

    except Exception as e:
        logger.error(f"Erro no processo de web scraping: {e}")
        return False

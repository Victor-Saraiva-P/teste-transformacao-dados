import sys

from logger_config import logger
from web_scraping.scraper import executar_web_scraping

if __name__ == "__main__":
    try:
        # Executar web scraping
        if not executar_web_scraping():
            logger.error("Web scraping falhou. Interrompendo execução.")
            sys.exit(1)

        # TODO: Executar transformação de dados

    except Exception as e:
        logger.critical(f"Erro crítico na execução do script: {e}")
        sys.exit(1)
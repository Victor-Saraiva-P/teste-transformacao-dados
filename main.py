import sys

from data_transformation.transformation import executar_data_transformation
from logger_config import logger
from web_scraping.scraper import executar_web_scraping

if __name__ == "__main__":
    try:
        # Executar web scraping
        if not executar_web_scraping():
            logger.error("Web scraping falhou. Interrompendo execução.")
            sys.exit(1)

        if not executar_data_transformation():
            logger.error("Transformação de dados falhou. Interrompendo execução.")
            sys.exit(1)

    except Exception as e:
        logger.critical(f"Erro crítico na execução do script: {e}")
        sys.exit(1)
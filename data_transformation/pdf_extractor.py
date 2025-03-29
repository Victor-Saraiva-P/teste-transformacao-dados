from pathlib import Path

import pdfplumber

from logger_config import logger
from config import PAGINA_FINAL, PAGINA_INICIAL, NOME_ARQUIVO_PDF, PASTA_DOWNLOADS, PASTA_ARQUIVOS


def extrair_dados_pdf():
    """
    Extrai os dados do PDF do Anexo I baixado pelo web scraping,
    processando apenas as páginas definidas pelas constantes PAGINA_INICIAL e PAGINA_FINAL.

    Returns:
        list: Lista de linhas extraídas da tabela única do PDF.
    """
    logger.info("Iniciando extração de dados do PDF")

    # Caminho para o arquivo PDF do Anexo I
    caminho_pdf = Path(PASTA_DOWNLOADS) / PASTA_ARQUIVOS / NOME_ARQUIVO_PDF
    if not caminho_pdf.exists():
        logger.error(f"Arquivo {caminho_pdf} não encontrado.")
        raise FileNotFoundError(f"O arquivo {caminho_pdf} não foi encontrado.")

    logger.info(f"Abrindo PDF em: {caminho_pdf}")

    dados_tabelas = []
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            total_paginas = len(pdf.pages)
            logger.info(f"PDF aberto com {total_paginas} páginas")

            # Definição do intervalo de páginas com base nas constantes
            pagina_inicial = PAGINA_INICIAL if PAGINA_INICIAL is not None else 1
            pagina_final = PAGINA_FINAL if PAGINA_FINAL is not None else total_paginas

            # --- Validações Inseridas Aqui ---
            if pagina_inicial < 1 or pagina_final < 1:
                raise ValueError("PAGINA_INICIAL e PAGINA_FINAL devem ser maiores ou iguais a 1.")
            if pagina_inicial > pagina_final:
                raise ValueError("PAGINA_INICIAL não pode ser maior que PAGINA_FINAL.")
            if pagina_final > total_paginas:
                raise ValueError(f"PAGINA_FINAL ({pagina_final}) é maior que o número total de páginas ({total_paginas}).")
            # --- Fim das Validações ---

            logger.info(f"Processando páginas de {pagina_inicial} a {pagina_final}")

            for num_pagina in range(pagina_inicial, pagina_final + 1):
                pagina = pdf.pages[num_pagina - 1]
                logger.debug(f"Processando página {num_pagina} de {total_paginas}")

                # Extrai as tabelas da página atual
                tabelas = pagina.extract_tables()

                if tabelas:
                    logger.debug(f"Encontradas {len(tabelas)} tabelas na página {num_pagina}")
                    # Concatena todas as linhas de todas as tabelas (PDF contém uma única grande tabela)
                    for tabela in tabelas:
                        for linha in tabela:
                            if any(cell and cell.strip() for cell in linha):
                                dados_tabelas.append(linha)
                else:
                    logger.debug(f"Nenhuma tabela encontrada na página {num_pagina}")

        logger.info(f"Extração concluída. Total de {len(dados_tabelas)} linhas extraídas.")
        return dados_tabelas

    except Exception as e:
        logger.error(f"Erro ao extrair dados do PDF: {e}", exc_info=True)
        raise Exception(f"Falha ao extrair dados do PDF: {e}")

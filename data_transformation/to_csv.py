import pandas as pd
import logging
from pathlib import Path

from config import NOME_ARQUIVO_CSV, PASTA_DOWNLOADS

logger = logging.getLogger(__name__)

def salvar_csv(df: pd.DataFrame) -> Path:
    """
    Salva o DataFrame em um arquivo CSV no diretório especificado.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados transformados.
    Returns:
        Path: Caminho completo do arquivo CSV gerado.
    """
    # Garante que a pasta de destino existe
    destino = Path(PASTA_DOWNLOADS)
    destino.mkdir(parents=True, exist_ok=True)

    # Constrói o caminho completo do arquivo CSV
    csv_path = destino / NOME_ARQUIVO_CSV

    try:
        df.to_csv(csv_path, index=False, encoding='utf-8')
        logger.info(f"CSV salvo em: {csv_path.resolve()}")
        return csv_path
    except Exception as e:
        logger.error(f"Erro ao salvar CSV: {e}", exc_info=True)
        raise

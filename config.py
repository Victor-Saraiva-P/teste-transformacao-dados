import os
from pathlib import Path

# =============================================================================
# Configurações Gerais
# =============================================================================

# Diretorio raiz do projeto (diretorio pai do diretório atual)
ROOT_DIR = Path(__file__).parent.absolute()

# URL base para acesso à ANS
URL_BASE_ANS = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# =============================================================================
# Configurações para Busca de Anexos
# =============================================================================

ANEXOS_CONFIG = {
    "Anexo_I.pdf": {
        "patterns": ["anexo i", "anexo_i"],
        "required_extension": ".pdf"
    },
}

# =============================================================================
# Configurações de Requisições
# =============================================================================

DELAY_ENTRE_REQUESTS = 1        # Delay entre requisições (em segundos)
REQUEST_TIMEOUT = 30           # Timeout para requisições (em segundos)

# =============================================================================
# Configurações de Download
# =============================================================================

# Diretórios para download
PASTA_DOWNLOADS = os.path.join(ROOT_DIR, 'downloads')   # Pasta base para downloads
PASTA_ARQUIVOS_PDF = "pdf"      # Subpasta onde os arquivos serão salvos
PASTA_ARQUIVOS_CSV = "csv"          # Subpasta onde os anexos serão salvos

# Parâmetros de download
MAX_PARALELO = 2               # Número máximo de downloads paralelos
MAX_TENTATIVAS = 3             # Número máximo de tentativas de download
DELAY_ENTRE_TENTATIVAS = 5     # Delay entre tentativas de download (em segundos)

# Flags de comportamento no download
LIMPAR_PASTA_DOWNLOADS = False   # Se True, limpa a pasta de downloads antes de iniciar
SOBRESCREVER_ARQUIVOS = False     # Se True, sobrescreve arquivos existentes
DOWNLOAD_PARALELO = True         # Se True, realiza downloads em paralelo

# =============================================================================
# Configurações de Compactação
# =============================================================================

SOBRESCREVER_COMPACTACAO = False  # Se True, sobrescreve arquivo compactado existente
FORMATO_COMPACTACAO = "zip"      # Formato de compactação: opções suportadas ("zip", "tar", "tar.gz", "tar.bz2", "7z")
NOME_ARQUIVO_COMPACTADO = "Teste_Victor_Alexandre_Saraiva_Pimentel"  # Nome base para o arquivo compactado

# =============================================================================
# Configurações de Transformação de Dados
# =============================================================================

NOME_ARQUIVO_PDF = "Anexo_I.pdf"  # Nome do arquivo PDF a ser transformado
PAGINA_INICIAL = 3  # Página inicial a ser processada
PAGINA_FINAL = 5  # Página final a ser processada

# Cabeçalho oficial esperado (13 colunas)
HEADER_CSV = [
    "PROCEDIMENTO",
    "RN\n(alteração)",
    "VIGÊNCIA",
    "OD",
    "AMB",
    "HCO",
    "HSO",
    "REF",
    "PAC",
    "DUT",
    "SUBGRUPO",
    "GRUPO",
    "CAPÍTULO"
]

NOME_ARQUIVO_CSV = "Anexo_I.csv"  # Nome do arquivo CSV a ser salvo
import pandas as pd

from config import HEADER_CSV


def transformar_dados_data_frame(dados_pdf):
    """
    Transforma a lista de linhas extraídas do PDF em um DataFrame estruturado,
    removendo cabeçalhos repetidos e renomeando colunas conforme solicitado.

    Args:
        dados_pdf (list of list): Dados extraídos do PDF (cada sublista é uma linha da tabela).

    Returns:
        pd.DataFrame: DataFrame com as colunas formatadas e dados limpos.
    """
    # Armazenará as linhas válidas (excluindo as que são só repetições do header)
    data_rows = []

    for linha in dados_pdf:
        # Verifica se a linha tem exatamente 13 colunas
        if len(linha) == 13:
            # Se for a linha de cabeçalho repetida, ignoramos
            if linha == HEADER_CSV:
                continue
            # Caso contrário, é uma linha de dados válida
            data_rows.append(linha)

    # Se não encontrou nenhuma linha válida, possivelmente o PDF não está no formato esperado
    if not data_rows:
        raise ValueError("Não foram encontradas linhas de dados válidas após filtrar o cabeçalho.")

    # Cria o DataFrame usando o cabeçalho oficial
    df = pd.DataFrame(data_rows, columns=HEADER_CSV)

    # Ajusta "RN\n(alteração)" para "RN (alteração)" no nome da coluna
    df.rename(columns={"RN\n(alteração)": "RN (alteração)"}, inplace=True)

    # Renomeia as colunas OD e AMB para seus significados completos
    df.rename(columns={
        "OD": "Odontologia",
        "AMB": "Ambulatorial"
    }, inplace=True)

    return df

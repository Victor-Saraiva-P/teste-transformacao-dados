![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![pdfplumber](https://img.shields.io/badge/pdfplumber-FF5A5F?style=for-the-badge&logo=&logoColor=white)
![Zipfile](https://img.shields.io/badge/Zipfile-BDBDBD?style=for-the-badge&logo=&logoColor=black)
# Teste de Transformação de Dados


Este projeto transforma dados do PDF do Anexo I (obtido através do [Teste de Web Scraping](https://github.com/Victor-Saraiva-P/teste-web-scraping)) em uma tabela estruturada e organizada.
## Stack Utilizada

- **Linguagem:** Python 3
- **Bibliotecas:**
  - `pdfplumber` – Para extração dos dados da tabela no PDF.
  - `pandas` – Para manipulação dos dados e criação da tabela.
  - `zipfile` – Biblioteca padrão do Python para compactação de arquivos.
- **Outros repositórios**
    - uma adaptação de [Teste de Web Scraping](https://github.com/Victor-Saraiva-P/teste-web-scraping)
## Funcionalidades

- **Extração de Dados do PDF:**  
  Utiliza `pdfplumber` para extrair tabelas de dados de procedimentos e eventos em saúde do Anexo I.

- **Transformação Estruturada:**  
  Organiza os dados em um DataFrame, realiza limpeza e formatação, e substitui abreviações como "OD" (Odontologia) e "AMB" (Ambulatorial) por seus significados completos.

- **Exportação para CSV:**  
  Salva o DataFrame resultante em formato CSV com codificação UTF-8 para preservar caracteres especiais.

- **Compactação Automática:**  
  Compacta o CSV gerado em um arquivo ZIP, facilitando o compartilhamento.

- **Sistema de Logs:**  
  Fornece logs detalhados de cada etapa do processo para facilitar monitoramento e depuração.
  ## Estrutura do Projeto

```
teste-transformacao-dados/
├── data_transformation/        # Módulos para transformação de dados
│   ├── compressor.py          # Compactação de arquivos
│   ├── pdf_extractor.py       # Extração de dados do PDF
│   ├── to_csv.py              # Conversão para CSV
│   ├── to_data_frame.py       # Transformação em DataFrame
│   └── transformation.py      # Processo principal de transformação
├── web_scraping/              # Módulos para web scraping
│   ├── downloader.py          # Download de arquivos
│   ├── extractor.py           # Extração de links
│   ├── scraper.py             # Processo principal de scraping
│   └── siteConnector.py       # Conexão com o site
├── downloads/                 # Pasta onde são salvos os arquivos
│   └── arquivos/              # PDF do Anexo I e arquivos CSV
├── config.py                  # Configurações globais
├── web_scraping_config.py     # Configurações do web scraping
└── logger_config.py           # Configurações de logging
```
## Rodando Localmente

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/teste-transformacao-dados.git
   cd teste-transformacao-dados
   ```

2. **Crie um Ambiente Virtual e Instale as Dependências:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure o Sistema (Opcional):**  
   Edite `config.py` e `web_scraping_config.py` para ajustar caminhos, nomes de arquivo ou outros parâmetros.

4. **Execute o Script Principal:**

   ```bash
   python main.py
   ```

5. **Verifique os Resultados:**
   - O CSV gerado será salvo no diretório `downloads/arquivos/`
   - O arquivo ZIP resultante será salvo em `downloads/`
   - Consulte os logs para acompanhar o processo
## 👨‍💻 Autor

Desenvolvido por **[Victor Saraiva](https://github.com/Victor-Saraiva-P)**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![pdfplumber](https://img.shields.io/badge/pdfplumber-FF5A5F?style=for-the-badge&logo=&logoColor=white)
![Zipfile](https://img.shields.io/badge/Zipfile-BDBDBD?style=for-the-badge&logo=&logoColor=black)
# Teste de Transformação de Dados

Este projeto tem como objetivo transformar os dados do PDF do Anexo I (obtido no **[Teste de Web Scraping](https://github.com/Victor-Saraiva-P/teste-web-scraping))** em uma tabela estruturada.

## Stack Utilizada

- **Linguagem:** Python 3
- **Bibliotecas:**
  - `pdfplumber` – Para extração dos dados da tabela no PDF.
  - `pandas` – Para manipulação dos dados e criação da tabela.
  - `zipfile` – Biblioteca padrão do Python para compactação de arquivos.
- **Outros repositórios**
    - uma adaptação de [Teste de Web Scraping](https://github.com/Victor-Saraiva-P/teste-web-scraping)

  ## Funcionalidades

- **Extração dos Dados do PDF:**  
  Utiliza `pdfplumber` para ler todas as páginas do PDF do Anexo I e extrair a tabela com os dados de procedimentos e eventos em saúde.

- **Transformação dos Dados:**  
  Organiza os dados extraídos em um DataFrame do Pandas, realizando limpeza e formatação dos dados, e substitui as abreviações das colunas OD e AMB por suas descrições completas (segundo a legenda no rodapé do PDF).

- **Exportação e Compactação:**  
  Salva o DataFrame resultante em formato CSV e, em seguida, compacta o CSV em um arquivo ZIP com o nome `Teste_{seu_nome}.zip`.

- **Logging Detalhado:**  
  O sistema registra o andamento de cada etapa para facilitar o monitoramento e a depuração.
## Estrutura do Projeto

- `downloads` – Pasta onde serão salvos o PDF do Anexo I (em /arquivos) e o arquivo compactado
- `web_scraping` – Cópia adaptada do código de web scraping original
- `web_scraping_config.py` – Configurações específicas do web scraping (adaptadas para Anexo I).
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
   Edite `config.py` se precisar ajustar os caminhos, nomes de arquivo ou outros parâmetros.

4. **Execute o Script:**

   ```bash
   python transformador.py
   ```

5. **Verifique os Resultados:**

   - O CSV com os dados transformados será salvo no diretório configurado.
   - O arquivo compactado `Teste_{seu_nome}.zip` será gerado conforme o especificado.
   - Consulte os logs para acompanhar o andamento do processo.
## 👨‍💻 Autor

Desenvolvido por **[Victor Saraiva](https://github.com/Victor-Saraiva-P)**

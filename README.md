# OracleDBManager

\`OracleDBManager\` é uma classe Python para gerenciar operações comuns em um banco de dados Oracle. Ela encapsula funcionalidades como criação de tabelas, execução de ações e listagem de colunas/tabelas.

## Pré-requisitos

- Python 3.x
- Bibliotecas: \`oracledb\`, \`os\`, \`dotenv\`, \`time\`, \`colorama\`

## Instalação

1. Clone este repositório:
   \```bash
   git clone [URL_DO_REPOSITORIO]
   \```

2. Navegue até o diretório do projeto e instale as dependências:
   \```bash
   pip install -r requirements.txt
   \```

## Configuração

Antes de usar a classe \`OracleDBManager\`, você precisa configurar suas credenciais e informações de conexão. Isso é feito através de um arquivo \`.env\` e baixar a wallet de credencial.

### Wallet Autonomous Database Oracle

Antes de utilizar a classe OracleDBManager, é essencial que você baixe a "wallet" de credenciais do banco de dados Oracle. A "wallet" é um conjunto de arquivos fornecidos pela Oracle que contém informações de segurança e configuração necessárias para estabelecer uma conexão segura. Ela é disponibilizada como um arquivo ZIP. Após o download, extraia o conteúdo desse arquivo ZIP na pasta \`Wallet_Oracle\` localizada no diretório raiz do projeto.

### Criando o arquivo \`.env\`

No diretório raiz do projeto, crie um arquivo chamado \`.env\`. Este arquivo deve conter as seguintes variáveis:

\```env
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_DSN=seu_dsn
DB_WALLET_PASSWORD=sua_senha_wallet
\```

Substitua \`seu_usuario\`, \`sua_senha\`, \`seu_dsn\` e \`sua_senha_wallet\` pelos valores apropriados para sua configuração de banco de dados.

**Nota**: Nunca compartilhe seu arquivo \`.env\` ou divulgue suas credenciais. O arquivo \`.env\` deve ser adicionado ao \`.gitignore\` para garantir que não seja enviado acidentalmente ao GitHub.

## Uso

Aqui está um exemplo básico de como usar a classe \`OracleDBManager\`:

\```python
from oracledb_manager import OracleDBManager

db_manager = OracleDBManager()

# Exemplo de uso:
colunas = {
    "ID": "NUMBER",
    "NOME": "VARCHAR2(50)",
    "DADO": "VARCHAR2(50)"
}

db_manager.cria_tabela_se_nao_existe("TEST", colunas)
db_manager.lista_colunas("TEST")

db_manager.close()
\```

## Contribuição

Sinta-se à vontade para fazer fork, abrir issues e enviar pull requests. Todas as contribuições são bem-vindas!

# Um modelo de projetos web usando docker

## Como executar

- Crie um arquivo `.env` na raiz deste repositório e cole nele todo o conteúdo do bloco a baixo

```bash
DB_URL="postgresql+asyncpg://user:password@database:5432/db"
DB_USER="user"
DB_PASSWORD="password"
DB_HOST="database"
DB_PORT="5432"
DB_NAME="db"
TEST_DB_URL="sqlite+aiosqlite:///:memory:"
```

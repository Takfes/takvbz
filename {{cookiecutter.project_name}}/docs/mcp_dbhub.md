# Dual-database setup (PostgreSQL + MySQL) with DBHub MCP servers for VS Code integration.

## 🚁 Overview
- **mcp.json** configures **two DBHub MCP** Server-Sent-Event (SSE) servers
- **Docker-Compose** sets up **two DBHub containers** exposing MCP servers on ports 8081/8082
- Each connects to respective database using internal Docker networking
    - **PostgreSQL 15**: Port 5432, DBHub MCP on 8081
    - **MySQL 8.0**: Port 3306, DBHub MCP on 8082
- **Read-only access** enforced for safety

## 🚀 Quick Start

### 1. Start the Stack
```bash
docker-compose up -d
```

### 2. Query via MCP Tools
Use VS Code's MCP tools to query databases:
- PostgreSQL: `mcp_dbhub-pg_execute_sql`  
- MySQL: `mcp_dbhub-mysql_execute_sql`

### 3. Cleanup
```bash
# Stop containers, remove data
docker-compose down -v
```


## 🔧 How to Install

### 1. VS Code MCP Configuration (`.vscode/mcp.json`)
```json
{
  "mcpServers": {
    "dbhub-pg": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--transport", "stdio", "--dsn", "postgres://pokemon_user:pokemon_pass@localhost:5432/pokemon_db?sslmode=disable", "--readonly"]
    },
    "dbhub-mysql": {
      "command": "npx", 
      "args": ["-y", "@bytebase/dbhub", "--transport", "stdio", "--dsn", "mysql://pokemon_user:pokemon_pass@localhost:3306/pokemon_db", "--readonly"]
    }
  }
}
```

### 2. Create Docker-Compose
```yaml
services:
  # DBHub for PostgreSQL
  dbhub-pg:
    image: node:20-alpine
    container_name: dbhub_pg
    init: true
    depends_on:
      - postgres
    environment:
      - DBHUB_PG_DSN=${DBHUB_PG_DSN}
    command: >
      sh -lc "npx -y @bytebase/dbhub
      --transport http --port 8080
      --dsn \"${DBHUB_PG_DSN}\" --readonly"
    ports:
      - "${DBHUB_PG_PORT}:8080"
    restart: unless-stopped
    networks:
      - pokemon_network

  # DBHub for MySQL
  dbhub-mysql:
    image: node:20-alpine
    container_name: dbhub_mysql
    init: true
    depends_on:
      - mysql
    environment:
      - DBHUB_MYSQL_DSN=${DBHUB_MYSQL_DSN}
    command: >
      sh -lc "npx -y @bytebase/dbhub
      --transport http --port 8080
      --dsn \"${DBHUB_MYSQL_DSN}\" --readonly"
    ports:
      - "${DBHUB_MY_PORT}:8080"
    restart: unless-stopped
    networks:
      - pokemon_network

  # PostgreSQL Database (mock)
  # Remove this if you already have a PostgreSQL instance
  postgres:
    image: postgres:15-alpine
    container_name: pokemon_db
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "${POSTGRES_PORT}:5432"
    restart: unless-stopped
    networks:
      - pokemon_network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 30s

  # MySQL Database (mock)
  # Remove this if you already have a MySQL instance
  mysql:
    image: mysql:8.0
    container_name: pokemon_mysql
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    volumes:
      - mysql_data:/var/lib/mysql
    ports:
      - "${MYSQL_PORT}:3306"
    restart: unless-stopped
    networks:
      - pokemon_network
    command: --default-authentication-plugin=mysql_native_password
    healthcheck:
      test:
        [
          "CMD",
          "mysqladmin",
          "ping",
          "-h",
          "127.0.0.1",
          "-u",
          "${MYSQL_USER}",
          "-p${MYSQL_PASSWORD}",
        ]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 30s

volumes:
  postgres_data:
    driver: local
  mysql_data:
    driver: local

networks:
  pokemon_network:
    name: pokemon_network
```

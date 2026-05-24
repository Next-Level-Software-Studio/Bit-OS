#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <sqlite3.h>

#define DB_NAME "tradutor_bidirecional.db"

// Função auxiliar para converter uma string para minúsculas (equivalente ao .lower())
void para_minusculas(char *str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower((unsigned char)str[i]);
    }
}

// Inicializa o sistema, cria tabelas e índices
int inicializar_sistema() {
    sqlite3 *db;
    char *err_msg = 0;
    
    int rc = sqlite3.open(DB_NAME, &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Não foi possível abrir o banco de dados: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return 1;
    }

    // Otimizações de velocidade para o SQLite (WAL e Synchronous OFF)
    sqlite3_exec(db, "PRAGMA journal_mode = WAL;", 0, 0, &err_msg);
    sqlite3_exec(db, "PRAGMA synchronous = OFF;", 0, 0, &err_msg);

    // Criação da tabela
    const char *sql_table = "CREATE TABLE IF NOT EXISTS dicionario ("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "FHS TEXT NOT NULL,"
                            "NLFH TEXT NOT NULL);";
    
    rc = sqlite3_exec(db, sql_table, 0, 0, &err_msg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao criar tabela: %s\n", err_msg);
        sqlite3_free(err_msg);
        sqlite3_close(db);
        return 1;
    }

    // Criação dos índices para Bidirecionalidade rápida
    sqlite3_exec(db, "CREATE UNIQUE INDEX IF NOT EXISTS idx_fhs ON dicionario(FHS);", 0, 0, &err_msg);
    sqlite3_exec(db, "CREATE UNIQUE INDEX IF NOT EXISTS idx_nlfh ON dicionario(NLFH);", 0, 0, &err_msg);

    sqlite3_close(db);
    return 0;
}

// Função interna para buscar em uma coluna específica
// Retorna 1 se encontrar e aloca o resultado em 'resultado_out', retorna 0 se não encontrar
int _buscar_no_disco(const char *coluna_busca, const char *coluna_retorno, const char *termo, char *resultado_out, int max_len) {
    sqlite3 *db;
    sqlite3_stmt *res;
    int encontrado = 0;

    if (sqlite3.open(DB_NAME, &db) != SQLITE_OK) {
        sqlite3_close(db);
        return 0;
    }

    // Prepara a query dinamicamente de forma segura (colunas internas, não inputs do usuário)
    char sql[256];
    snprintf(sql, sizeof(sql), "SELECT %s FROM dicionario WHERE %s = ?;", coluna_retorno, coluna_busca);

    if (sqlite3_prepare_v2(db, sql, -1, &res, 0) == SQLITE_OK) {
        sqlite3_bind_text(res, 1, termo, -1, SQLITE_STATIC);
        
        if (sqlite3_step(res) == SQLITE_ROW) {
            const unsigned char *texto = sqlite3_column_text(res, 0);
            if (texto) {
                strncpy(resultado_out, (const char*)texto, max_len - 1);
                resultado_out[max_len - 1] = '\0'; // Garante o null-terminator
                encontrado = 1;
            }
        }
    }

    sqlite3_finalize(res);
    sqlite3_close(db);
    return encontrado;
}

// Função de Tradução Inteligente
// Escreve a resposta formatada em 'buffer_saida'
void traduzir(const char *palavra, char *buffer_saida, int max_len) {
    char termo[256];
    char resultado[256];
    
    // Copia e transforma em minúsculas (Tratamento simples, sem o strip avançado do Python)
    strncpy(termo, palavra, sizeof(termo) - 1);
    termo[sizeof(termo) - 1] = '\0';
    para_minusculas(termo);

    // 1. Tenta FHS -> NLFH
    if (_buscar_no_disco("FHS", "NLFH", termo, resultado, sizeof(resultado))) {
        snprintf(buffer_saida, max_len, "[FHS -> NLFH] %s = %s", palavra, resultado);
        return;
    }

    // 2. Tenta NLFH -> FHS
    if (_buscar_no_disco("NLFH", "FHS", termo, resultado, sizeof(resultado))) {
        snprintf(buffer_saida, max_len, "[NLFH -> FHS] %s = %s", palavra, resultado);
        return;
    }

    snprintf(buffer_saida, max_len, "Correspondência não encontrada.");
}

// Adiciona ou atualiza um par no dicionário
int adicionar_par(const char *valor_fhs, const char *valor_nlfh) {
    sqlite3 *db;
    sqlite3_stmt *res;
    
    if (sqlite3.open(DB_NAME, &db) != SQLITE_OK) {
        sqlite3_close(db);
        return 1;
    }

    char fhs_low[256], nlfh_low[256];
    strncpy(fhs_low, valor_fhs, sizeof(fhs_low) - 1); fhs_low[sizeof(fhs_low)-1] = '\0';
    strncpy(nlfh_low, valor_nlfh, sizeof(nlfh_low) - 1); nlfh_low[sizeof(nlfh_low)-1] = '\0';
    para_minusculas(fhs_low);
    para_minusculas(nlfh_low);

    const char *sql = "INSERT OR REPLACE INTO dicionario (FHS, NLFH) VALUES (?, ?);";
    
    int rc = sqlite3_prepare_v2(db, sql, -1, &res, 0);
    if (rc == SQLITE_OK) {
        sqlite3_bind_text(res, 1, fhs_low, -1, SQLITE_STATIC);
        sqlite3_bind_text(res, 2, nlfh_low, -1, SQLITE_STATIC);
        
        rc = sqlite3_step(res);
        if (rc != SQLITE_DONE) {
            fprintf(stderr, "Erro ao inserir par.\n");
        }
    }

    sqlite3_finalize(res);
    sqlite3_close(db);
    return (rc == SQLITE_DONE) ? 0 : 1;
}
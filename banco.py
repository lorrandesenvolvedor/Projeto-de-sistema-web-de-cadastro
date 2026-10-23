import sqlite3
banco = sqlite3.connect("banco.db")
cursor = banco.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS registros (
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    descricao_cliente TEXT NOT NULL
    )
""")

cursor.execute("PRAGMA table_info(registros)")
colunas = [coluna[1] for coluna in cursor.fetchall()]

if "descricao_cliente" not in colunas:
    cursor.execute("""
        ALTER TABLE registros
        ADD COLUMN descricao_cliente TEXT
    """)
banco.commit()
banco.close()
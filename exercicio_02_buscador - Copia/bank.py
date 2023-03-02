import sqlite3
from datetime import datetime, timedelta


def createTableBank():
    conexao = sqlite3.connect('pages.db')
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE paginas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        conteudo TEXT,
        data_atualizacao TEXT
    )''')

    conexao.commit()
    conexao.close()


def printTable():
    conexao = sqlite3.connect('pages.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM paginas")
    rows = cursor.fetchall()

    if rows == None:
        print('ssas')

    for row in rows:
        print(row)

    conexao.close()


def savePage(url, conteudo):
    agora = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    with sqlite3.connect('pages.db') as conexao:
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM paginas WHERE url = ?', (url,))
        registro = cursor.fetchone()

        if registro is None:
            cursor.execute('INSERT INTO paginas (url, conteudo, data_atualizacao) VALUES (?, ?, ?)', (url, conteudo, agora))
        else:
            ultima_atualizacao = datetime.fromisoformat(registro[2])
            if datetime.utcnow() - ultima_atualizacao >= timedelta(days=0):
                cursor.execute('UPDATE paginas SET conteudo = ?, data_atualizacao = ? WHERE url = ?', (conteudo, agora, url))

        conexao.commit()



def isPageAlredySaved(url):
    conexao = sqlite3.connect('pages.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM paginas WHERE url = ?', (url,))
    registro = cursor.fetchone()
    conexao.close()
    
    if registro is None:
        return False
    else:
        return True


def getHtml(url):
    conexao = sqlite3.connect('pages.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT conteudo FROM paginas WHERE url = ?', (url,))
    registro = cursor.fetchone()
    conexao.close()

    if registro is None:
        return None
    else:
        return registro[0]


def checkTableStructure():
    conexao = sqlite3.connect('pages.db')
    cursor = conexao.cursor()

    cursor.execute('PRAGMA table_info(paginas)')

    for coluna in cursor.fetchall():
        print(coluna)

    conexao.close()

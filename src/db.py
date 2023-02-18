import psycopg2

host = "localhost"
dbname = "petLovers"
user = "postgres"
password = "1234"
# sslmode = "require"

#inicia conexao
conn_string = "host={0} user={1} dbname={2} password={3}".format(host,user,dbname,password)

conn = psycopg2.connect(conn_string)
print("conexão deu bom")

cursor = conn.cursor()

def inserealgo(d1,d2):
    cursor.execute("insert into tabela (col1, col2) values (%s, %s);",(d1, d2))
    conn.commit()

#encerra conexao
# cursor.close()
# conn.close
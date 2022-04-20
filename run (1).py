import psycopg2
import configparser
from sql_queries import CreateTable_queries,DropTable_queries


def DropTables(cur, conn):

    for query in DropTable_queries:
        cur.execute(query)
        conn.commit()
        
def CreateTables(cur, conn):

    for query in CreateTable_queries:
        cur.execute(query)
        conn.commit()


        
        
def main():
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    
    DropTables(cur, conn)
    CreateTables(cur, conn)

    conn.close()




if __name__ == "__main__":
    main()
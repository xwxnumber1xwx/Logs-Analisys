import psycopg2

DBNAME = "news"

QUERY1 = 'select title, num from articles left join (select path, count(path) as num from log group by path order by num desc) as res on substring(path, 10) = slug limit 3;'
QUERY2 = ''
QUERY3 = ''

def getDB(query):
    """Return the database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result

if __name__ == "__main__":
    query = QUERY1
    print('select one query: \n')
    print('1 - What are the most popular three articles of all time?')
    print('2 - Who are the most popular article authors of all time?')
    print("3 - On which days did more than 1'%' of requests lead to errors?")
    input_number = input(' digit 1, 2 or 3:')
    if input_number == 2:
        query = QUERY2
    elif input_number == 3:
        query = QUERY3
    getDB(query)
import psycopg2

DBNAME = "news"

query = ''
QUERY1 = 'SELECT title, num FROM articles LEFT JOIN (SELECT path, count(path) as num FROM log GROUP BY path ORDER BY num desc) as res on substring(path, 10) = slug LIMIT 3;'
QUERY2 = 'SELECT name, sum(num) FROM authors, (SELECT author, title, num FROM articles LEFT JOIN (SELECT path, count(path) as num FROM log GROUP BY path ORDER BY num desc) as res on substring(path, 10) = slug) as aut WHERE author = id GROUP BY name ORDER BY sum desc LIMIT 1;'
QUERY3 = '''
CREATE OR REPLACE VIEW allrequests AS
    SELECT status, date(time) AS date FROM log;

CREATE OR REPLACE VIEW allrequests_day AS
    SELECT date, count(date) AS num
    FROM allrequests
    GROUP BY date
    ORDER BY date;

CREATE OR REPLACE VIEW errors AS
    SELECT status, date(time) AS date
    FROM log
    WHERE status LIKE '4%';

CREATE OR REPLACE VIEW errors_day AS
    SELECT date, count(date) AS num
    FROM errors
    GROUP BY date
    ORDER BY date;

CREATE OR REPLACE VIEW allrequests_err AS
    SELECT allrequests_day.date, allrequests_day.num AS tot_requests, err.num AS errors
    FROM allrequests_day
    LEFT JOIN (
        SELECT date, num FROM errors_day) AS err
    ON allrequests_day.date = err.date;

SELECT *, errors*100::double precision/tot_requests::double precision AS percentage
    FROM allrequests_err
    WHERE errors::double precision*100/tot_requests::double precision >= 1
    LIMIT 10;

'''


def getDB(query):
    """Return the database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    colnames = [desc[0] for desc in c.description]
    result = c.fetchall()
    db.close()
    print('\n\n')
    print(str(colnames))
    for res in result:
        text = '| '
        for r in res:
            text += str(r) + " | "
        print(text)
        print('')
    # print(result)
    print('\n\n')
    selectQuery('')


def selectQuery(msg):
    print('select one query: \n')
    print('1 - What are the most popular three articles of all time?')
    print('2 - Who are the most popular article authors of all time?')
    print("3 - On which days did more than 1'%' of requests lead to errors?")
    print('4 - for exit')
    if msg:
        print(msg)
    input_number = input('digit 1, 2, 3 or 4:')
    if input_number == 1:
        query = QUERY1
    elif input_number == 2:
        query = QUERY2
    elif input_number == 3:
        query = QUERY3
    elif input_number == 4:
        exit()
    else:
        selectQuery(
            '+++ please just write on number (1 to 4) and than press Enter +++')
    getDB(query)


if __name__ == "__main__":
    selectQuery('')

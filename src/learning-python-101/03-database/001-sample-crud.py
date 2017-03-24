import sqlite3


def insert(db, data):
    db.execute('insert into test(t1, i1) values (?, ?)', (data['t1'], data['i1']))
    db.commit()


def retrieve(db, t1):
    cursor = db.execute('select * from test where t1 = ?', (t1, ))
    return cursor.fetchone()


def update(db, data):
    db.execute('update test set i1 = ? where t1 = ?', (data['i1'], data['t1']))
    db.commit()


def delete(db, t1):
    db.execute('delete from test where t1 = ?', (t1, ))
    db.commit()


def get_all(db):
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print(row)


def main():
    db = sqlite3.connect('text.db')
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    print('Create rows')
    insert(db, dict(t1='one', i1=4))
    get_all(db)

if __name__ == '__main__':
    main()

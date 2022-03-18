import cx_Oracle as DB

def Database(sql,mode):
    host_name = 'localhost'
    oracle_port = 1521
    service_name = 'xe'
    a = DB.makedsn(host_name, oracle_port, service_name)
    con = DB.connect('test', 'test', a)
    csr = con.cursor()
    csr.execute(sql)
    if mode==0:
        csr.close()
        con.commit()
        con.close()
    else:
        b = csr.fetchall()
        csr.close()
        con.close()
        return b


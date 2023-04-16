#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
    user  = 'root',
    host = 'localhost'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[2]:


import mysql.connector

conn = mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023')

print(conn)
conn.close()


# In[4]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE MAHASISWA (
                    NIM VARCHAR(10) PRIMARY KEY,
                    Nama VARCHAR(30) NOT NULL,
                    Alamat VARCHAR(255) NOT NULL,
                    Mata_kuliah_yang_diikuti VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[5]:


# In[5]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE DOSEN (
                    NIP VARCHAR(20) PRIMARY KEY,
                    Nama_Dosen VARCHAR(50) NOT NULL,
                    Mata_kuliah_yang_diajar VARCHAR(50)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[6]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE MATA_KULIAH (
                    Kode_MK VARCHAR(10) NOT NULL,
                    Nama_MK VARCHAR(50) NOT NULL,
                    Waktu DATE,
                    Ruangan VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[7]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MAHASISWA (NIM, Nama, Alamat, Mata_kuliah_yang_diikuti)VALUES (%s, %s, %s, %s)"
val = [("VMH12345", "Shani", "Magetan", "APSI"),
       ("VMH12346", "Indira", "Bandung", "PBO"),
       ("VMH12347", "Natio", "Padang", "MIKRO", ),
       ("VMH12348", "Gracia", "Lampung", "PYTHON"),
       ("VMH12349", "Adit", "Palu", "STATISTIKA"), ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[8]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO DOSEN (NIP, Nama_Dosen, Mata_kuliah_yang_diajar)VALUES (%s, %s, %s)"
val = [("VD12345", "Melody", "APSI"),
       ("VD12346", "Beby", "PBO"),
       ("VD12347", "Kinal", "MIKRO"),
       ("VD12348", "Shania", "PYTHON"),
       ("VD12349", "Ayana", "STATISTIKA"), ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[9]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MATA_KULIAH (Kode_MK, Nama_MK, Waktu, Ruangan)VALUES (%s, %s, %s, %s)"
val = [("MK12345", "APSI", "2023-01-1", "Lab1"),
       ("MK12346", "PBO", "2023-02-2", "Lab2"),
       ("MK12347", "MIKRO", "2023-03-3", "Lab3"),
       ("MK12348", "PYTHON", "2023-04-4", "Lab1"),
       ("MK12349", "STATISTIKA", "2023-05-5", "Lab3"), ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[10]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()


sql = "SELECT   matkul.Nama_MK, mahasiswa.Nama, dosen.Nama_Dosen FROM MATA_KULIAH matkul    INNER JOIN MAHASISWA mahasiswa ON mahasiswa.Mata_kuliah_yang_diikuti = matkul.Nama_MK    INNER JOIN DOSEN dosen ON dosen.Mata_kuliah_yang_diajar = matkul.Nama_MK"

cursorObject.execute(sql)

result = cursorObject.fetchall()

for row in result:
    print(row)

dataBase.close()


# In[ ]:





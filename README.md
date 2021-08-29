Pysqleet is a Python wrapper around [sqleet](https://github.com/resilar/sqleet). It is a drop in replacement
for the standard libraries sqlite3. 

# Installation
```pip install pysqleet```

# Usage
The usage is the same as sqlite3 with a few differences.
1. You can pass the kwarg ```key=[bytes, str, None]``` to ```sqleet.connect()``` and ```sqleet.Connection```.
2. You can call ```connection.change_key(key: [bytes, str, None])``` to change the key on an already
   open database. Setting the key to None will decrypt the database, making it compatible with the traditional
   sqlite3 lib.
3. A new exception type ```sqleet.AuthenticationError(sqleet.DatabaseError)``` is exposed, 
   which is raised on authentication based errors.
   
### Example:
```python3
import sqleet


key = b"Key"
db_name = "test.sqlite3"

# Create a new encrypted db
con = sqleet.connect(db_name, key=key)
con.execute("create table test(col char);")
con.commit()
con.close()

# Try to open db with the wrong key, this fails
try:
    con = sqleet.connect(db_name, key="The wrong key")
except sqleet.AuthenticationError:
    print("Failed to open database")    


# Remove the encryption on the created database
con = sqleet.connect(db_name, key=key)
con.change_key(None)
con.close()
```

# Versioning
The versions (```sqleet.__version__```) first 2 places (major, minor) match the sqleet version used in the sources.
For example an sqleet version of 1.2.3 would have pysqleet version of 12.3. The last place (patch) is used
internally for pysqleet patches.

# Sources
Pysqleet mixes source code from the below sources, with any modifications being noted in the copyright header
at the beginning of the file.
- [CPython v3.6.14](https://github.com/python/cpython/releases/tag/v3.6.14) sqlite3 module. (
[C Sources](https://github.com/python/cpython/tree/9a0099d1bf14bce417370aae6d55527417cda354/Modules/_sqlite) (used for ext _sqleet),
[Python sources](https://github.com/python/cpython/tree/9a0099d1bf14bce417370aae6d55527417cda354/Lib/sqlite3) (used for sqleet py module) )
- [Sqleet v0.31.1](https://github.com/resilar/sqleet/releases/tag/v0.31.1) amalgamation

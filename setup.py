from distutils.core import setup, Extension
import sys
import os

sqleet_defines = [
    ("SQLITE_OMIT_LOAD_EXTENSION", "1"),
    ("SQLITE_USE_URI", "1"),
    ("PY_SSIZE_T_CLEAN", "1")
]

if sys.platform != "win32":
    sqleet_defines.append(('MODULE_NAME', '"sqleet"'))
else:
    sqleet_defines.append(('MODULE_NAME', '\\"sqleet\\"'))


_sqleet = Extension("_sqleet",
                   ["_sqleet/connection.c",
                    "_sqleet/cursor.c",
                    "_sqleet/microprotocols.c",
                    "_sqleet/module.c",
                    "_sqleet/prepare_protocol.c",
                    "_sqleet/row.c",
                    "_sqleet/statement.c",
                    "_sqleet/util.c",
                    "_sqleet/cache.c",
                    "_sqleet/sqleet.c"
                    ],
                    define_macros=sqleet_defines,
                    library_dirs=[os.getcwd()])


setup(name="pysqleet",
      ext_modules=[_sqleet],
      packages=["sqleet"])

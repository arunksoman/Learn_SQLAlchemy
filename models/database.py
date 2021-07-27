from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from tabulate import tabulate

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://phpmyadmin:root@localhost/db_sqlalchemy_tut"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def pretty_print(result_set):
    if isinstance(result_set, list) or isinstance(result_set, tuple):
        rows = []
        for index, obj in enumerate(result_set):
            if index == 0:
                # print("Here")
                header = [c_attr.key for c_attr in inspect(obj).mapper.column_attrs]
            row_tuple = [getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs]
            rows.append(row_tuple)
        print(tabulate(rows, headers=header, tablefmt="pretty"))

    else:
        obj = result_set
        # print(dir(inspect(obj).mapper))
        header = [c_attr.key for c_attr in inspect(obj).mapper.columns]
        print(header)
        rows = [[getattr(obj, c.key) for c in inspect(obj).mapper.columns]]
        print(tabulate(rows, headers=header, tablefmt="pretty"))

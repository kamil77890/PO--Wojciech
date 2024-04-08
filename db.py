from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://admin:admin@localhost:5432/po_db')

Session = sessionmaker(bind=engine)
session = Session()

with engine.connect() as con:
    query = """
    CREATE TABLE users (
        id INTEGER,
        name VARCHAR(100),
    )
    INSERT INTO users VALUES (1, 'Franciszek');
    SELECT * FROM users;
    """

statement = text(query)

result = con.execute(statement)
print(result.first())

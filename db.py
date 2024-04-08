from sqlalchemy import create_engine

engine = create_engine('postgresql://admin:admin@localhost:5432/po_db')

Session = sessionmarker(bind=engine)
session = Session()

query = """


"""

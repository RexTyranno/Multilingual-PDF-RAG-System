from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Float, ARRAY  

Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text_chunk = Column(Text)
    embedding = Column(ARRAY(Float))  

def get_engine(db_url='sqlite:///rag_documents.db'):
    engine = create_engine(db_url, echo=False)
    return engine

def init_db(engine):
    Base.metadata.create_all(engine)

def store_chunks(chunk_list: list, session):
    
    for chunk in chunk_list:
        doc = Document(text_chunk=chunk)
        session.add(doc)
    session.commit()

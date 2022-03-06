from flask import session
from sqlalchemy import Column, String, Integer, Date, insert
from Models.core_model import Base, Session

class MundialModel(Base):
    __tablename__ = 'mundials'
    id = Column(Integer, primary_key=True)
    pais_id = Column(Integer)
    anio = Column(Integer)
    campeon = Column(Integer)
    activo = Column(Integer)
    botin = Column(Integer)
    por = Column(Integer)
    dfi = Column(Integer)
    dfd = Column(Integer)
    li = Column(Integer)
    ld = Column(Integer)
    mi = Column(Integer)
    mc = Column(Integer)
    md = Column(Integer)
    ei = Column(Integer)
    dc = Column(Integer)
    ed = Column(Integer)

def get_all():
    session = Session()
    mundiales = session.query(MundialModel).all()
    data = [{
        'id' : item.id,
        'pais_id' : item.pais_id,
        'anio' : item.anio,
        'campeon' : item.campeon,
        'activo' : item.activo,
        'botin' : item.botin,
        'por' : item.por,
        'dfi' : item.dfi,
        'dfd' : item.dfd,
        'li' : item.li,
        'ld' : item.ld,
        'mi' : item.mi,
        'mc' : item.mc,
        'md' : item.md,
        'ei' : item.ei,
        'dc' : item.dc,
        'ed' : item.ed,
    } for item in mundiales ]
    return data

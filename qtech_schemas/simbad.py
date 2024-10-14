from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import  Integer, String
from qtech_schemas.dbo import Base
from typing import Optional

ARGS= {'schema': 'SIMBAD','extend_existing': True}

class TIPO_ENTIDAD(Base):
    __tablename__ = 'TIPO_ENTIDAD'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    tipo_entidad: Mapped[Optional[str]] = mapped_column('TIPO_ENTIDAD', String(100))

    def __repr__(self) -> str:
        return f"TIPO_ENTIDAD(ID={self.id!r}, TIPO_ENTIDAD={self.tipo_entidad!r})"
    
class ENTIDAD(Base):
    __tablename__ = 'ENTIDAD'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    entidad: Mapped[Optional[str]] = mapped_column('ENTIDAD', String(100))

    def __repr__(self) -> str:
        return f"ENTIDAD(ID={self.id!r}, ENTIDAD={self.entidad!r})"
    
class REGION(Base):
    __tablename__ = 'REGION'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    region: Mapped[Optional[str]] = mapped_column('REGION', String(100))

    def __repr__(self) -> str:
        return f"REGION(ID={self.id!r}, REGION={self.region!r})"
    
class PROVINCIA(Base):
    __tablename__ = 'PROVINCIA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    provincia: Mapped[Optional[str]] = mapped_column('PROVINCIA', String(100))

    def __repr__(self) -> str:
        return f"PROVINCIA(ID={self.id!r}, PROVINCIA={self.provincia!r})"
    
class PERSONA(Base):
    __tablename__ = 'PERSONA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    persona: Mapped[Optional[str]] = mapped_column('PERSONA', String(100))

    def __repr__(self) -> str:
        return f"PERSONA(ID={self.id!r}, PERSONA={self.persona!r})"
    
class GENERO(Base):
    __tablename__ = 'GENERO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    genero: Mapped[Optional[str]] = mapped_column('GENERO', String(100))

    def __repr__(self) -> str:
        return f"GENERO(ID={self.id!r}, GENERO={self.genero!r})"
    
class TIPO_CLIENTE(Base):
    __tablename__ = 'TIPO_CLIENTE'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    tipo_cliente: Mapped[Optional[str]] = mapped_column('TIPO_CLIENTE', String(100))

    def __repr__(self) -> str:
        return f"TIPO_CLIENTE(ID={self.id!r}, TIPO_CLIENTE={self.tipo_cliente!r})"
    
class INSTRUMENTO_CAPTACION(Base):
    __tablename__ = 'INSTRUMENTO_CAPTACION'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    instrumento_captacion: Mapped[Optional[str]] = mapped_column('INSTRUMENTO_CAPTACION', String(100))

    def __repr__(self) -> str:
        return f"INSTRUMENTO_CAPTACION(ID={self.id!r}, INSTRUMENTO_CAPTACION={self.instrumento_captacion!r})"
    
class MONEDA(Base):
    __tablename__ = 'MONEDA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    moneda: Mapped[Optional[str]] = mapped_column('MONEDA', String(100))

    def __repr__(self) -> str:
        return f"MONEDA(ID={self.id!r}, MONEDA={self.moneda!r})"
    
class DIVISA(Base):
    __tablename__ = 'DIVISA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    divisa: Mapped[Optional[str]] = mapped_column('DIVISA', String(100))

    def __repr__(self) -> str:
        return f"DIVISA(ID={self.id!r}, DIVISA={self.divisa!r})"
    
class PARTIDA_NIVEL_1(Base):
    __tablename__ = 'PARTIDA_NIVEL_1'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    partida_nivel_1: Mapped[Optional[str]] = mapped_column('PUBLICO_PRIVADO_NIVEL_1', String(100))

    def __repr__(self) -> str:
        return f"PARTIDA_NIVEL_1(ID={self.id!r}, PUBLICO_PRIVADO_NIVEL_1={self.partida_nivel_1!r})"
    
class PARTIDA_NIVEL_2(Base):
    __tablename__ = 'PARTIDA_NIVEL_2'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    partida_nivel_2: Mapped[Optional[str]] = mapped_column('PARTIDA_NIVEL_2', String(100))

    def __repr__(self) -> str:
        return f"PARTIDA_NIVEL_2(ID={self.id!r}, PARTIDA_NIVEL_2={self.partida_nivel_2!r})"
    
class PUBLICO_PRIVADO_1(Base):
    __tablename__ = 'PUBLICO_PRIVADO_1'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    publica_privado_1: Mapped[Optional[str]] = mapped_column('PUBLICO_PRIVADO_NIVEL_1', String(100))

    def __repr__(self) -> str:
        return f"PUBLICO_PRIVADO_1(ID={self.id!r}, PUBLICO_PRIVADO_NIVEL_1={self.publica_privado_1!r})"
    
class PUBLICO_PRIVADO_2(Base):
    __tablename__ = 'PUBLICO_PRIVADO_2'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    publica_privado_2: Mapped[Optional[str]] = mapped_column('PUBLICO_PRIVADO_NIVEL_2', String(100))

    def __repr__(self) -> str:
        return f"PUBLICO_PRIVADO_2(ID={self.id!r}, PUBLICO_PRIVADO_NIVEL_2={self.publica_privado_2!r})"
    
class RESIDENTE_NORESIDENTE(Base):
    __tablename__ = 'RESIDENTE_NORESIDENTE'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    residente_noresidente: Mapped[Optional[str]] = mapped_column('RESIDENTE_NO_NORESIDENTE', String(100))

    def __repr__(self) -> str:
        return f"RESIDENTE_NORESIDENTE(ID={self.id!r}, RESIDENTE_NO_NORESIDENTE={self.residente_noresidente!r})"
    
class COMPONENTE(Base):
    __tablename__ = 'COMPONENTE'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    componente: Mapped[Optional[str]] = mapped_column('COMPONENTE', String(100))

    def __repr__(self) -> str:
        return f"COMPONENTE(ID={self.id!r}, COMPONENTE={self.componente!r})"

class INSTRUMENTO_MEDIO(Base):
    __tablename__ = 'INSTRUMENTO_MEDIO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    instrumento_medio: Mapped[Optional[str]] = mapped_column('INSTRUMENTO_MEDIO', String(100))

    def __repr__(self) -> str:
        return f"INSTRUMENTO_MEDIO(ID={self.id!r}, INSTRUMENTO_MEDIO={self.instrumento_medio!r})"
    
class CONTRAPARTE(Base):
    __tablename__ = 'CONTRAPARTE'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    contraparte: Mapped[Optional[str]] = mapped_column('CONTRA_PARTE', String(100))

    def __repr__(self) -> str:
        return f"CONTRAPARTE(ID={self.id!r}, CONTRA_PARTE={self.contraparte!r})"
    
class SITUACION_NIVEL1(Base):
    __tablename__ = 'SITUACION_NIVEL1'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    situacion_nivel_1: Mapped[Optional[str]] = mapped_column('SITUACION_NIVEL_1', String(100))

    def __repr__(self) -> str:
        return f"SITUACION_NIVEL1(ID={self.id!r}, SITUACION_NIVEL_1={self.situacion_nivel_1!r})"
    
class SITUACION_NIVEL2(Base):
    __tablename__ = 'SITUACION_NIVEL2'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    situacion_nivel_2: Mapped[Optional[str]] = mapped_column('SITUACION_NIVEL_2', String(100))

    def __repr__(self) -> str:
        return f"SITUACION_NIVEL2(ID={self.id!r}, SITUACION_NIVEL_2={self.situacion_nivel_2!r})"
    
class FINANCIERO_NOFINANCIERO(Base):
    __tablename__ = 'FINANCIERO_NOFINANCIERO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    financiero_no_financiero: Mapped[Optional[str]] = mapped_column('FINANCIERO_NO_FINANCIERO', String(100))

    def __repr__(self) -> str:
        return f"FINANCIERO_NOFINANCIERO(ID={self.id!r}, FINANCIERO_NO_FINANCIERO={self.financiero_no_financiero!r})"
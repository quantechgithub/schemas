from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import  Integer, String, Float, Date, ForeignKey,Time,BigInteger
from qtech_schemas.dbo import Base
from typing import Optional,List
from pandas import Timestamp as time
from sqlalchemy.sql import func

ARGS= {'schema': 'MARKET','extend_existing': True}
class Amortiza(Base):
    __tablename__ = 'AMORTIZA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    amortiza: Mapped[str] = mapped_column('AMORTIZA', String(20))

    def __repr__(self) -> str:
        return f"User(ID={self.id!r}, AMORTIZA={self.amortiza!r},"

class Sector(Base):
    __tablename__ = 'SECTOR'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    sector: Mapped[Optional[str]] = mapped_column('SECTOR', String(100))

    def __repr__(self) -> str:
        return f"Sector(ID={self.id!r}, SECTOR={self.sector!r})"

class Emisor(Base):
    __tablename__ = 'EMISORES'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    siglas: Mapped[Optional[str]] = mapped_column('SIGLAS', String(100))
    nombre: Mapped[str] = mapped_column('NOMBRE', String(200))
    sector_id: Mapped[Optional[int]] = mapped_column('SECTOR_ID', Integer, ForeignKey(Sector.id))

    def __repr__(self) -> str:
        return f"Emisores(ID={self.id!r}, SIGLAS={self.siglas!r}, NOMBRE={self.nombre!r}, SECTOR={self.sector_id!r})"
    
class SerieEmision(Base):
    __tablename__ = 'SERIES_EMISION'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    siglas: Mapped[Optional[str]] = mapped_column('SIGLAS', String(100))
    nombre: Mapped[str] = mapped_column('NOMBRE', String(260))
    nombre_bvrd: Mapped[Optional[str]] = mapped_column('NOMBRE_BVRD', String(260))
    emisor_id: Mapped[int] = mapped_column('EMISOR_ID',ForeignKey(Emisor.id))

    def __repr__(self) -> str:
        return f"User(ID={self.id!r}, SIGLAS={self.siglas!r}, NOMBRE={self.nombre!r},NOMBRE_BVRD={self.nombre_bvrd!r},EMISOR_ID ={self.emisor_id!r})"

class Moneda(Base):
    __tablename__ = 'MONEDA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    moneda: Mapped[str] = mapped_column('MONEDA', String(30))

class ClaseInstrumento(Base):
    __tablename__ = 'CLASE_INSTRUMENTO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    clase: Mapped[str] = mapped_column('CLASE', String(30))

class TipoInstrumento(Base):
    __tablename__ = 'TIPO_INSTRUMENTO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    tipo_instrumento: Mapped[str] = mapped_column('TIPO_INSTRUMENTO', String(100))
    siglas: Mapped[Optional[str]] = mapped_column('SIGLAS',String(20))
    clase_instrumento: Mapped[Optional[int]] = mapped_column('CLASE_INSTRUMENTO_ID',Integer,ForeignKey(ClaseInstrumento.id)) 
    titulos : Mapped[List['Maestro']] = relationship(back_populates='tipo_instrumento')

class BasePago(Base):
    __tablename__ = 'BASE_PAGO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    base_pago: Mapped[str] = mapped_column('BASE_PAGO', String(100))

class Periodicidad(Base):
    __tablename__ = 'PERIODICIDAD_PAGO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    periodicidad: Mapped[str] = mapped_column('PERIODICIDAD_PAGO', String(50))
    periodicidad_bvrd: Mapped[Optional[str]] = mapped_column('PERIODICIDAD_BVRD', String(50))

class EmisorMoneda(Base):
    __tablename__ = 'EMISOR_MONEDA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    emisor_moneda: Mapped[str] = mapped_column('EMISOR_MONEDA', String(100))

    titulos : Mapped[List['Maestro']] = relationship(back_populates='emisor_moneda')

class MetodoCalculo(Base):
    __tablename__ = 'METODO_CALCULO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    metodo_calculo: Mapped[str] = mapped_column('METODO_CALCULO', String(100))

class TipoTasa(Base):
    __tablename__ = 'TIPO_TASA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    tipo: Mapped[str] = mapped_column('TIPO_TASA', String(50))

class TipoEmisor(Base):
    __tablename__ = 'TIPO_EMISOR'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    tipo: Mapped[str] = mapped_column('TIPO_EMISOR',String(50))

class TipoOperacion(Base):
    __tablename__= 'TIPO_OPERACIONES'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    tipo_operacion: Mapped[str] = mapped_column('TIPO_OPERACION',String(50))

class Parte(Base):
    __tablename__='PARTES'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    partes : Mapped[str] = mapped_column('PARTE',String(50))

class Sistema_Mercado(Base):
    __tablename__ = 'SISTEMA_MERCADO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    registro: Mapped[str] = mapped_column('REGISTRO',String(100))

class Estado(Base):
    __tablename__= 'ESTADO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    estados : Mapped[str] = mapped_column('ESTADOS',String(50))

class Mercado(Base):
    __tablename__= 'MERCADO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    mercado : Mapped[str] = mapped_column('MERCADO',String(50))


class Ranking(Base):
    __tablename__= 'RANKING'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    mercado: Mapped[int] = mapped_column('MERCADO',Integer,ForeignKey(Mercado.id))
    participante:Mapped[str] = mapped_column('PARTICIPANTE',String(50))
    actual:Mapped[int] = mapped_column('ACTUAL',BigInteger)
    ranking: Mapped[int] = mapped_column('RANKING',BigInteger)
    fechas: Mapped[time] = mapped_column('FECHA',Date)

    def __repr__(self) -> str:
        return f"User(ID={self.id!r}, MERCADO={self.mercado!r}, PARTICIPANTE={self.participante!r},ACTUAL={self.actual!r},RANKING ={self.ranking!r},FECHAS ={self.fechas!r})"
    
class Maestro(Base):
    __tablename__ = 'MAESTRO_TITULOS'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin: Mapped[str] = mapped_column('ISIN', String(100), unique=True)
    fecha_emision: Mapped[Optional[time]] = mapped_column('EMISION', Date)
    fecha_vencimiento: Mapped[Optional[time]] = mapped_column('VENCIMIENTO', Date)
    cupon: Mapped[Optional[float]] = mapped_column('CUPON', Float)
    amortiza_id: Mapped[Optional[int]] = mapped_column('AMORTIZA', Integer, ForeignKey(Amortiza.id))
    serie_id: Mapped[Optional[int]] = mapped_column('SERIES_ID', Integer, ForeignKey(SerieEmision.id))
    moneda_id: Mapped[Optional[int]] = mapped_column('MONEDA_ID', Integer, ForeignKey(Moneda.id))
    tipo_id: Mapped[Optional[int]] = mapped_column('TIPO_ID', Integer, ForeignKey(TipoInstrumento.id))
    base_id: Mapped[Optional[int]] = mapped_column('BASE_ID', Integer, ForeignKey(BasePago.id))
    periodicidad_id: Mapped[Optional[int]] = mapped_column('PERIODICIDAD_ID', Integer, ForeignKey(Periodicidad.id))
    monto_total_programa: Mapped[Optional[float]] = mapped_column('MONTO_TOTAL_PROGRAMA', Float)
    nemotecnico: Mapped[Optional[str]] = mapped_column('NEMOTECNICO', String(100))
    option_call: Mapped[Optional[int]] = mapped_column('OPTION_CALL', Integer)
    call_date: Mapped[Optional[time]] = mapped_column('CALL_DATE', Date)
    emisor_moneda_id: Mapped[Optional[int]] = mapped_column('EMISOR_MONEDA_ID', Integer, ForeignKey(EmisorMoneda.id))
    metodo_calculo_id: Mapped[Optional[int]] = mapped_column('METODO_CALCULO_ID', Integer, ForeignKey(MetodoCalculo.id))
    calificacion_riesgo:Mapped[Optional[str]] = mapped_column('CALIFICACION_RIESGO',String(50))
    tipo_tasa:Mapped[Optional[int]] = mapped_column('TIPO_TASA_ID',Integer,ForeignKey(TipoTasa.id))
    sobre_tasa : Mapped[Optional[float]] = mapped_column('SOBRE_TASA',Float)
    tipo_emisor: Mapped[Optional[int]] = mapped_column('TIPO_EMISOR',Integer,ForeignKey(TipoEmisor.id))   

    emisor_moneda : Mapped['EmisorMoneda'] = relationship(back_populates='titulos')
    tipo_instrumento : Mapped['TipoInstrumento'] = relationship(back_populates='titulos')
    emisor_moneda : Mapped['EmisorMoneda'] = relationship(back_populates='titulos')
    tipo_instrumento : Mapped['TipoInstrumento'] = relationship(back_populates='titulos')
    montos: Mapped[List['Monto']] = relationship('Monto', back_populates='titulo')

class VectorMonto(Base):
    __tablename__= 'VECTOR_MONTO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID',Integer,ForeignKey(Maestro.id))
    fecha: Mapped[Optional[time]] = mapped_column('FECHA',Date)
    monto_emitido: Mapped[Optional[float]] = mapped_column('MONTO_EMITIDO',Float)
    moneda: Mapped[Optional[float]] = mapped_column('MONEDA_ID',Integer,ForeignKey(Moneda.id))
    monto_circulante: Mapped[Optional[float]] = mapped_column('MONTO_CIRCULANTE',Float)

class Monto(Base):
    __tablename__ = 'MONTOS'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    fecha: Mapped[Optional[time]] = mapped_column('FECHA', Date)
    monto_emitido: Mapped[Optional[float]] = mapped_column('MONTO_EMITIDO', Float)
    monto_circulacion: Mapped[Optional[float]] = mapped_column('MONTO_CIRCULACION', Float)
    isin_id: Mapped[int] = mapped_column('ISIN_ID', Integer, ForeignKey(Maestro.id))

    titulo: Mapped['Maestro'] = relationship(back_populates='montos')

class SubastaCredito(Base):
    __tablename__ = 'SUBASTAS_CREDITO_PUBLICO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID',Integer,ForeignKey(Maestro.id))
    fecha_subasta: Mapped[Optional[time]] = mapped_column('FECHA_SUBASTA',Date)
    fecha_liquidacion: Mapped[Optional[time]] = mapped_column('FECHA_LIQUIDACION',Date)
    monto_ofertado: Mapped[Optional[float]] = mapped_column('MONTO_OFERTADO',Float)
    valor_nominal_recibido: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_RECIBIDO',Float)
    precio_promedio_ponderado: Mapped[Optional[float]] = mapped_column('PRECIO_PROMEDIO_PONDERADO',Float)
    tasa_promedio_ponderada: Mapped[Optional[float]] = mapped_column('TASA_PROMEDIO_PONDERADA',Float)
    valor_nominal_adjudicada: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_ADJUDICADA',Float)
    precio_adjudicacion: Mapped[Optional[float]] = mapped_column('PRECIO_DE_ADJUDICACION',Float)
    tasa_de_adjudicacion: Mapped[Optional[float]] = mapped_column('TASA_DE_ADJUDICACION',Float)
    valor_nominal_rechazado: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_RECHAZADO',Float)
    precio_promedio_ponderado_rechazado: Mapped[Optional[float]] = mapped_column('PRECIO_PROMEDIO_PONDERADO_RECHAZADO',Float)
    tasa_promedio_ponderado_rechazado: Mapped[Optional[float]] = mapped_column('TASA_PROMEDIO_PONDERADO_RECHAZADO',Float)

class SubastaBCRD(Base):
    __tablename__ = 'SUBASTAS_BCRD'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID',Integer,ForeignKey(Maestro.id))
    fecha_subasta: Mapped[Optional[time]] = mapped_column('FECHA_SUBASTA',Date)
    valor_nominal_recibido: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_RECIBIDO',Float)
    precio_de_oferta: Mapped[Optional[float]] = mapped_column('PRECIO_DE_LA_OFERTA',Float)
    valor_nominal_adjudicada: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_ADJUDICADA',Float)
    precio_de_corte: Mapped[Optional[Float]] = mapped_column('PRECIO_DE_CORTE',Float)
    precio_promedio_ponderado: Mapped[Optional[float]] = mapped_column('PRECIO_PROMEDIO_PONDERADO',Float)
    precio_rechazado:Mapped[Optional[float]] = mapped_column('PRECIO_RECHAZADO',Float)
    yield_promedio_ponderada_referencias_bcrd:Mapped[Optional[float]] = mapped_column('YIELD_PROMEDIO_PONDERADA_REFERENCIAS_BCRD')
    yield_oferta: Mapped[Optional[float]] = mapped_column('YIELD_OFERTA',Float)
    yield_corte: Mapped[Optional[float]] = mapped_column('YIELD_CORTE',Float)
    yield_promedio_ponderada: Mapped[Optional[Float]] = mapped_column('YIELD_PROMEDIO_PONDERADA',Float)
    yield_rechazada :Mapped[Optional[Float]]  = mapped_column('YIELD_RECHAZADA',Float)
    bid_to_cover: Mapped[Optional[float]] = mapped_column('BID_TO_COVER',Float)

class OperacionMM(Base):
    __tablename__ = 'OPERACIONES_MARKETMAKERS'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID',Integer,ForeignKey(Maestro.id))
    fecha_valor: Mapped[Optional[time]] = mapped_column('FECHA_VALOR',Date)
    cantidad_titulos: Mapped[Optional[int]] = mapped_column('CANTIDAD_TITULOS',Integer)
    valor_transado: Mapped[Optional[float]] = mapped_column('VALOR_TRANSDO',Float)
    dias_interes: Mapped[Optional[int]] = mapped_column('DIAS_INTERES',Integer)
    monto_interes: Mapped[Optional[float]] = mapped_column('MONTO_INTERES',Float)
    monto_limpio: Mapped[Optional[float]] = mapped_column('MONTO_LIMPIO',Float)
    precio_limpio: Mapped[Optional[float]] = mapped_column('PRECIO_LIMPIO',Float)
    rendimiento_vencimiento: Mapped[Optional[float]] = mapped_column('RENDIMIENTO_VENCIMIENTO')

class OperacionesCevaldom(Base):
    __tablename__= 'OPERACIONES_CEVALDOM'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    fisn: Mapped[str] = mapped_column('FISN',String(100))
    isin_id: Mapped[int] = mapped_column('ISIN_ID',Integer,ForeignKey(Maestro.id))
    monto_nominal_operacion: Mapped[Optional[int]]= mapped_column('MONTO_NOMINAL_OPERACION',BigInteger)
    moneda_id: Mapped[Optional[int]] = mapped_column('MONEDA_ID',Integer,ForeignKey(Moneda.id))
    cantidad_valores: Mapped[Optional[int]] = mapped_column('CANTIDAD_VALORES',BigInteger)
    _yield: Mapped[Optional[float]] = mapped_column ('YIELD',Float)
    precio_limpio: Mapped[Optional[float]] = mapped_column('PRECIO_LIMPIO',Float)
    fecha_pacto: Mapped[Optional[time]] = mapped_column('FECHA_PACTO',Date)
    hora_pacto : Mapped[Optional[time]] = mapped_column('HORA_PACTO',Time)
    tipo_operacion: Mapped[Optional[int]] = mapped_column('TIPO_OPERACION',Integer,ForeignKey(TipoOperacion.id))
    parte : Mapped[Optional[int]] = mapped_column('PARTE',Integer,ForeignKey('MARKET.PARTES.ID'))
    sistema_registro: Mapped[Optional[int]] = mapped_column('SISTEMA_REGISTRO_OTC_MERCADO',Integer,ForeignKey(Sistema_Mercado.id))
    fecha_liquidacion: Mapped[Optional[time]] = mapped_column('FECHA_LIQUIDACION',Date)
    estados: Mapped[Optional[int]] = mapped_column('ESTADOS',Integer,ForeignKey('MARKET.ESTADO.ID'))
    subida: Mapped[time] = mapped_column('SUBIDA', Date, server_default=func.now())

    vector_precio: Mapped['VectorPrecioOTC'] = relationship(back_populates='operacion')

class VectorPrecioOTC(Base):
    __tablename__= 'VECTOR_PRECIO_OTC'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    operacion_id: Mapped[int] = mapped_column(Integer, ForeignKey(OperacionesCevaldom.id))
    facial_value : Mapped[Optional[float]] = mapped_column(Float)
    traded_value : Mapped[Optional[float]] = mapped_column(Float)
    ytm : Mapped[Optional[float]] = mapped_column(Float)
    clean_price : Mapped[Optional[float]] = mapped_column(Float)
    dirty_price : Mapped[Optional[float]] = mapped_column(Float)
    theta : Mapped[Optional[float]] = mapped_column(Float)
    time : Mapped[Optional[float]] = mapped_column(Float)
    current_yield : Mapped[Optional[float]] = mapped_column(Float)
    mcauly_duration : Mapped[Optional[float]] = mapped_column(Float)
    mduration : Mapped[Optional[float]] = mapped_column(Float)
    convexity : Mapped[Optional[float]] = mapped_column(Float)
    coupon : Mapped[Optional[float]] = mapped_column(Float)
    dollar_duration : Mapped[Optional[float]] = mapped_column(Float)
    dollar_convexity : Mapped[Optional[float]] = mapped_column(Float)
    duration_to_convexity: Mapped[Optional[float]] = mapped_column(Float)

    operacion: Mapped[OperacionesCevaldom] = relationship(back_populates='vector_precio')

class MaestroView(Base):
    __tablename__ = 'MAESTRO_TITULO_CALC'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    isin : Mapped[str] = mapped_column(String(100), unique=True)
    emision : Mapped[Optional[time]]  = mapped_column(Date)
    vencimiento : Mapped[Optional[time]] = mapped_column(Date)
    cupon : Mapped[Optional[float]] = mapped_column(Float)
    periodicidad_pago: Mapped[Optional[str]]= mapped_column(String(10))
    moneda : Mapped[Optional[str]] = mapped_column(String(10))
    amortizable : Mapped[Optional[int]] = mapped_column(Integer)
    base_pago : Mapped[Optional[str]] = mapped_column(String(10))

# from sqlalchemy import create_engine

# def conectar_db():
#     server = 'quantech-general-server.database.windows.net'
#     database = 'DEVELOPMENT'
#     username = 'development'
#     password = 'Desarrollo2024'
#     driver = 'ODBC Driver 17 for SQL Server'
    
#     connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
#     engine = create_engine(connection_string, pool_pre_ping=True, pool_recycle=3600)
#     return engine

# Base.metadata.create_all(conectar_db())

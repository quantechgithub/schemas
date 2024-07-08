from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Date, ForeignKey, MetaData
from typing import Optional
from datetime import datetime

metadata_obj = MetaData(schema='MARKET')
class Base(DeclarativeBase):
    metadata = metadata_obj

class Amortiza(Base):
    __tablename__ = 'AMORTIZA'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    amortiza: Mapped[str] = mapped_column('AMORTIZA', String(20))

    def __repr__(self) -> str:
        return f"User(ID={self.id!r}, AMORTIZA={self.amortiza!r},"


class Sector(Base):
    __tablename__ = 'SECTOR'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    sector: Mapped[Optional[str]] = mapped_column('SECTOR', String(100))

    def __repr__(self) -> str:
        return f"Sector(ID={self.id!r}, SECTOR={self.sector!r})"

class Emisor(Base):
    __tablename__ = 'EMISORES'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    siglas: Mapped[Optional[str]] = mapped_column('SIGLAS', String(100))
    nombre: Mapped[str] = mapped_column('NOMBRE', String(200))
    sector_id: Mapped[Optional[int]] = mapped_column('SECTOR_ID', Integer, ForeignKey('MARKET.SECTOR.ID'))


    def __repr__(self) -> str:
        return f"Emisores(ID={self.id!r}, SIGLAS={self.siglas!r}, NOMBRE={self.nombre!r}, SECTOR={self.sector_id!r})"
    

class SerieEmision(Base):
    __tablename__ = 'SERIES_EMISION'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    siglas: Mapped[Optional[str]] = mapped_column('SIGLAS', String(100))
    nombre: Mapped[str] = mapped_column('NOMBRE', String(260))
    nombre_bvrd: Mapped[Optional[str]] = mapped_column('NOMBRE_BVRD', String(260))
    emisor_id: Mapped[int] = mapped_column('EMISOR_ID',ForeignKey('MARKET.EMISORES.ID'))

    def __repr__(self) -> str:
        return f"User(ID={self.id!r}, SIGLAS={self.siglas!r}, NOMBRE={self.nombre!r},NOMBRE_BVRD={self.nombre_bvrd!r},EMISOR_ID ={self.emisor_id!r})"


class Moneda(Base):
    __tablename__ = 'MONEDA'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    moneda: Mapped[str] = mapped_column('MONEDA', String(30))


class TipoInstrumento(Base):
    __tablename__ = 'TIPO_INSTRUMENTO'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    tipo: Mapped[str] = mapped_column('TIPO', String(100))


class BasePago(Base):
    __tablename__ = 'BASE_PAGO'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    base_pago: Mapped[str] = mapped_column('BASE_PAGO', String(100))
    base_pago_bvrd: Mapped[Optional[str]] = mapped_column('BASE_PAGO_BVRD', String(100))


class Perioricidad(Base):
    __tablename__ = 'PERIODICIDAD_PAGO'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    perioricidad: Mapped[str] = mapped_column('PERIORICIDAD_PAGO', String(50))
    perioricidad_bvrd: Mapped[Optional[str]] = mapped_column('PERIORICIDAD_BVRD', String(50))


class EmisorMoneda(Base):
    __tablename__ = 'EMISOR_MONEDA'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    emisor_moneda: Mapped[str] = mapped_column('EMISOR_MONEDA', String(100))

    # curves : Mapped[List['Curve']] = relationship(back_populates='emisor_moneda')
    # sondeos_locales : Mapped[List['SondeoLocal']] = relationship(back_populates='emisor_moneda')
    # titulos : Mapped[List['Maestro']] = relationship(back_populates='emisor_moneda')


class MetodoCalculo(Base):
    __tablename__ = 'METODO_CALCULO'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    metodo_calculo: Mapped[str] = mapped_column('METODO_CALCULO', String(100))

class Maestro(Base):
    __tablename__ = 'MAESTRO_TITULOS'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin: Mapped[str] = mapped_column('ISIN', String(100), unique=True)
    fecha_emision: Mapped[Optional[datetime]] = mapped_column('EMISION', Date)
    fecha_vencimiento: Mapped[Optional[datetime]] = mapped_column('VENCIMIENTO', Date)
    cupon: Mapped[Optional[float]] = mapped_column('CUPON', Float)
    amortiza_id: Mapped[Optional[int]] = mapped_column('AMORTIZA', Integer, ForeignKey('MARKET.AMORTIZA.ID'))
    serie_id: Mapped[Optional[int]] = mapped_column('SERIES_ID', Integer, ForeignKey('MARKET.SERIES_EMISION.ID'))
    moneda_id: Mapped[Optional[int]] = mapped_column('MONEDA_ID', Integer, ForeignKey('MARKET.MONEDA.ID'))
    tipo_id: Mapped[Optional[int]] = mapped_column('TIPO_ID', Integer, ForeignKey('MARKET.TIPO_INSTRUMENTO.ID'))
    base_id: Mapped[Optional[int]] = mapped_column('BASE_ID', Integer, ForeignKey('MARKET.BASE_PAGO.ID'))
    periodicidad_id: Mapped[Optional[int]] = mapped_column('PERIODICIDAD_ID', Integer, ForeignKey('MARKET.PERIODICIDAD_PAGO.ID'))
    monto_emitido: Mapped[Optional[float]] = mapped_column('MONTO_EMITIDO', Float)
    nemotecnico: Mapped[Optional[str]] = mapped_column('NEMOTECNICO', String(100))
    option_call: Mapped[Optional[int]] = mapped_column('OPTION_CALL', Integer)
    call_date: Mapped[Optional[datetime]] = mapped_column('CALL_DATE', Date)
    emisor_moneda_id: Mapped[Optional[int]] = mapped_column('EMISOR_MONEDA_ID', Integer, ForeignKey('MARKET.EMISOR_MONEDA.ID'))
    metodo_calculo_id: Mapped[Optional[int]] = mapped_column('METODO_CALCULO_ID', Integer, ForeignKey('MARKET.METODO_CALCULO.ID'))

    # sondeos_eurobonos : Mapped[List['SondeoEurobono']] = relationship(back_populates='titulo')
    # vector_precio : Mapped[List['VectorPrecio']] = relationship(back_populates='titulo')
    # emisor_moneda : Mapped['EmisorMoneda'] = relationship(back_populates='titulos')
    # tipo_instrumento : Mapped['TipoInstrumento'] = relationship(back_populates='titulos')  

class SubataCredito(Base):
    __tablename__ = 'SUBASTAS_CREDITO_PUBLICO'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID',Integer,ForeignKey('MARKET.MAESTRO_TITULOS.ID'))
    fecha_subasta: Mapped[Optional[datetime]] = mapped_column('FECHA_SUBASTA',Date)
    fecha_liquidacion: Mapped[Optional[datetime]] = mapped_column('FECHA_LIQUIDACION',Date)
    monto_ofertado: Mapped[Optional[float]] = mapped_column('MONTO_OFERTADO',Float)
    valor_nominal_recibido: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_RECIBIDO',Float)
    precio_promedio_ponderado: Mapped[Optional[float]] = mapped_column('PRECIO_PROMEDIO_PONDERADO',Float)
    tasa_promedio_ponderada: Mapped[Optional[float]] = mapped_column('TASA_PROMEDIO_PONDERADA',Float)
    valor_nominal_adjudicada: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_ADJUDICADA',Float)
    precio_adjudicacion: Mapped[Optional[float]] = mapped_column('PRECIO_DE_ADJUDICACION',Float)
    tasa_de_adjudicacion: Mapped[Optional[float]] = mapped_column('TASA_DE_ADJUDICACION',Float)
    valor_nominal_rechazado: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_RECHAZADO',Float)
    precio_promedio_ponderado_rechazado: Mapped[Optional[float]] = mapped_column('PRECIO_PROMEDIO_PONDERADO_RECHAZADO',Float)
    tasa_promedio_ponderado_rechazado: Mapped[Optional[float]] = mapped_column('TASA_PROMEDIO_PONDERADO_RECHAZADO')

class SubastaBCRD(Base):
    __tablename__ = 'SUBASTAS_BCRD'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID',Integer,ForeignKey('MARKET.MAESTRO_TITULOS.ID'))
    fecha_subasta: Mapped[Optional[datetime]] = mapped_column('FECHA_SUBASTA',Date)
    valor_nominal_recibido: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_RECIBIDO',Float)
    precio_de_oferta: Mapped[Optional[float]] = mapped_column('PRECIO_DE_LA_OFERTA',Float)
    valor_nominal_adjudicada: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_ADJUDICADA',Float)
    precio_de_corte: Mapped[Optional[Float]] = mapped_column('PRECIO_DE_CORTE',Float)
    precio_promedio_ponderado: Mapped[Optional[float]] = mapped_column('PRECIO_PROMEDIO_PONDERADO',Float)
    precio_rechazado:Mapped[Optional[float]] = mapped_column('PRECIO_RECHAZADO',Float)
    yield_promedio_ponderada_referencias_bcrd:Mapped[Optional[float]] = mapped_column('YIELD_PROMEDIO_PONDERADAA_REFERENCIAS_BCRD')
    yield_oferta: Mapped[Optional[float]] = mapped_column('YIELD_OFERTA',Float)
    yield_corte: Mapped[Optional[float]] = mapped_column('YIELD_CORTE',Float)
    yield_promedio_ponderada: Mapped[Optional[Float]] = mapped_column('YIELD_PROMEDIO_PONDERADA',Float)
    yield_rechazada :Mapped[Optional[Float]]  = mapped_column('YIELD_RECHAZADA',Float)

class OperacionMM(Base):
    __tablename__ = 'OPERACIONES_MARKETMAKERS'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID',Integer,ForeignKey('MARKET.MAESTRO_TITULOS.ID'))
    fecha_valor: Mapped[Optional[datetime]] = mapped_column('FECHA_VALOR',Date)
    cantidad_titulos: Mapped[Optional[int]] = mapped_column('CANTIDAD_TITULOS',Integer)
    valor_transado: Mapped[Optional[float]] = mapped_column('VALOR_TRANSDO',Float)
    dias_interes: Mapped[Optional[int]] = mapped_column('DIAS_INTERES',Integer)
    monto_interes: Mapped[Optional[float]] = mapped_column('MONTO_INTERES',Float)
    monto_limpio: Mapped[Optional[float]] = mapped_column('MONTO_LIMPIO',Float)
    precio_limpio: Mapped[Optional[float]] = mapped_column('PRECIO_LIMPIO',Float)
    rendimiento_vencimiento: Mapped[Optional[float]] = mapped_column('RENDIMIENTO_VENCIMIENTO')






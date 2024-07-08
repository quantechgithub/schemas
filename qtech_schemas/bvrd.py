from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer, String, Float, Date, ForeignKey,MetaData,Time,DateTime
from typing import Optional
from datetime import datetime
from qtech_schemas.market import Maestro

metadata_obj = MetaData(schema='BVRD')
class Base(DeclarativeBase):
    metadata = metadata_obj

class Codigo_Rueda(Base):
    __tablename__ = 'CODIGO_RUEDA'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    codigo_rueda: Mapped[str] = mapped_column('CODIGO_RUEDA', String(100))

class Compra_venta(Base):
    __tablename__ = 'COMPRA_VENTA'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    compra_venta: Mapped[str] = mapped_column('COMPRA_VENTA', String(100))

class Descripcion_instrumento(Base):
    __tablename__ = 'DESCRIPCION_INSTRUMENTO'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    descripcion_instrumento: Mapped[str] = mapped_column('DESCRIPCION_INSTRUMENTO', String(100))

class Estatus_operacion(Base):
    __tablename__ = 'ESTATUS_OPERACION'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    estatus_operacion: Mapped[str] = mapped_column('ESTATUS_OPERACION', String(100))

class Estatus_orden(Base):
    __tablename__ = 'ESTATUS_ORDEN'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    estatus_orden: Mapped[str] = mapped_column('ESTATUS_ORDEN', String(100))

class Rueda(Base):
    __tablename__ = 'RUEDA'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    rueda: Mapped[str] = mapped_column('RUEDA', String(100))

class Nombre_mercado(Base):
    __tablename__ = 'NOMBRE_MERCADO'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    nombre_mercado: Mapped[str] = mapped_column('NOMBRE_MERCADO', String(100))


class Mejor_ejecucion(Base):
    __tablename__ = 'MEJOR_EJECUCION'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID', Integer, ForeignKey('MARKET.MAESTRO_TITULOS.ID'))
    dias_sin_operar: Mapped[Optional[int]] = mapped_column('DIAS_SIN_OPERAR', Integer)
    fecha_hora_operacion: Mapped[Optional[datetime]] = mapped_column('FECHA_HORA_OPERACION', DateTime)
    fecha_operacion: Mapped[Optional[datetime]] = mapped_column('FECHA_OPERACION', Date)
    hora_operacion: Mapped[Optional[datetime]] = mapped_column('HORA_OPERACION', Time)
    monto_nominal: Mapped[Optional[int]] = mapped_column('MONTO_NOMINAL', Integer)
    monto_transado: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO', Float)
    monto_transado_equivalente_dolares: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO_EQUIVALENTE_DOLARES', Float)
    monto_transado_equivalente_pesos: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO_EQUIVALENTE_PESOS', Float)
    nombre_mercado: Mapped[Optional[int]] = mapped_column('NOMBRE_MERCADO_ID', Integer, ForeignKey('BVRD.NOMBRE_MERCADO.ID'))
    precio_limpio: Mapped[Optional[float]] = mapped_column('PRECIO_LIMPIO', Float)
    rendimiento: Mapped[Optional[float]] = mapped_column('RENDIMIENTO', Float)
    num_mercado: Mapped[Optional[int]] = mapped_column('NUM_MERCADO', Integer)

class Operaciones_bvrd(Base):
    __tablename__ = 'OPERACIONES_BVRD'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID', Integer, ForeignKey('MARKET.MAESTRO_TITULOS.ID'))
    valor_nominal: Mapped[Optional[float]] = mapped_column('VALOR_MONIMAL', Float)
    valor_transado: Mapped[Optional[float]] = mapped_column('VALOR_TRANSADO', Float)
    precio_porcentaje: Mapped[Optional[float]] = mapped_column('VALOR_PORCENTAJE', Float)
    ytm: Mapped[Optional[float]] = mapped_column('YTM', Float)
    dias_al_vencimiento: Mapped[Optional[int]] = mapped_column('DIAS_AL_VENCIMIENTO', Integer)
    fecha_operacion: Mapped[Optional[datetime]] = mapped_column('FECHA_OPERACION', Date)
    fechaa_liquidacion: Mapped[Optional[datetime]] = mapped_column('FECHA_LIQUIDACION', Date)

class Operaciones_totales(Base):
    __tablename__ = 'OPERACIONES_TOTALES'

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID', Integer, ForeignKey('MARKET.MAESTRO_TITULOS.ID'))
    descripcion_instrumento: Mapped[Optional[int]] = mapped_column('DESCRIPCION_INSTRUMENTO', Integer, ForeignKey('BVRD.DESCRIPCION_INSTRUMENTO.ID'))
    valor_nominal_unitario: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_UNITARIO', Float)

    emisor: Mapped[Optional[int]] = mapped_column('EMISOR', Integer, ForeignKey('MARKET.EMISORES.ID'))
    tasa_cupon: Mapped[Optional[float]] = mapped_column('TASA_CUPON', Float)
    fecha_liquidacion: Mapped[Optional[datetime]] = mapped_column('FECHA_LIQUIDACION', Date)
    cantidad_titulos: Mapped[Optional[float]] = mapped_column('CANTIDAD_TITULOS', Float)
    fecha_operacion: Mapped[Optional[datetime]] = mapped_column('FECHA_OPERACION', Date)
    hora_operacion: Mapped[Optional[datetime]] = mapped_column('HORA_OPERACION', Time)
    mercado: Mapped[Optional[int]] = mapped_column('MERCADO', Integer)
    nombre_mercado: Mapped[Optional[int]] = mapped_column('NOMBRE_MERCADO', Integer, ForeignKey('BVRD.NOMBRE_MERCADO.ID'))
    precio_limpio: Mapped[Optional[float]] = mapped_column('PRECIO_LIMPIO', Float)
    monto_nominal: Mapped[Optional[float]] = mapped_column('MONTO_NOMINAL', Float)
    monto_transado: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO', Float)
    plazo_liquidacion: Mapped[Optional[int]] = mapped_column('PLAZO_LIQUIDACION', Integer)
    estatus_operacion: Mapped[Optional[int]] = mapped_column('ESTATUS_OPERACION', Integer, ForeignKey('BVRD.ESTATUS_OPERACION.ID'))
    tasa_venta_dolar: Mapped[Optional[float]] = mapped_column('TASA_VENTA', Float)
    rendimiento: Mapped[Optional[float]] = mapped_column('RENDIMIENTO', Float)
    monto_transado_equivalente_pesos: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO_EQUIVALENTE_PESOS', Float)
    monto_transado_equivalente_dolares: Mapped[Optional[float]] = mapped_column('MONTO_TRNASADO_EQUIVALENTE_DOLARES', Float)
    rueda: Mapped[Optional[int]] = mapped_column('RUEDA', Integer, ForeignKey('BVRD.RUEDA.ID'))
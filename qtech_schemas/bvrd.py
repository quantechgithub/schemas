from sqlalchemy.orm import Mapped,mapped_column, relationship
from sqlalchemy import Integer, String, Float, Date, ForeignKey,Time,DateTime
from typing import Optional, List
from qtech_schemas.market import Maestro
from qtech_schemas.dbo import Base
from pandas import Timestamp as time

ARGS= {'schema': 'BVRD','extend_existing': True}
class CodigoRueda(Base):
    __tablename__ = 'CODIGO_RUEDA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    codigo_rueda: Mapped[str] = mapped_column('CODIGO_RUEDA', String(100))

class CompraVenta(Base):
    __tablename__ = 'COMPRA_VENTA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    compra_venta: Mapped[str] = mapped_column('COMPRA_VENTA', String(100))

class DescripcionInstrumento(Base):
    __tablename__ = 'DESCRIPCION_INSTRUMENTO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    descripcion_instrumento: Mapped[str] = mapped_column('DESCRIPCION_INSTRUMENTO', String(100))

class EstatusOperacion(Base):
    __tablename__ = 'ESTATUS_OPERACION'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    estatus_operacion: Mapped[str] = mapped_column('ESTATUS_OPERACION', String(100))

class EstatusOrden(Base):
    __tablename__ = 'ESTATUS_ORDEN'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    estatus_orden: Mapped[str] = mapped_column('ESTATUS_ORDEN', String(100))

class Rueda(Base):
    __tablename__ = 'RUEDA'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    rueda: Mapped[str] = mapped_column('RUEDA', String(100))

class NombreMercado(Base):
    __tablename__ = 'NOMBRE_MERCADO'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    nombre_mercado: Mapped[str] = mapped_column('NOMBRE_MERCADO', String(100))

    operaciones : Mapped[List['OperacionesTotales']] = relationship(back_populates='mercado')

class MejorEjecucion(Base):
    __tablename__ = 'MEJOR_EJECUCION'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID', Integer, ForeignKey(Maestro.id))
    dias_sin_operar: Mapped[Optional[int]] = mapped_column('DIAS_SIN_OPERAR', Integer)
    fecha_hora_operacion: Mapped[Optional[time]] = mapped_column('FECHA_HORA_OPERACION', DateTime)
    fecha_operacion: Mapped[Optional[time]] = mapped_column('FECHA_OPERACION', Date)
    hora_operacion: Mapped[Optional[time]] = mapped_column('HORA_OPERACION', Time)
    monto_nominal: Mapped[Optional[float]] = mapped_column('MONTO_NOMINAL', Float)
    monto_transado: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO', Float)
    monto_transado_equivalente_dolares: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO_EQUIVALENTE_DOLARES', Float)
    monto_transado_equivalente_pesos: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO_EQUIVALENTE_PESOS', Float)
    nombre_mercado: Mapped[Optional[int]] = mapped_column('NOMBRE_MERCADO_ID', Integer, ForeignKey(NombreMercado.id))
    precio_limpio: Mapped[Optional[float]] = mapped_column('PRECIO_LIMPIO', Float)
    rendimiento: Mapped[Optional[float]] = mapped_column('RENDIMIENTO', Float)
    num_mercado: Mapped[Optional[int]] = mapped_column('NUM_MERCADO', Integer)

class OperacionesBVRD(Base):
    __tablename__ = 'OPERACIONES_BVRD'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID', Integer, ForeignKey(Maestro.id))
    valor_nominal: Mapped[Optional[float]] = mapped_column('VALOR_MONIMAL', Float)
    valor_transado: Mapped[Optional[float]] = mapped_column('VALOR_TRANSADO', Float)
    precio_porcentaje: Mapped[Optional[float]] = mapped_column('VALOR_PORCENTAJE', Float)
    ytm: Mapped[Optional[float]] = mapped_column('YTM', Float)
    dias_al_vencimiento: Mapped[Optional[int]] = mapped_column('DIAS_AL_VENCIMIENTO', Integer)
    fecha_operacion: Mapped[Optional[time]] = mapped_column('FECHA_OPERACION', Date)
    fecha_liquidacion: Mapped[Optional[time]] = mapped_column('FECHA_LIQUIDACION', Date)

class OperacionesTotales(Base):
    __tablename__ = 'OPERACIONES_TOTALES'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID', Integer, ForeignKey(Maestro.id))
    descripcion_instrumento: Mapped[Optional[int]] = mapped_column('DESCRIPCION_INSTRUMENTO', Integer, ForeignKey(DescripcionInstrumento.id))
    valor_nominal_unitario: Mapped[Optional[float]] = mapped_column('VALOR_NOMINAL_UNITARIO', Float)
    tasa_cupon: Mapped[Optional[float]] = mapped_column('TASA_CUPON', Float)
    fecha_liquidacion: Mapped[Optional[time]] = mapped_column('FECHA_LIQUIDACION', Date)
    cantidad_titulos: Mapped[Optional[float]] = mapped_column('CANTIDAD_TITULOS', Float)
    fecha_operacion: Mapped[Optional[time]] = mapped_column('FECHA_OPERACION', Date)
    hora_operacion: Mapped[Optional[time]] = mapped_column('HORA_OPERACION', Time)
    tipo_mercado_id: Mapped[Optional[int]] = mapped_column('MERCADO', Integer)
    mercado_id: Mapped[Optional[int]] = mapped_column('NOMBRE_MERCADO', Integer, ForeignKey(NombreMercado.id))
    precio_limpio: Mapped[Optional[float]] = mapped_column('PRECIO_LIMPIO', Float)
    monto_nominal: Mapped[Optional[float]] = mapped_column('MONTO_NOMINAL', Float)
    monto_transado: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO', Float)
    plazo_liquidacion: Mapped[Optional[int]] = mapped_column('PLAZO_LIQUIDACION', Integer)
    estatus_operacion: Mapped[Optional[int]] = mapped_column('ESTATUS_OPERACION', Integer, ForeignKey(EstatusOperacion.id))
    tasa_venta_dolar: Mapped[Optional[float]] = mapped_column('TASA_VENTA', Float)
    rendimiento: Mapped[Optional[float]] = mapped_column('RENDIMIENTO', Float)
    monto_transado_equivalente_pesos: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO_EQUIVALENTE_PESOS', Float)
    monto_transado_equivalente_dolares: Mapped[Optional[float]] = mapped_column('MONTO_TRANSADO_EQUIVALENTE_DOLARES', Float)
    rueda: Mapped[Optional[int]] = mapped_column('RUEDA', Integer, ForeignKey(CodigoRueda.id))

    mercado: Mapped['NombreMercado'] = relationship(back_populates='operaciones')

class PosturasTotales(Base):
    __tablename__= 'POSTURAS_TOTALES'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID', Integer, ForeignKey(Maestro.id))
    nominal_unitario :Mapped[Optional[float]] = mapped_column('NOMINAL_UNITARIO',Float)
    tasa_cupon : Mapped[Optional[Float]] = mapped_column('TASA_CUPON',Float)
    fecha_postura : Mapped[Optional[time]] = mapped_column('FECHA_POSTURA',Date)
    hora_postura: Mapped[Optional[time]] = mapped_column('HORA_POSTURA',Time)
    monto_nominal : Mapped[Optional[Float]] = mapped_column('MONTO_NOMINAL',Float)
    precio_limpio : Mapped[Optional[Float]] = mapped_column('PRECIO_LIMPIO',Float)
    codigo_rueda : Mapped[Optional[int]] = mapped_column('CODIGO_RUEDA',Integer,ForeignKey(CodigoRueda.id))
    rendimiento : Mapped[Optional[Float]] = mapped_column('RENDIMIENTO',Float)
    compra_venta : Mapped[Optional[int]] = mapped_column('COMPRA_VENTA',Integer,ForeignKey(CompraVenta.id))
    plazo_liquidacion : Mapped[Optional[float]] = mapped_column('PLAZO_LIQUIDACION',Float)
    fecha_liquidacion: Mapped[Optional[time]] = mapped_column('FECHA_LIQUIDACION',Date)
    numero_operacion_id : Mapped[Optional[float]] = mapped_column('NUMERO_OPERACION_ID',Float)
    estatus_orden : Mapped[Optional[int]] = mapped_column('ESTATUS_ORDEN',Integer,ForeignKey(EstatusOrden.id))
    cantidad_titulos : Mapped[Optional[float]] = mapped_column('CANTIDAD_TITULOS',Float)

class Flujos(Base):
    __tablename__= 'FLUJOS'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column('ID', Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column('ISIN_ID',Integer,ForeignKey(Maestro.id))
    fecha_previo: Mapped[time] = mapped_column("FECHA_PREVIO", Date)
    fecha_flujo: Mapped[time] = mapped_column("FECHA_FLUJO",Date)
    fecha_previo_str: Mapped[time] = mapped_column('FECHA_PREVIO_STR',Date)
    fecha_flujo_str: Mapped[time] = mapped_column("FECHA_FLUJO_STR",Date)
    dias_cupon: Mapped[int]= mapped_column("DIAS_CUPON",Integer)
    dias_al_flujo: Mapped[int] = mapped_column("DIAS_AL_FLUJO",Integer)
    cantidad_meses: Mapped[int] = mapped_column("CANTIDAD_MESES",Integer)
    tasa_amortizacion: Mapped[int] = mapped_column("TASA_AMORTIZACION",Integer)
    amortizacion_acumulada: Mapped[int] = mapped_column("AMORTIZACION_ACUMULADA",Integer)
    monto_amortizacion: Mapped[int] = mapped_column("MONTO_AMORTIZACION",Integer)
    base_dias: Mapped[int] = mapped_column("BASE_DIAS", Integer)
    
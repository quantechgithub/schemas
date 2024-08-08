from sqlalchemy.orm import Mapped,mapped_column, relationship
from sqlalchemy import Integer, String, Float, Date, ForeignKey, Table, Column
from typing import List, Optional
from qtech_schemas.market import Maestro, VectorMonto, Moneda, EmisorMoneda
from qtech_schemas._yield import TimeSeriesState, ValuationMethod
from qtech_schemas.dbo import Variables, Base
from pandas import Timestamp as time

ARGS= {'schema': 'DRIX'} #,'extend_existing': True

class Titulo(Maestro):
    pass

index_emisor_moneda_linkage = Table(
    'INDEX_EMISOR_MONEDA_LINKAGE',
    Base.metadata,
    Column('index_id', Integer, ForeignKey('DRIX.INDEX.id')),
    Column('emisor_moneda_id', Integer, ForeignKey('MARKET.EMISOR_MONEDA.id'))
)

class EmisorMonedaDrix(EmisorMoneda):
    risk_factors : Mapped[List['RiskFactor']] = relationship('RiskFactor', back_populates='emisor_moneda')
    indexes : Mapped[List['Index']] = relationship('Index', secondary = index_emisor_moneda_linkage, back_populates='emisor_monedas')
    
class VectorMontoDrix(VectorMonto):
    pass

class MonedaDrix(Moneda):
    indexes : Mapped[List['Index']] = relationship('Index', back_populates='reporting_currency')

index_risk_factor_linkage = Table(
    'INDEX_RISK_FACTOR_LINKAGE',
    Base.metadata,
    Column('index_id', Integer, ForeignKey('DRIX.INDEX.id')),
    Column('risk_factor_id', Integer, ForeignKey('DRIX.RISK_FACTOR.id'))
)

class TimeSeriesStateDrix(TimeSeriesState):
    pass

class ValuationMethodDrix(ValuationMethod):
    indexes : Mapped[List['Index']] = relationship('Index', back_populates='valuation_method')

class VariablesDrix(Variables):
    pass

class WeightingMethod(Base):
    __tablename__ = 'WEIGHTING_METHOD'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(100), unique=True)

    indexes : Mapped[List['Index']] = relationship('Index', back_populates='weighting_method')

class CalculationFrequency(Base):
    __tablename__ = 'CALCULATION_FREQUENCY'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(100), unique=True)

    indexes : Mapped[List['Index']] = relationship('Index', back_populates='calculation_frequency')

class RebalancingFrequency(Base):
    __tablename__ = 'REBALANCING_FREQUENCY'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(100), unique=True)

    indexes : Mapped[List['Index']] = relationship('Index', back_populates='rebalancing_frequency')

class IndexType(Base):
    __tablename__ = 'INDEX_TYPE'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(100), unique=True)

    indexes : Mapped[List['Index']] = relationship('Index', back_populates='index_type')

class RiskFactor(Base):
    __tablename__ = 'RISK_FACTOR'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(100), unique=True)
    maturity: Mapped[Optional[float]] = mapped_column(Float)
    emisor_moneda_id: Mapped[int] = mapped_column(Integer, ForeignKey(EmisorMonedaDrix.id))

    emisor_moneda : Mapped[EmisorMonedaDrix] = relationship(back_populates='risk_factors')
    indexes : Mapped[List['Index']] = relationship(secondary = index_risk_factor_linkage, back_populates='risk_factors')


class Index(Base):
    __tablename__ = 'INDEX'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(100), unique=True)
    weighting_method_id: Mapped[int] = mapped_column(Integer, ForeignKey(WeightingMethod.id))
    rebalancing_frequency_id: Mapped[int] = mapped_column(Integer, ForeignKey(RebalancingFrequency.id))
    calculation_frequency_id: Mapped[int] = mapped_column(Integer, ForeignKey(CalculationFrequency.id))
    reporting_currency_id: Mapped[int] = mapped_column(Integer, ForeignKey(MonedaDrix.id))
    launch_date: Mapped[time] = mapped_column(Date)
    index_type_id: Mapped[int] = mapped_column(Integer, ForeignKey(IndexType.id))
    valuation_method_id: Mapped[int] = mapped_column(Integer, ForeignKey(ValuationMethodDrix.id))

    weighting_method: Mapped[WeightingMethod] = relationship(back_populates ='indexes')
    rebalancing_frequency: Mapped[RebalancingFrequency] = relationship(back_populates ='indexes')
    calculation_frequency: Mapped[CalculationFrequency] = relationship(back_populates ='indexes')
    reporting_currency: Mapped[MonedaDrix] = relationship(back_populates ='indexes')
    index_type: Mapped[IndexType] = relationship(back_populates ='indexes')
    valuation_method: Mapped[ValuationMethodDrix] = relationship(back_populates ='indexes')
    risk_factors: Mapped[List[RiskFactor]] = relationship(secondary = index_risk_factor_linkage, back_populates='indexes')
    emisor_monedas: Mapped[List[EmisorMonedaDrix]] = relationship('EmisorMonedaDrix', secondary = index_risk_factor_linkage, back_populates='indexes')

class TypeValue(Base):
    __tablename__ = 'TYPE_VALUE'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(100), unique=True)

class IndexFact(Base):
    __tablename__ = 'INDEX_FACT'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    index_id: Mapped[int] = mapped_column(Integer, ForeignKey(Index.id))
    titulo_id: Mapped[int] = mapped_column(Integer, ForeignKey(Titulo.id))
    benchmark_id: Mapped[int] = mapped_column(Integer, ForeignKey(RiskFactor.id))
    type_value_id: Mapped[int] = mapped_column(Integer, ForeignKey(TypeValue.id))
    value: Mapped[float] = mapped_column(Float)



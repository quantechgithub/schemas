from sqlalchemy.orm import Mapped,mapped_column, relationship
from sqlalchemy import Integer, String, Float, Date, ForeignKey, Table, Column
from typing import List, Optional
from qtech_schemas.market import Maestro, EmisorMoneda
from qtech_schemas.dbo import Variables, Base
from pandas import Timestamp as time

ARGS= {'schema': 'FX','extend_existing': True}

class VariablesDboFx(Variables):
    pass

class FxQuote(Base):
    __tablename__ = 'QUOTE'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(15), unique=True)

    variable: Mapped[List['FxVariable']] = relationship(back_populates='quote')

class FxEntity(Base):
    __tablename__ = 'ENTITIES'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(15), unique=True)

    variable: Mapped[List['FxVariable']] = relationship(back_populates='entity')

class FxType(Base):
    __tablename__ = 'TYPE'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(15), unique=True)

    variable: Mapped[List['FxVariable']] = relationship(back_populates='type')

class FxScenario(Base):
    __tablename__ = 'SCENARIO'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(15), unique=True)
    upper_bound : Mapped[float] = mapped_column(Float)
    lower_bound : Mapped[float] = mapped_column(Float)

    probability_fact: Mapped[List['FxProbabilityFact']] = relationship(back_populates='scenario')

class FxSeriesState(Base):
    __tablename__ = 'SERIES_STATE'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(15), unique=True)

    variable_fact: Mapped[List['FxVariableFact']] = relationship(back_populates='state')
    analytics_fact: Mapped[List['FxAnalyticsFact']] = relationship(back_populates='state')

class FxTypeTransform(Base):
    __tablename__ = 'TYPE_TRANSFORM'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(15), unique=True)

    analytics: Mapped[List['FxAnalytics']] = relationship(back_populates='transform')

association_table = Table(
    'ANALYTICS_VARIABLE_LINKAGE', 
    Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('variable_id', Integer, ForeignKey('FX.VARIABLE.id')),
    Column('analytics_id', Integer, ForeignKey('FX.ANALYTICS.id')),
    Column('index', Integer),
    schema='FX',
    extend_existing=True  # Esto es importante para evitar el error
)

class FxVariable(Base):
    __tablename__ = 'VARIABLE'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(30), unique=True)
    datos_id : Mapped[int] = mapped_column(ForeignKey(VariablesDboFx.id))
    quote_id : Mapped[int] = mapped_column(ForeignKey(FxQuote.id))
    entity_id: Mapped[int] = mapped_column(ForeignKey(FxEntity.id))
    type_id: Mapped[int] = mapped_column(ForeignKey(FxType.id))

    quote: Mapped[FxQuote] = relationship(back_populates='variable')
    entity: Mapped[FxEntity] = relationship(back_populates='variable')
    type: Mapped[FxType] = relationship(back_populates='variable')

    datos: Mapped[List[VariablesDboFx]] = relationship(back_populates='variable')
    variable_facts : Mapped[List['FxVariableFact']] = relationship(back_populates='variable')
    probability_facts: Mapped[List['FxProbabilityFact']] = relationship(back_populates='variable')

    analytics : Mapped[List['FxAnalytics']] = relationship(secondary=association_table, back_populates='variables')

class FxVariableFact(Base):
    __tablename__ = 'VARIABLE_FACT'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    name : Mapped[str] = mapped_column(String(30), unique=True)
    state_id: Mapped[int] = mapped_column(ForeignKey(FxSeriesState.id))
    variable_id : Mapped[int] = mapped_column(ForeignKey(FxVariable.id))
    value: Mapped[float] = mapped_column(Float)

    variable: Mapped[FxVariable] = relationship(back_populates = 'variable_fact')
    state: Mapped[FxSeriesState] = relationship(back_populates='variable_fact')

class FxProbabilityFact(Base):
    __tablename__ = 'PROBABILITY_FACT'
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key= True, autoincrement= True)
    date: Mapped[time] = mapped_column(Date)
    scenario_id: Mapped[int] = mapped_column(ForeignKey(FxScenario.id))
    variable_id : Mapped[int] = mapped_column(ForeignKey(FxVariable.id))
    value: Mapped[float] = mapped_column(Float)

    variable: Mapped[FxVariable] = relationship(back_populates = 'variable_fact')
    scenario: Mapped[FxScenario] = relationship(back_populates='probability_fact')

class FxAnalytics(Base):
    __tablename__ = 'ANALYTICS'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(30), unique=True)
    transfor_id: Mapped[int] = mapped_column(ForeignKey(FxTypeTransform.id))

    variables : Mapped[List['FxVariable']] = relationship(secondary=association_table, back_populates='analytics')

class FxAnalyticsFact(Base):
    __tablename__ = 'ANALYTICS_FACT'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date : Mapped[time] = mapped_column(Date)
    analytics_id : Mapped[int] = mapped_column(ForeignKey(FxAnalytics.id))
    state_id: Mapped[int] = mapped_column(ForeignKey(FxSeriesState.id))
    value : Mapped[float] = mapped_column(Float)

    analytics: Mapped[FxAnalytics] = relationship(back_populates='analytics_facts')
    state: Mapped[FxSeriesState] = relationship(back_populates='analytics_fact')

class AnalyticsVariableLikage(Base):
    __tablename__ = 'ANALYTICS_VARIABLE_LINKAGE'
    __table_args__ = ARGS

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    variable_id: Mapped[int] = mapped_column(ForeignKey(FxVariable.id))
    analytics_id: Mapped[int] = mapped_column(ForeignKey(FxAnalytics.id))
    index = Column(Integer)


# from sqlalchemy import create_engine

# def conectar_db():
#     server = 'quantech-general-server.database.windows.net'
#     database = 'DEVELOPMENT'
#     username = 'development'
#     password = 'Desarrollo2024's
#     driver = 'ODBC Driver 17 for SQL Server'
    
#     connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
#     engine = create_engine(connection_string, pool_pre_ping=True, pool_recycle=3600)
#     return engine

# Base.metadata.create_all(conectar_db())

from sqlalchemy.orm import Mapped,mapped_column, relationship
from sqlalchemy import Integer, String, Float, Date, ForeignKey, Table, Column
from datetime import date as dt
from typing import List, Optional
from market import Maestro, EmisorMoneda
from dbo import Variables
from dbo import Base


SCHEMA = {'schema': 'YIELD'}
class Titulo(Maestro):
    sondeos_eurobonos : Mapped[List['SondeoEurobono']] = relationship(back_populates='titulo')
    vector_precio : Mapped[List['VectorPrecio']] = relationship(back_populates='titulo')

class VariablesMarket(Variables):
    sondeos_fred : Mapped[List['SondeosFredOption']] = relationship(back_populates='variable')

class EmisorMonedaMarket(EmisorMoneda):
    curves : Mapped[List['Curve']] = relationship(back_populates='emisor_moneda')
    sondeos_locales : Mapped[List['SondeoLocal']] = relationship(back_populates='emisor_moneda')

class CurveInput(Base):
    __tablename__ = 'CURVE_INPUT'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    inputs : Mapped[str] = mapped_column(String(20), unique=True)

    curves : Mapped[List['Curve']] = relationship(back_populates='input')

class CurveType(Base):
    __tablename__ = 'CURVE_TYPE'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type : Mapped[str] = mapped_column(String(15), unique=True)

    curves : Mapped[List['Curve']] = relationship(back_populates='type')

class CurveMethod(Base):
    __tablename__ = 'CURVE_METHOD'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    method : Mapped[str] = mapped_column(String(15), unique=True)

    curves : Mapped[List['Curve']] = relationship(back_populates='method')

class CurveMode(Base):
    __tablename__ = 'CURVE_MODE'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mode : Mapped[str] = mapped_column(String(15), unique=True)
    curves : Mapped[List['Curve']] = relationship(back_populates='mode')

class Quote(Base):
    __tablename__ = 'QUOTE'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    quote : Mapped[str] = mapped_column(String(15), unique=True)
    curves : Mapped[List['Curve']] = relationship(back_populates='quote')
    sondeos_locales : Mapped[List['SondeoLocal']] = relationship(back_populates='quote')
    sondeos_eurobonos : Mapped[List['SondeoEurobono']] = relationship(back_populates='quote')
    valuation_methods : Mapped[List['ValuationMethod']] = relationship(back_populates='quote')

class Curve(Base):
    __tablename__ = 'CURVE'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    qtech_id : Mapped[str] = mapped_column(String(25), unique=True)
    name : Mapped[str] = mapped_column(String(75), unique=True)
    input_id : Mapped[int] = mapped_column(ForeignKey(CurveInput.id))
    emisor_moneda_id : Mapped[int] = mapped_column(ForeignKey(EmisorMonedaMarket.id))
    mode_id : Mapped[int] = mapped_column(ForeignKey(CurveMode.id))
    quote_id : Mapped[int] = mapped_column(ForeignKey(Quote.id))
    method_id : Mapped[int] = mapped_column(ForeignKey(CurveMethod.id))
    type_id : Mapped[int] = mapped_column(ForeignKey(CurveType.id))
    fwd_time : Mapped[float] = mapped_column(Float)
    tax_rate : Mapped[float] = mapped_column(Float)
    
    input: Mapped['CurveInput'] = relationship(back_populates='curves')
    emisor_moneda: Mapped['EmisorMonedaMarket'] = relationship(back_populates='curves')
    method: Mapped['CurveMethod'] = relationship(back_populates='curves')
    mode: Mapped['CurveMode'] = relationship(back_populates='curves')
    quote: Mapped['Quote'] = relationship(back_populates='curves')
    valuation_method : Mapped['ValuationMethod'] = relationship(back_populates='curve')
    type : Mapped['CurveType'] = relationship(back_populates='curves')

    parametros : Mapped[List['Parametro']] = relationship(back_populates='curve')
    benchmarks : Mapped[List['CurveBenchmark']] = relationship(back_populates='curve')
    sondeos_fred : Mapped[List['SondeosFredOption']] = relationship(back_populates='curve')

class SondeoLocal(Base):
    __tablename__ = 'SONDEOS_LOCALES'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date : Mapped[dt] = mapped_column(Date)
    maturity : Mapped[int] = mapped_column(Integer)
    emisor_moneda_id : Mapped[int] = mapped_column(ForeignKey(EmisorMonedaMarket.id))
    quote_id : Mapped[int] = mapped_column(ForeignKey(Quote.id))
    ytm : Mapped[float] = mapped_column(Float)

    emisor_moneda : Mapped['EmisorMonedaMarket'] = relationship(back_populates='sondeos_locales')
    quote : Mapped['Quote'] = relationship(back_populates='sondeos_locales')

    def to_dict(self)-> dict:
        return {
            'id': self.id,
            'date': self.date,
            'maturity': self.maturity,
            'emisor_moneda': self.emisor_moneda.emisor_moneda,
            'quote': self.quote.quote,
            'ytm': self.ytm
        }

class SondeoEurobono(Base):
    __tablename__ = 'SONDEOS_EUROBONOS'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date : Mapped[dt] = mapped_column(Date)
    titulo_id : Mapped[int] = mapped_column(ForeignKey(Maestro.id))
    quote_id : Mapped[int] = mapped_column(ForeignKey(Quote.id))
    ytm :  Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    price :  Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    titulo : Mapped['Titulo'] = relationship(back_populates='sondeos_eurobonos')
    quote : Mapped['Quote'] = relationship(back_populates='sondeos_eurobonos')

    def to_dict(self)-> dict:
        return {
            'id': self.id,
            'date': self.date,
            'titulo': self.titulo.isin,
            'maturity': self.titulo.fecha_vencimiento,
            'quote': self.quote.quote,
            'ytm': self.ytm,
            'price': self.price
        }

class SondeosFredOption(Base):
    __tablename__ = 'SONDEOS_FRED'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    variable_id : Mapped[int] = mapped_column(ForeignKey(VariablesMarket.id))
    maturity : Mapped[int] = mapped_column(Integer)
    curve_id : Mapped[int] = mapped_column(ForeignKey(Curve.id))

    variable : Mapped['VariablesMarket'] = relationship(back_populates='sondeos_fred')
    curve : Mapped['Curve'] = relationship(back_populates='sondeos_fred')

class Parametro(Base):
    __tablename__ = 'PARAMETROS'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date : Mapped[dt] = mapped_column(Date)
    curve_id : Mapped[int] = mapped_column(ForeignKey(Curve.id))
    tau1 : Mapped[float] = mapped_column(Float)
    tau2 :  Mapped[Optional[float]] = mapped_column(Float)	
    b0 : Mapped[float] = mapped_column(Float)
    b1 :  Mapped[float]= mapped_column(Float)
    b2 :  Mapped[float] = mapped_column(Float)
    b3 :  Mapped[Optional[float]] = mapped_column(Float)

    curve : Mapped['Curve'] = relationship(back_populates='parametros')

    def to_dict(self)-> dict:
        return {
            'id': self.id,
            'date': self.date,
            'curve': self.curve.name,
            'tau1': self.tau1,
            'tau2': self.tau2,
            'b0': self.b0,
            'b1': self.b1,
            'b2': self.b2,
            'b3': self.b3
        }

    def __str__(self):
        return f"date={self.date}, curve={self.curve.name}, tau1={self.tau1}, tau2={self.tau2}, b0={self.b0}, b1={self.b1}, b2={self.b2}, b3={self.b3})"

class ValuationMethodOption(Base):
    __tablename__ = 'VALUATION_METHOD_OPTION'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    option : Mapped[str] = mapped_column(String(15), unique=True)

    valuation_methods : Mapped[List['ValuationMethod']] = relationship(back_populates='valuation_method_option')

class ValuationMethod(Base):
    __tablename__ = 'VALUATION_METHOD'
    __table_args__ = SCHEMA
 
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(30), unique=True)
    valuation_method_option_id : Mapped[int] = mapped_column(ForeignKey(ValuationMethodOption.id))
    curve_id : Mapped[Optional[int]] = mapped_column(ForeignKey(Curve.id))
    quote_id : Mapped[Optional[int]] = mapped_column(ForeignKey(Quote.id))
 
    valuation_method_option : Mapped['ValuationMethodOption'] = relationship(back_populates='valuation_methods')
    quote : Mapped['Quote'] = relationship(back_populates='valuation_methods')
    curve : Mapped['Curve'] = relationship(back_populates='valuation_method')
    vectores_precios : Mapped[List['VectorPrecio']] = relationship(back_populates='valuation_method')
 
    def to_dict(self)-> dict:
        return {
            'id': self.id,
            'name': self.name,
            'valuation_method_option': self.valuation_method_option.option,
            'curve': self.curve.name if self.curve else None,
            'quote': self.quote.quote if self.quote else None,
            'method': self.curve.method.method if self.curve else None,
            'market': self.curve.quote.quote if self.curve else self.quote.quote
        }

class VectorPrecio(Base):
    __tablename__ = 'VECTOR_PRECIO'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date : Mapped[dt] = mapped_column(Date)
    titulo_id : Mapped[int] = mapped_column(ForeignKey(Maestro.id))
    valuation_method_id : Mapped[int] = mapped_column(ForeignKey(ValuationMethod.id))
    ytm : Mapped[Optional[float]] = mapped_column(Float)
    clean_price : Mapped[Optional[float]] = mapped_column(Float)
    dirty_price : Mapped[Optional[float]] = mapped_column(Float)
    theta : Mapped[Optional[float]] = mapped_column(Float)
    time : Mapped[Optional[float]] = mapped_column(Float)
    current_yield : Mapped[Optional[float]] = mapped_column(Float)
    mcauly_duration : Mapped[Optional[float]] = mapped_column(Float)
    mduration : Mapped[Optional[float]] = mapped_column(Float)
    convexity : Mapped[Optional[float]] = mapped_column(Float)

    titulo : Mapped['Titulo'] = relationship(back_populates='vector_precio')
    valuation_method : Mapped['ValuationMethod'] = relationship(back_populates='vectores_precios')

    def to_dict(self)-> dict:
        return {
            'id': self.id,
            'date': self.date,
            'titulo': self.titulo.isin,
            'valuation_method': self.valuation_method.name,
            'valuation_method_option': self.valuation_method.valuation_method_option.option,
            'market': self.valuation_method.curve.quote.quote if self.valuation_method.curve else self.valuation_method.quote.quote,
            'method': self.valuation_method.curve.method.method if self.valuation_method.curve else None,
            'ytm': self.ytm,
            'clean_price': self.clean_price,
            'dirty_price': self.dirty_price
        }
    
    def __str__(self):
        return f"date={self.date}, titulo={self.titulo.isin}, valuation_method={self.valuation_method.name}, ytm={self.ytm}, clean_price={self.clean_price}, dirty_price={self.dirty_price})"

association_table = Table(
    'BENCHMARK_DERIVATIVES', 
    Base.metadata,
    Column('benchmark_id', Integer, ForeignKey('YIELD.CURVE_BENCHMARK.id')),
    Column('benchmark_derivative_id', Integer, ForeignKey('YIELD.BENCHMARK_DERIVATIVE.id')),
    schema='YIELD'
)

class CurveBenchmark(Base):
    __tablename__ = 'CURVE_BENCHMARK'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(30), unique=True)
    maturity : Mapped[float] = mapped_column(Float)
    curve_id : Mapped[int] = mapped_column(ForeignKey(Curve.id))

    curve : Mapped['Curve'] = relationship(back_populates='benchmarks')
    benchmark_facts : Mapped[List['BenchmarkFact']] = relationship(back_populates='curve_benchmark')
    derivatives : Mapped[List['BenchmarkDerivative']] = relationship(secondary=association_table, back_populates='benchmarks')

class BenchmarkFact(Base):
    __tablename__ = 'BENCHMARK_FACT'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date : Mapped[dt] = mapped_column(Date)
    curve_benchmark_id : Mapped[int] = mapped_column(ForeignKey(CurveBenchmark.id))
    value : Mapped[float] = mapped_column(Float)

    curve_benchmark : Mapped['CurveBenchmark'] = relationship(back_populates='benchmark_facts')

    def to_dict(self)-> dict:
        return {
            'id': self.id,
            'date': self.date,
            'curve_benchmark': self.curve_benchmark.name,
            'value': self.value
        }

    def __str__(self):
        return f"date={self.date}, curve_benchmark={self.curve_benchmark.name}, value={self.value})"  

class TypeDerivative(Base):
    __tablename__ = 'TIPO_DERIVADO'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type : Mapped[str] = mapped_column(String(30), unique=True)

    derivatives : Mapped[List['BenchmarkDerivative']] = relationship(back_populates='type_derivative')

class BenchmarkDerivative(Base):
    __tablename__ = 'BENCHMARK_DERIVATIVE'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(75), unique=True)
    type_derivative_id : Mapped[int] = mapped_column(ForeignKey(TypeDerivative.id))
    fwd_time : Mapped[float] = mapped_column(Float)
    init_benchmark_id : Mapped[int] = mapped_column(ForeignKey(CurveBenchmark.id))
    end_benchmark_id : Mapped[int] = mapped_column(ForeignKey(CurveBenchmark.id))
    
    type_derivative : Mapped['TypeDerivative'] = relationship(back_populates='derivatives')
    benchmarks : Mapped[List['CurveBenchmark']] = relationship(secondary=association_table, back_populates='derivatives')
    derivative_facts : Mapped[List['DerivativeFact']] = relationship(back_populates='benchmark_derivative')

class DerivativeFact(Base):
    __tablename__ = 'DERIVATIVE_FACT'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date : Mapped[dt] = mapped_column(Date)
    benchmark_derivative_id : Mapped[int] = mapped_column(ForeignKey(BenchmarkDerivative.id))
    value : Mapped[float] = mapped_column(Float)

    benchmark_derivative : Mapped['BenchmarkDerivative'] = relationship(back_populates='derivative_facts')

class TituloView(Base):
    __tablename__ = 'MAESTRO_TITULO'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    isin : Mapped[str] = mapped_column(String(100), unique=True)
    emision : Mapped[Optional[dt]]  = mapped_column(Date)
    vencimiento : Mapped[Optional[dt]] = mapped_column(Date)
    cupon : Mapped[Optional[float]] = mapped_column(Float)
    periodicidad_pago: Mapped[Optional[str]]= mapped_column(String(10))
    moneda : Mapped[Optional[str]] = mapped_column(String(10))
    amortizable : Mapped[Optional[int]] = mapped_column(Integer)
    base_pago : Mapped[Optional[str]] = mapped_column(String(10))

class DatoView(Base):
    __tablename__ = 'DATOS_VIEW'
    __table_args__ = SCHEMA

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date : Mapped[dt] = mapped_column( Date)
    index : Mapped[str] = mapped_column(String(100))
    value : Mapped[float] = mapped_column( Float)

    def to_dict(self)-> dict:
        return {
            'id': self.id,
            'date': self.date,
            'index': self.index,
            'value': self.value
        }
    
from sqlalchemy import create_engine

def conectar_db():
    server = 'quantech-general-server.database.windows.net'
    database = 'DEVELOPMENT'
    username = 'development'
    password = 'Desarrollo2024'
    driver = 'ODBC Driver 17 for SQL Server'
    
    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
    engine = create_engine(connection_string, pool_pre_ping=True)
    return engine

Base.metadata.create_all(conectar_db())
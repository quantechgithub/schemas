from pandas import Timestamp as time
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from qtech_schemas.dbo import Base, Variables
from qtech_schemas.market import EmisorMoneda, Maestro

ARGS = {"schema": "YIELD", "extend_existing": True}


class Titulo(Maestro):
    sondeos_eurobonos: Mapped[list["SondeoEurobono"]] = relationship(
        back_populates="titulo"
    )
    vector_precio: Mapped[list["VectorPrecio"]] = relationship(back_populates="titulo")


class VariablesMarket(Variables):
    sondeos_fred: Mapped[list["SondeosFredOption"]] = relationship(
        back_populates="variable"
    )
    curve_inflation_link: Mapped[list["CurveInflationLinkage"]] = relationship(
        back_populates="variable"
    )


class EmisorMonedaMarket(EmisorMoneda):
    curves: Mapped[list["Curve"]] = relationship(back_populates="emisor_moneda")
    sondeos_locales: Mapped[list["SondeoLocal"]] = relationship(
        back_populates="emisor_moneda"
    )


class CurveInput(Base):
    __tablename__ = "CURVE_INPUT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    inputs: Mapped[str] = mapped_column(String(20), unique=True)

    curves: Mapped[list["Curve"]] = relationship(back_populates="input")


class CurveType(Base):
    __tablename__ = "CURVE_TYPE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String(15), unique=True)

    curves: Mapped[list["Curve"]] = relationship(back_populates="type")


class CurveMethod(Base):
    __tablename__ = "CURVE_METHOD"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    method: Mapped[str] = mapped_column(String(15), unique=True)

    curves: Mapped[list["Curve"]] = relationship(back_populates="method")


class CurveMode(Base):
    __tablename__ = "CURVE_MODE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mode: Mapped[str] = mapped_column(String(15), unique=True)
    curves: Mapped[list["Curve"]] = relationship(back_populates="mode")


class Quote(Base):
    __tablename__ = "QUOTE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    quote: Mapped[str] = mapped_column(String(15), unique=True)
    curves: Mapped[list["Curve"]] = relationship(back_populates="quote")
    sondeos_locales: Mapped[list["SondeoLocal"]] = relationship(back_populates="quote")
    sondeos_eurobonos: Mapped[list["SondeoEurobono"]] = relationship(
        back_populates="quote"
    )
    valuation_methods: Mapped[list["ValuationMethod"]] = relationship(
        back_populates="quote"
    )


association_table2 = Table(
    "CURVE_DERIVATIVE_LINKAGE",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("curve_id", Integer, ForeignKey("YIELD.CURVE.id")),
    Column("benchmark_derivative_id", Integer, ForeignKey("YIELD.DERIVATIVE.id")),
    Column("index", Integer),
    schema="YIELD",
    extend_existing=True,  # Esto es importante para evitar el error
)


class Curve(Base):
    __tablename__ = "CURVE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    qtech_id: Mapped[str] = mapped_column(String(25), unique=True)
    name: Mapped[str] = mapped_column(String(75), unique=True)
    input_id: Mapped[int] = mapped_column(ForeignKey(CurveInput.id))
    emisor_moneda_id: Mapped[int] = mapped_column(ForeignKey(EmisorMonedaMarket.id))
    mode_id: Mapped[int] = mapped_column(ForeignKey(CurveMode.id))
    quote_id: Mapped[int] = mapped_column(ForeignKey(Quote.id))
    method_id: Mapped[int] = mapped_column(ForeignKey(CurveMethod.id))
    type_id: Mapped[int] = mapped_column(ForeignKey(CurveType.id))
    fwd_time: Mapped[float] = mapped_column(Float)
    tax_rate: Mapped[float] = mapped_column(Float)
    filter: Mapped[bool] = mapped_column(Boolean)
    constrained: Mapped[bool] = mapped_column(Boolean)

    input: Mapped["CurveInput"] = relationship(back_populates="curves")
    emisor_moneda: Mapped["EmisorMonedaMarket"] = relationship(back_populates="curves")
    method: Mapped["CurveMethod"] = relationship(back_populates="curves")
    mode: Mapped["CurveMode"] = relationship(back_populates="curves")
    quote: Mapped["Quote"] = relationship(back_populates="curves")
    valuation_method: Mapped["ValuationMethod"] = relationship(back_populates="curve")
    type: Mapped["CurveType"] = relationship(back_populates="curves")

    parametros: Mapped[list["Parametro"]] = relationship(back_populates="curve")
    benchmarks: Mapped[list["CurveBenchmark"]] = relationship(back_populates="curve")
    sondeos_fred: Mapped[list["SondeosFredOption"]] = relationship(
        back_populates="curve"
    )
    curve_inflation_link: Mapped[list["CurveInflationLinkage"]] = relationship(
        back_populates="curve"
    )
    derivatives: Mapped[list["BenchmarkDerivative"]] = relationship(
        secondary=association_table2, back_populates="curves"
    )


class SondeoLocal(Base):
    __tablename__ = "SONDEOS_LOCALES"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    maturity: Mapped[int] = mapped_column(Integer)
    emisor_moneda_id: Mapped[int] = mapped_column(ForeignKey(EmisorMonedaMarket.id))
    quote_id: Mapped[int] = mapped_column(ForeignKey(Quote.id))
    ytm: Mapped[float] = mapped_column(Float)

    emisor_moneda: Mapped["EmisorMonedaMarket"] = relationship(
        back_populates="sondeos_locales"
    )
    quote: Mapped["Quote"] = relationship(back_populates="sondeos_locales")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "maturity": self.maturity,
            "emisor_moneda": self.emisor_moneda.emisor_moneda,
            "quote": self.quote.quote,
            "ytm": self.ytm,
        }


class SondeoEurobono(Base):
    __tablename__ = "SONDEOS_EUROBONOS"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    titulo_id: Mapped[int] = mapped_column(ForeignKey(Titulo.id))
    quote_id: Mapped[int] = mapped_column(ForeignKey(Quote.id))
    ytm: Mapped[float | None] = mapped_column(Float, nullable=True)
    price: Mapped[float | None] = mapped_column(Float, nullable=True)

    titulo: Mapped["Titulo"] = relationship(back_populates="sondeos_eurobonos")
    quote: Mapped["Quote"] = relationship(back_populates="sondeos_eurobonos")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "titulo": self.titulo.isin,
            "maturity": self.titulo.fecha_vencimiento,
            "quote": self.quote.quote,
            "ytm": self.ytm,
            "price": self.price,
        }


class SondeosFredOption(Base):
    __tablename__ = "SONDEOS_FRED"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    variable_id: Mapped[int] = mapped_column(ForeignKey(VariablesMarket.id))
    maturity: Mapped[float] = mapped_column(Float)
    curve_id: Mapped[int] = mapped_column(ForeignKey(Curve.id))

    variable: Mapped["VariablesMarket"] = relationship(back_populates="sondeos_fred")
    curve: Mapped["Curve"] = relationship(back_populates="sondeos_fred")


class CurveInflationLinkage(Base):
    __tablename__ = "CURVE_INFLATION_LINKAGE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    inflation_id: Mapped[int] = mapped_column(ForeignKey(VariablesMarket.id))
    curve_id: Mapped[int] = mapped_column(ForeignKey(Curve.id))

    variable: Mapped["VariablesMarket"] = relationship(
        back_populates="curve_inflation_link"
    )
    curve: Mapped["Curve"] = relationship(back_populates="curve_inflation_link")


class Parametro(Base):
    __tablename__ = "PARAMETROS"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    curve_id: Mapped[int] = mapped_column(ForeignKey(Curve.id))
    tau1: Mapped[float] = mapped_column(Float)
    tau2: Mapped[float | None] = mapped_column(Float)
    b0: Mapped[float] = mapped_column(Float)
    b1: Mapped[float] = mapped_column(Float)
    b2: Mapped[float] = mapped_column(Float)
    b3: Mapped[float | None] = mapped_column(Float)

    curve: Mapped["Curve"] = relationship(back_populates="parametros")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "curve": self.curve.name,
            "tau1": self.tau1,
            "tau2": self.tau2,
            "b0": self.b0,
            "b1": self.b1,
            "b2": self.b2,
            "b3": self.b3,
        }

    def __str__(self):
        return (
            f"date={self.date}, "
            f"curve={self.curve.name}, "
            f"tau1={self.tau1}, "
            f"tau2={self.tau2}, "
            f"b0={self.b0}, "
            f"b1={self.b1}, "
            f"b2={self.b2}, "
            f"b3={self.b3})"
        )


class ValuationMethodOption(Base):
    __tablename__ = "VALUATION_METHOD_OPTION"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    option: Mapped[str] = mapped_column(String(15), unique=True)

    valuation_methods: Mapped[list["ValuationMethod"]] = relationship(
        back_populates="valuation_method_option"
    )


class ValuationMethod(Base):
    __tablename__ = "VALUATION_METHOD"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    valuation_method_option_id: Mapped[int] = mapped_column(
        ForeignKey(ValuationMethodOption.id)
    )
    curve_id: Mapped[int | None] = mapped_column(ForeignKey(Curve.id))
    quote_id: Mapped[int | None] = mapped_column(ForeignKey(Quote.id))

    valuation_method_option: Mapped["ValuationMethodOption"] = relationship(
        back_populates="valuation_methods"
    )
    quote: Mapped["Quote"] = relationship(back_populates="valuation_methods")
    curve: Mapped["Curve"] = relationship(back_populates="valuation_method")
    vectores_precios: Mapped[list["VectorPrecio"]] = relationship(
        back_populates="valuation_method"
    )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "valuation_method_option": self.valuation_method_option.option,
            "curve": self.curve.name if self.curve else None,
            "quote": self.quote.quote if self.quote else None,
            "method": self.curve.method.method if self.curve else None,
            "market": self.curve.quote.quote if self.curve else self.quote.quote,
        }


class VectorPrecio(Base):
    __tablename__ = "VECTOR_PRECIO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    titulo_id: Mapped[int] = mapped_column(ForeignKey(Titulo.id))
    valuation_method_id: Mapped[int] = mapped_column(ForeignKey(ValuationMethod.id))
    ytm: Mapped[float | None] = mapped_column(Float)
    clean_price: Mapped[float | None] = mapped_column(Float)
    dirty_price: Mapped[float | None] = mapped_column(Float)
    theta: Mapped[float | None] = mapped_column(Float)
    time: Mapped[float | None] = mapped_column(Float)
    current_yield: Mapped[float | None] = mapped_column(Float)
    mcauly_duration: Mapped[float | None] = mapped_column(Float)
    mduration: Mapped[float | None] = mapped_column(Float)
    convexity: Mapped[float | None] = mapped_column(Float)
    coupon: Mapped[float | None] = mapped_column(Float)
    dollar_duration: Mapped[float | None] = mapped_column(Float)
    dollar_convexity: Mapped[float | None] = mapped_column(Float)

    titulo: Mapped["Titulo"] = relationship(back_populates="vector_precio")
    valuation_method: Mapped["ValuationMethod"] = relationship(
        back_populates="vectores_precios"
    )

    def __str__(self):
        return (
            f"date={self.date}, "
            f"titulo={self.titulo.isin}, "
            f"valuation_method={self.valuation_method.name}, "
            f"ytm={self.ytm}, "
            f"clean_price={self.clean_price}, "
            f"dirty_price={self.dirty_price})"
        )


association_table = Table(
    "BENCHMARK_DERIVATIVE_LINKAGE",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("benchmark_id", Integer, ForeignKey("YIELD.CURVE_BENCHMARK.id")),
    Column("benchmark_derivative_id", Integer, ForeignKey("YIELD.DERIVATIVE.id")),
    Column("index", Integer),
    schema="YIELD",
    extend_existing=True,  # Esto es importante para evitar el error
)


class TimeSeriesState(Base):
    __tablename__ = "TIME_SERIES_STATE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    state: Mapped[str] = mapped_column(String(50), unique=True)

    benchmark_facts: Mapped[list["BenchmarkFact"]] = relationship(
        back_populates="state"
    )
    derivative_facts: Mapped[list["DerivativeFact"]] = relationship(
        back_populates="state"
    )


class CurveBenchmark(Base):
    __tablename__ = "CURVE_BENCHMARK"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    maturity: Mapped[float] = mapped_column(Float)
    curve_id: Mapped[int] = mapped_column(ForeignKey(Curve.id))

    curve: Mapped["Curve"] = relationship(back_populates="benchmarks")
    benchmark_facts: Mapped[list["BenchmarkFact"]] = relationship(
        back_populates="curve_benchmark"
    )
    derivatives: Mapped[list["BenchmarkDerivative"]] = relationship(
        secondary=association_table, back_populates="benchmarks"
    )
    probability_facts: Mapped[list["ProbabilityFact"]] = relationship(
        back_populates="benchmark"
    )


class BenchmarkFact(Base):
    __tablename__ = "BENCHMARK_FACT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    curve_benchmark_id: Mapped[int] = mapped_column(ForeignKey(CurveBenchmark.id))
    state_id: Mapped[int] = mapped_column(ForeignKey(TimeSeriesState.id))
    value: Mapped[float] = mapped_column(Float)

    curve_benchmark: Mapped["CurveBenchmark"] = relationship(
        back_populates="benchmark_facts"
    )
    state: Mapped["TimeSeriesState"] = relationship(back_populates="benchmark_facts")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "curve_benchmark": self.curve_benchmark.name,
            "state": self.state.state,
            "value": self.value,
        }

    def __str__(self):
        return (
            f"date={self.date}, "
            f"curve_benchmark={self.curve_benchmark.name}, "
            f"value={self.value})"
        )


class Scenario(Base):
    __tablename__ = "SCENARIO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    upper_bound: Mapped[float] = mapped_column(Float)
    lower_bound: Mapped[float] = mapped_column(Float)

    probability_facts: Mapped[list["ProbabilityFact"]] = relationship(
        back_populates="scenario"
    )


class ProbabilityFact(Base):
    __tablename__ = "PROBABILITY_FACT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    benchmark_id: Mapped[int] = mapped_column(ForeignKey(CurveBenchmark.id))
    scenario_id: Mapped[int] = mapped_column(ForeignKey(Scenario.id))
    value: Mapped[float] = mapped_column(Float)

    benchmark: Mapped["CurveBenchmark"] = relationship(
        back_populates="probability_facts"
    )
    scenario: Mapped["Scenario"] = relationship(back_populates="probability_facts")


class TypeDerivative(Base):
    __tablename__ = "TIPO_DERIVADO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String(30), unique=True)

    derivatives: Mapped[list["BenchmarkDerivative"]] = relationship(
        back_populates="type_derivative"
    )


class BenchmarkDerivative(Base):
    __tablename__ = "DERIVATIVE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(75), unique=True)
    type_derivative_id: Mapped[int] = mapped_column(ForeignKey(TypeDerivative.id))
    time: Mapped[float] = mapped_column(Float)

    type_derivative: Mapped["TypeDerivative"] = relationship(
        back_populates="derivatives"
    )
    benchmarks: Mapped[list["CurveBenchmark"]] = relationship(
        secondary=association_table, back_populates="derivatives"
    )
    curves: Mapped[list["Curve"]] = relationship(
        secondary=association_table2, back_populates="derivatives"
    )
    derivative_facts: Mapped[list["DerivativeFact"]] = relationship(
        back_populates="benchmark_derivative"
    )


class DerivativeFact(Base):
    __tablename__ = "DERIVATIVE_FACT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    benchmark_derivative_id: Mapped[int] = mapped_column(
        ForeignKey(BenchmarkDerivative.id)
    )
    state_id: Mapped[int] = mapped_column(ForeignKey(TimeSeriesState.id))
    value: Mapped[float] = mapped_column(Float)

    benchmark_derivative: Mapped["BenchmarkDerivative"] = relationship(
        back_populates="derivative_facts"
    )
    state: Mapped["TimeSeriesState"] = relationship(back_populates="derivative_facts")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "benchmark_derivative": self.benchmark_derivative.name,
            "state": self.state.state,
            "value": self.value,
        }


class CurveDerivativeLinkage(Base):
    __tablename__ = "CURVE_DERIVATIVE_LINKAGE"
    __table_args__ = ARGS

    id = Column(Integer, primary_key=True, autoincrement=True)
    curve_id = Column(Integer, ForeignKey(Curve.id))
    benchmark_derivative_id = Column(Integer, ForeignKey(BenchmarkDerivative.id))
    index = Column(Integer)


class BenchmarkDerivativeLinkage(Base):
    __tablename__ = "BENCHMARK_DERIVATIVE_LINKAGE"
    __table_args__ = ARGS

    id = Column(Integer, primary_key=True, autoincrement=True)
    benchmark_id = Column(Integer, ForeignKey(CurveBenchmark.id))
    benchmark_derivative_id = Column(Integer, ForeignKey(BenchmarkDerivative.id))
    index = Column(Integer)


class TituloView(Base):
    __tablename__ = "MAESTRO_TITULO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    isin: Mapped[str] = mapped_column(String(100), unique=True)
    emision: Mapped[time | None] = mapped_column(Date)
    vencimiento: Mapped[time | None] = mapped_column(Date)
    cupon: Mapped[float | None] = mapped_column(Float)
    periodicidad_pago: Mapped[str | None] = mapped_column(String(10))
    moneda: Mapped[str | None] = mapped_column(String(10))
    amortizable: Mapped[int | None] = mapped_column(Integer)
    base_pago: Mapped[str | None] = mapped_column(String(10))


class DatoView(Base):
    __tablename__ = "DATOS_VIEW"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    index: Mapped[str] = mapped_column(String(100))
    value: Mapped[float] = mapped_column(Float)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "index": self.index,
            "value": self.value,
        }

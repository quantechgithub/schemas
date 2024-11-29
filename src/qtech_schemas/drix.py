from pandas import Timestamp as time
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from qtech_schemas._yield import ValuationMethod
from qtech_schemas.dbo import Base
from qtech_schemas.market import Emisor, Maestro, Moneda, TipoEmisor, TipoTasa

ARGS = {"schema": "DRIX", "extend_existing": True}  # ,'extend_existing': True


class IndexStatus(Base):
    __tablename__ = "INDEX_STATUS"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    status: Mapped[str] = mapped_column(String(100), unique=True)

    indexes: Mapped[list["Index"]] = relationship(back_populates="status")


class Frequency(Base):
    __tablename__ = "FREQUENCY"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    frequency: Mapped[str] = mapped_column(String(100), unique=True)

    schedules: Mapped[list["Schedule"]] = relationship(back_populates="frequency_rel")


class Convention(Base):
    __tablename__ = "CONVENTION"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    convention: Mapped[str] = mapped_column(String(100), unique=True)

    schedules_convention: Mapped[list["Schedule"]] = relationship(
        foreign_keys="[Schedule.convention]", back_populates="convention_rel"
    )
    schedules_termination: Mapped[list["Schedule"]] = relationship(
        foreign_keys="[Schedule.terminationDateConvention]",
        back_populates="termination_convention_rel",
    )


class DateGenerationRule(Base):
    __tablename__ = "DATE_GENERATION_RULE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    rule: Mapped[str] = mapped_column(String(100), unique=True)

    schedules: Mapped[list["Schedule"]] = relationship(back_populates="rule_rel")


class Schedule(Base):
    __tablename__ = "SCHEDULE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    start_date: Mapped[time] = mapped_column(Date)
    end_date: Mapped[time] = mapped_column(Date)
    frequency: Mapped[int] = mapped_column(Integer, ForeignKey(Frequency.id))
    convention: Mapped[int] = mapped_column(Integer, ForeignKey(Convention.id))
    terminationDateConvention: Mapped[int] = mapped_column(
        Integer, ForeignKey(Convention.id)
    )
    rule: Mapped[int] = mapped_column(Integer, ForeignKey(DateGenerationRule.id))
    endOfMonth: Mapped[bool] = mapped_column(Boolean)

    frequency_rel: Mapped["Frequency"] = relationship(back_populates="schedules")
    convention_rel: Mapped["Convention"] = relationship(
        foreign_keys=[convention], back_populates="schedules_convention"
    )
    termination_convention_rel: Mapped["Convention"] = relationship(
        foreign_keys=[terminationDateConvention], back_populates="schedules_termination"
    )
    rule_rel: Mapped["DateGenerationRule"] = relationship(back_populates="schedules")
    indexes_rebalancing: Mapped[list["Index"]] = relationship(
        foreign_keys="[Index.rebalancing_schedule_id]",
        back_populates="rebalancing_schedule",
    )
    indexes_return: Mapped[list["Index"]] = relationship(
        foreign_keys="[Index.return_schedule_id]", back_populates="return_schedule"
    )


class RebalancingRules(Base):
    __tablename__ = "REBALANCING_RULES"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    issuer_type: Mapped[int] = mapped_column(Integer, ForeignKey(TipoEmisor.id))
    issuer: Mapped[int] = mapped_column(Integer, ForeignKey(Emisor.id))
    type_rate: Mapped[int] = mapped_column(Integer, ForeignKey(TipoTasa.id))
    currency: Mapped[int] = mapped_column(Integer, ForeignKey(Moneda.id))
    locality: Mapped[str] = mapped_column(String(30))
    type_amortizaton: Mapped[bool] = mapped_column(Boolean)
    days_since_issued: Mapped[int] = mapped_column(Integer)
    days_until_maturity: Mapped[int] = mapped_column(Integer)
    minimum_outstanding: Mapped[float] = mapped_column(Float)

    indexes: Mapped[list["Index"]] = relationship(back_populates="rebalancing_rules")


index_risk_factor_linkage = Table(
    "MATURITY_RISK_FACTOR_LINKAGE",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("index_id", Integer, ForeignKey("DRIX.INDEX.id")),
    Column("maturity_risk_factor_id", Integer, ForeignKey("DRIX.RISK_FACTOR.id")),
    schema="DRIX",
)


class MaturityRiskFactor(Base):
    __tablename__ = "MATURITY_RISK_FACTOR"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    maturity: Mapped[float] = mapped_column(Float)

    indexes: Mapped[list["Index"]] = relationship(
        secondary=index_risk_factor_linkage, back_populates="maturity_risk_factors"
    )
    positions: Mapped[list["Position"]] = relationship(
        back_populates="maturity_risk_factor"
    )


class Index(Base):
    __tablename__ = "INDEX"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    launch_date: Mapped[time] = mapped_column(Date)
    include_paydown_returns: Mapped[bool] = mapped_column(Boolean)
    levered: Mapped[bool] = mapped_column(Boolean)
    reporting_currency_id: Mapped[int] = mapped_column(Integer, ForeignKey(Moneda.id))
    valuation_method_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(ValuationMethod.id)
    )
    status_id: Mapped[int] = mapped_column(Integer, ForeignKey(IndexStatus.id))
    rebalancing_schedule_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Schedule.id)
    )
    return_schedule_id: Mapped[int] = mapped_column(Integer, ForeignKey(Schedule.id))
    rebalancing_rules_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(RebalancingRules.id)
    )

    status: Mapped["IndexStatus"] = relationship(back_populates="indexes")
    rebalancing_schedule: Mapped["Schedule"] = relationship(
        foreign_keys=[rebalancing_schedule_id], back_populates="indexes_rebalancing"
    )
    return_schedule: Mapped["Schedule"] = relationship(
        foreign_keys=[return_schedule_id], back_populates="indexes_return"
    )
    rebalancing_rules: Mapped["RebalancingRules"] = relationship(
        back_populates="indexes"
    )
    maturity_risk_factors: Mapped[list["MaturityRiskFactor"]] = relationship(
        secondary=index_risk_factor_linkage, back_populates="indexes"
    )
    positions: Mapped[list["Position"]] = relationship(back_populates="index")
    weights: Mapped[list["WeightFact"]] = relationship(back_populates="index")
    returns: Mapped[list["ReturnFact"]] = relationship(back_populates="index")
    facts: Mapped[list["IndexFact"]] = relationship(back_populates="index")


class Position(Base):
    __tablename__ = "POSITION"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    index_id: Mapped[int] = mapped_column(Integer, ForeignKey(Index.id))
    instrument_id: Mapped[int] = mapped_column(Integer, ForeignKey(Maestro.id))
    clean_price: Mapped[float] = mapped_column(Float)
    maturity_risk_factor_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(MaturityRiskFactor.id)
    )
    position: Mapped[float] = mapped_column(Float)

    index: Mapped["Index"] = relationship(back_populates="positions")
    maturity_risk_factor: Mapped["MaturityRiskFactor"] = relationship(
        back_populates="positions"
    )


class WeightType(Base):
    __tablename__ = "WEIGHT_TYPE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    weight_type: Mapped[str] = mapped_column(String(100), unique=True)

    weights: Mapped[list["WeightFact"]] = relationship(back_populates="weight_type")


class WeightFact(Base):
    __tablename__ = "WEIGHT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    index_id: Mapped[int] = mapped_column(Integer, ForeignKey(Index.id))
    weight_type_id: Mapped[int] = mapped_column(Integer, ForeignKey(WeightType.id))
    value: Mapped[float] = mapped_column(Float)

    index: Mapped["Index"] = relationship(back_populates="weights")
    weight_type: Mapped["WeightType"] = relationship(back_populates="weights")


class ReturnType(Base):
    __tablename__ = "RETURN_TYPE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    return_type: Mapped[str] = mapped_column(String(100), unique=True)

    returns: Mapped[list["ReturnFact"]] = relationship(back_populates="return_type")


class ReturnFact(Base):
    __tablename__ = "RETURN"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    index_id: Mapped[int] = mapped_column(Integer, ForeignKey(Index.id))
    return_type_id: Mapped[int] = mapped_column(Integer, ForeignKey(ReturnType.id))
    value: Mapped[float] = mapped_column(Float)

    index: Mapped["Index"] = relationship(back_populates="returns")
    return_type: Mapped["ReturnType"] = relationship(back_populates="returns")


class IndexVariables(Base):
    __tablename__ = "INDEX_VARIABLES"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    facts: Mapped[list["IndexFact"]] = relationship(back_populates="variable")
    # A la clase le falta la definición de metodos de extraccción, transformacion y carga.


class IndexFact(Base):
    __tablename__ = "INDEX_FACT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    index_id: Mapped[int] = mapped_column(Integer, ForeignKey(Index.id))
    variable_id: Mapped[int] = mapped_column(Integer, ForeignKey(IndexVariables.id))
    value: Mapped[float] = mapped_column(Float)

    index: Mapped["Index"] = relationship(back_populates="facts")
    variable: Mapped["IndexVariables"] = relationship(back_populates="facts")


# class TimeSeriesStateDrix(TimeSeriesState):
#     pass

# class Index(Base):
#     __tablename__ = 'INDEX'
#     __table_args__ = ARGS

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     name : Mapped[str] = mapped_column(String(100), unique=True)
#     weighting_method_id: Mapped[int] = mapped_column(Integer, ForeignKey(WeightingMethod.id))
#     rebalancing_frequency_id: Mapped[int] = mapped_column(Integer, ForeignKey(RebalancingFrequency.id))
#     calculation_frequency_id: Mapped[int] = mapped_column(Integer, ForeignKey(CalculationFrequency.id))
#     reporting_currency_id: Mapped[int] = mapped_column(Integer, ForeignKey(MonedaDrix.id))
#     launch_date: Mapped[time] = mapped_column(Date)
#     type_id: Mapped[int] = mapped_column(Integer, ForeignKey(IndexType.id))
#     valuation_method_id: Mapped[int] = mapped_column(Integer, ForeignKey(ValuationMethodDrix.id))
#     status_id: Mapped[int] = mapped_column(Integer, ForeignKey(IndexStatus.id))

#     weighting_method: Mapped[WeightingMethod] = relationship(back_populates ='indexes')
#     rebalancing_frequency: Mapped[RebalancingFrequency] = relationship(back_populates ='indexes')
#     calculation_frequency: Mapped[CalculationFrequency] = relationship(back_populates ='indexes')
#     reporting_currency: Mapped[MonedaDrix] = relationship(back_populates ='indexes')
#     index_type: Mapped[IndexType] = relationship(back_populates ='indexes')
#     valuation_method: Mapped[ValuationMethodDrix] = relationship(back_populates ='indexes')
#     status: Mapped[IndexStatus] = relationship(back_populates ='indexes')
#     risk_factors: Mapped[List[RiskFactor]] = relationship(secondary = index_risk_factor_linkage, back_populates='indexes')
#     emisor_moneda: Mapped[List[EmisorMonedaDrix]] = relationship(secondary = index_emisor_moneda_linkage, back_populates='indexes')

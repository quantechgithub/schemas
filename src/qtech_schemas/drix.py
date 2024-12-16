from pandas import Timestamp as time
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from qtech_schemas._yield import ValuationMethod
from qtech_schemas.dbo import Base
from qtech_schemas.market import Emisor, Maestro, Moneda, TipoEmisor, TipoTasa

ARGS = {"schema": "DRIX", "extend_existing": True}  # ,'extend_existing': True


class Issuer(Emisor):
    rebalancing_rules: Mapped[list["RebalancingRules"]] = relationship(
        back_populates="issuer_rel"
    )


class Currency(Moneda):
    rebalancing_rules: Mapped[list["RebalancingRules"]] = relationship(
        back_populates="currency_rel"
    )
    indexes: Mapped[list["Index"]] = relationship(back_populates="reporting_currency")


class IssuerType(TipoEmisor):
    rebalancing_rules: Mapped[list["RebalancingRules"]] = relationship(
        back_populates="issuer_type_rel"
    )


class RateType(TipoTasa):
    rebalancing_rules: Mapped[list["RebalancingRules"]] = relationship(
        back_populates="type_rate_rel"
    )


class SecuritiesMaster(Maestro):
    positions: Mapped[list["Position"]] = relationship(back_populates="instrument")


class PricingMethod(ValuationMethod):
    indexes: Mapped[list["Index"]] = relationship(back_populates="valuation_method")


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
    frequency_id: Mapped[int] = mapped_column(Integer, ForeignKey(Frequency.id))
    convention_id: Mapped[int] = mapped_column(Integer, ForeignKey(Convention.id))
    terminationDateConvention_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Convention.id)
    )
    rule: Mapped[int] = mapped_column(Integer, ForeignKey(DateGenerationRule.id))
    endOfMonth: Mapped[bool] = mapped_column(Boolean)

    frequency_rel: Mapped["Frequency"] = relationship(
        back_populates="schedules", lazy="joined"
    )
    convention_rel: Mapped["Convention"] = relationship(
        foreign_keys=[convention_id],
        lazy="joined",
    )
    termination_convention_rel: Mapped["Convention"] = relationship(
        foreign_keys=[terminationDateConvention_id],
        lazy="joined",
    )
    rule_rel: Mapped["DateGenerationRule"] = relationship(
        back_populates="schedules", lazy="joined"
    )


class RebalancingRules(Base):
    __tablename__ = "REBALANCING_RULES"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    issuer_type: Mapped[int | None] = mapped_column(Integer, ForeignKey(IssuerType.id))
    issuer: Mapped[int | None] = mapped_column(Integer, ForeignKey(Issuer.id))
    type_rate: Mapped[int | None] = mapped_column(Integer, ForeignKey(RateType.id))
    currency: Mapped[int | None] = mapped_column(Integer, ForeignKey(Currency.id))
    locality: Mapped[str | None] = mapped_column(String(30))
    type_amortizaton: Mapped[bool | None] = mapped_column(Boolean)
    days_since_issued: Mapped[int | None] = mapped_column(Integer)
    days_until_maturity: Mapped[int | None] = mapped_column(Integer)
    minimum_outstanding: Mapped[float | None] = mapped_column(Float)

    issuer_type_rel: Mapped["IssuerType"] = relationship(
        back_populates="rebalancing_rules", lazy="joined"
    )
    issuer_rel: Mapped["Issuer"] = relationship(
        back_populates="rebalancing_rules", lazy="joined"
    )
    type_rate_rel: Mapped["RateType"] = relationship(
        back_populates="rebalancing_rules", lazy="joined"
    )
    currency_rel: Mapped["Currency"] = relationship(
        back_populates="rebalancing_rules", lazy="joined"
    )
    indexes: Mapped[list["Index"]] = relationship(
        back_populates="rebalancing_rules", lazy="joined"
    )


index_risk_factor_linkage = Table(
    "MATURITY_RISK_FACTOR_LINKAGE",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("index_id", Integer, ForeignKey("DRIX.INDEX.id")),
    Column(
        "maturity_risk_factor_id", Integer, ForeignKey("DRIX.MATURITY_RISK_FACTOR.id")
    ),
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
    reporting_currency_id: Mapped[int] = mapped_column(Integer, ForeignKey(Currency.id))
    valuation_method_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(PricingMethod.id)
    )
    status_id: Mapped[int] = mapped_column(Integer, ForeignKey(IndexStatus.id))
    rebalancing_schedule_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Schedule.id)
    )
    return_schedule_id: Mapped[int] = mapped_column(Integer, ForeignKey(Schedule.id))
    rebalancing_rules_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(RebalancingRules.id)
    )

    reporting_currency: Mapped["Currency"] = relationship(
        back_populates="indexes", lazy="joined"
    )
    valuation_method: Mapped["PricingMethod"] = relationship(back_populates="indexes")
    status: Mapped["IndexStatus"] = relationship(
        back_populates="indexes", lazy="joined"
    )
    rebalancing_schedule: Mapped["Schedule"] = relationship(
        foreign_keys=[rebalancing_schedule_id],
        lazy="joined",
    )
    return_schedule: Mapped["Schedule"] = relationship(
        foreign_keys=[return_schedule_id],
        lazy="joined",
    )
    rebalancing_rules: Mapped["RebalancingRules"] = relationship(
        back_populates="indexes", lazy="joined"
    )
    maturity_risk_factors: Mapped[list["MaturityRiskFactor"]] = relationship(
        secondary=index_risk_factor_linkage, back_populates="indexes", lazy="joined"
    )
    positions: Mapped[list["Position"]] = relationship(back_populates="index")
    variables: Mapped[list["IndexVariables"]] = relationship(back_populates="index")


class Position(Base):
    __tablename__ = "POSITION"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    index_id: Mapped[int] = mapped_column(Integer, ForeignKey(Index.id))
    instrument_id: Mapped[int] = mapped_column(Integer, ForeignKey(SecuritiesMaster.id))
    clean_price: Mapped[float] = mapped_column(Float)
    maturity_risk_factor_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(MaturityRiskFactor.id)
    )
    position: Mapped[float] = mapped_column(Float)

    instrument: Mapped["SecuritiesMaster"] = relationship(
        back_populates="positions", lazy="joined"
    )
    index: Mapped["Index"] = relationship(back_populates="positions", lazy="joined")
    maturity_risk_factor: Mapped["MaturityRiskFactor"] = relationship(
        back_populates="positions", lazy="joined"
    )
    weights: Mapped[list["WeightFact"]] = relationship(back_populates="position")
    weighted_returns: Mapped[list["WeightedReturnFact"]] = relationship(
        back_populates="position"
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
    position_id: Mapped[int] = mapped_column(Integer, ForeignKey(Position.id))
    weight_type_id: Mapped[int] = mapped_column(Integer, ForeignKey(WeightType.id))
    value: Mapped[float] = mapped_column(Float)

    position: Mapped["Position"] = relationship(back_populates="weights", lazy="joined")
    weight_type: Mapped["WeightType"] = relationship(
        back_populates="weights", lazy="joined"
    )


class SeriesState(Base):
    __tablename__ = "TIME_SERIES_STATE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    state: Mapped[str] = mapped_column(String(100), unique=True)

    weighted_returns: Mapped[list["WeightedReturnFact"]] = relationship(
        back_populates="state"
    )
    index_variables: Mapped[list["IndexVariables"]] = relationship(
        back_populates="state"
    )


class TransformMethod(Base):
    __tablename__ = "TRANSFORMED_METHOD"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)

    index_variables: Mapped[list["IndexVariables"]] = relationship(
        back_populates="transform_method"
    )


class IndexVariables(Base):
    __tablename__ = "VARIABLES"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    index_id: Mapped[int] = mapped_column(Integer, ForeignKey(Index.id))
    transform_method_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(TransformMethod.id)
    )
    state_id: Mapped[int] = mapped_column(Integer, ForeignKey(SeriesState.id))

    index: Mapped["Index"] = relationship(back_populates="variables", lazy="joined")
    transform_method: Mapped["TransformMethod"] = relationship(
        back_populates="index_variables", lazy="joined"
    )
    state: Mapped["SeriesState"] = relationship(
        back_populates="index_variables", lazy="joined"
    )
    facts: Mapped[list["IndexFact"]] = relationship(back_populates="variable")


class IndexFact(Base):
    __tablename__ = "INDEX_FACT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    variable_id: Mapped[int] = mapped_column(Integer, ForeignKey(IndexVariables.id))
    value: Mapped[float] = mapped_column(Float)

    variable: Mapped["IndexVariables"] = relationship(
        back_populates="facts", lazy="joined"
    )


class ReturnType(Base):
    __tablename__ = "RETURN_TYPE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    return_type: Mapped[str] = mapped_column(String(100), unique=True)

    weighted_returns: Mapped[list["WeightedReturnFact"]] = relationship(
        back_populates="return_type"
    )


class InterestType(Base):
    __tablename__ = "INTEREST_TYPE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    interest_type: Mapped[str] = mapped_column(String(100), unique=True)

    weighted_returns: Mapped[list["WeightedReturnFact"]] = relationship(
        back_populates="interest_type"
    )


class WeightedReturnFact(Base):
    __tablename__ = "WEIGHTED_RETURN_FACT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    position_id: Mapped[int] = mapped_column(Integer, ForeignKey(Position.id))
    return_type_id: Mapped[int] = mapped_column(Integer, ForeignKey(ReturnType.id))
    interest_type_id: Mapped[int] = mapped_column(Integer, ForeignKey(InterestType.id))
    state_id: Mapped[int] = mapped_column(Integer, ForeignKey(SeriesState.id))
    value: Mapped[float] = mapped_column(Float)

    position: Mapped["Position"] = relationship(
        back_populates="weighted_returns", lazy="joined"
    )
    return_type: Mapped["ReturnType"] = relationship(
        back_populates="weighted_returns", lazy="joined"
    )
    interest_type: Mapped["InterestType"] = relationship(
        back_populates="weighted_returns", lazy="joined"
    )
    state: Mapped["SeriesState"] = relationship(
        back_populates="weighted_returns", lazy="joined"
    )

from pandas import Timestamp as time
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from qtech_schemas.dbo import Base, Variables

ARGS = {"schema": "FX", "extend_existing": True}

association_table = Table(
    "VARIABLE_LINKAGE",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("variable_id", Integer, ForeignKey("FX.VARIABLE.id")),
    Column("dbo_id", Integer, ForeignKey("dbo.VARIABLES.id")),
    Column("index", Integer),
    schema="FX",
    extend_existing=True,
)


class VariablesDboFx(Variables):
    fx_variables: Mapped[list["FxVariable"]] = relationship(
        secondary=association_table, back_populates="dbo_variables"
    )


class FxQuote(Base):
    __tablename__ = "QUOTE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)

    variables: Mapped[list["FxVariable"]] = relationship(back_populates="quote")


class FxEntity(Base):
    __tablename__ = "ENTITIES"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)

    variables: Mapped[list["FxVariable"]] = relationship(back_populates="entity")


class FxType(Base):
    __tablename__ = "TYPE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)

    variables: Mapped[list["FxVariable"]] = relationship(back_populates="type")


class FxScenario(Base):
    __tablename__ = "SCENARIO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)
    upper_bound: Mapped[float] = mapped_column(Float)
    lower_bound: Mapped[float] = mapped_column(Float)

    probability_fact: Mapped[list["FxProbabilityFact"]] = relationship(
        back_populates="scenario"
    )


class FxTypeTransform(Base):
    __tablename__ = "TYPE_TRANSFORM"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)

    variables: Mapped[list["FxVariable"]] = relationship(
        "FxVariable",
        back_populates="transform",
        primaryjoin="FxTypeTransform.id == FxVariable.transform_id",
    )
    analytics: Mapped[list["FxAnalytics"]] = relationship(back_populates="transform")


class FxVariable(Base):
    __tablename__ = "VARIABLE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), unique=True)
    quote_id: Mapped[int | None] = mapped_column(ForeignKey(FxQuote.id))
    entity_id: Mapped[int | None] = mapped_column(ForeignKey(FxEntity.id))
    type_id: Mapped[int | None] = mapped_column(ForeignKey(FxType.id))
    transform_id: Mapped[int | None] = mapped_column(ForeignKey(FxTypeTransform.id))

    quote: Mapped[FxQuote] = relationship(back_populates="variables")
    entity: Mapped[FxEntity] = relationship(back_populates="variables")
    type: Mapped[FxType] = relationship(back_populates="variables")
    transform: Mapped[FxTypeTransform] = relationship(back_populates="variables")

    variable_facts: Mapped[list["FxVariableFact"]] = relationship(
        back_populates="variable"
    )
    dbo_variables: Mapped[list["VariablesDboFx"]] = relationship(
        secondary=association_table, back_populates="fx_variables"
    )
    analytics: Mapped[list["FxAnalytics"]] = relationship(back_populates="variable")


class VariableLinkage(Base):
    __tablename__ = "VARIABLE_LINKAGE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    variable_id: Mapped[int] = mapped_column(ForeignKey(FxVariable.id))
    dbo_id: Mapped[int] = mapped_column(ForeignKey(VariablesDboFx.id))
    index: Mapped[int] = mapped_column(Integer)


class FxVariableFact(Base):
    __tablename__ = "VARIABLE_FACT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    variable_id: Mapped[int] = mapped_column(ForeignKey(FxVariable.id))
    value: Mapped[float] = mapped_column(Float)

    variable: Mapped[FxVariable] = relationship(back_populates="variable_facts")


class FxAnalytics(Base):
    __tablename__ = "ANALYTICS"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), unique=True)
    variable_id: Mapped[int] = mapped_column(ForeignKey(FxVariable.id))
    transform_id: Mapped[int] = mapped_column(ForeignKey(FxTypeTransform.id))
    probability_calc_state: Mapped[bool] = mapped_column(Boolean)

    variable: Mapped[FxVariable] = relationship(back_populates="analytics")
    transform: Mapped[FxTypeTransform] = relationship(back_populates="analytics")
    analytics_facts: Mapped[list["FxAnalyticsFact"]] = relationship(
        back_populates="analytic"
    )
    probability_fact: Mapped[list["FxProbabilityFact"]] = relationship(
        back_populates="analytic"
    )


class FxAnalyticsFact(Base):
    __tablename__ = "ANALYTICS_FACT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    analytics_id: Mapped[int] = mapped_column(ForeignKey(FxAnalytics.id))
    value: Mapped[float | None] = mapped_column(Float)

    analytic: Mapped[FxAnalytics] = relationship(back_populates="analytics_facts")


class FxProbabilityFact(Base):
    __tablename__ = "PROBABILITY_FACT"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[time] = mapped_column(Date)
    scenario_id: Mapped[int] = mapped_column(ForeignKey(FxScenario.id))
    analytic_id: Mapped[int] = mapped_column(ForeignKey(FxAnalytics.id))
    value: Mapped[float] = mapped_column(Float)

    analytic: Mapped[FxAnalytics] = relationship(back_populates="probability_fact")
    scenario: Mapped[FxScenario] = relationship(back_populates="probability_fact")

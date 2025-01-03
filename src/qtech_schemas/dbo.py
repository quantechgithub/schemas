from pandas import Timestamp as time
from sqlalchemy import Date, Float, ForeignKey, Integer, MetaData, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

metadata_obj = MetaData()


class Base(DeclarativeBase):
    metadata = metadata_obj


ARGS = {"schema": "dbo", "extend_existing": True}


class Frecuencias(Base):
    __tablename__ = "Frecuencias"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(
        "Frecuencia_id", Integer, primary_key=True, autoincrement=True
    )
    frecuencia: Mapped[str] = mapped_column("Frecuenciaa", String)


class Categoria(Base):
    __tablename__ = "Categoria"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(
        "Categoria_id", Integer, primary_key=True, autoincrement=True
    )
    indice: Mapped[str] = mapped_column("Indice", String(50))
    categoria: Mapped[str] = mapped_column("Categoria", String(100))


class Fuentes(Base):
    __tablename__ = "Fuentes"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(
        "Fuente_ID", Integer, primary_key=True, autoincrement=True
    )
    fuente: Mapped[str] = mapped_column("Fuente", String(100))
    siglas: Mapped[str] = mapped_column("Siglas", String(30))


class Moneda(Base):
    __tablename__ = "Moneda"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(
        "Moneda_ID", Integer, primary_key=True, autoincrement=True
    )
    moneda: Mapped[str] = mapped_column("Moneda", String(30))


class Metodo_Extraccion(Base):
    __tablename__ = "Metodo_Extraccion"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(
        "Metodo_Extraccion_ID", Integer, primary_key=True, autoincrement=True
    )
    metodo_extraccion: Mapped[str] = mapped_column("Metodo_Extraccion", String(30))


class Transformacion(Base):
    __tablename__ = "Transformaciones"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(
        "Metodo_transformacion", Integer, primary_key=True, autoincrement=True
    )
    transformacion: Mapped[str] = mapped_column("Transformacion", String(50))


class Extraccion(Base):
    __tablename__ = "Extracciones"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(
        "Extract_Method", Integer, primary_key=True, autoincrement=True
    )
    transformacion: Mapped[str] = mapped_column("Extraccion", String(50))


class Cargas(Base):
    __tablename__ = "Cargas"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(
        "Metodo_carga", Integer, primary_key=True, autoincrement=True
    )
    carga: Mapped[str] = mapped_column("Carga", String(100))


class Variables(Base):
    __tablename__ = "Variables"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(
        "Variable_ID", Integer, primary_key=True, autoincrement=True
    )
    indice: Mapped[str] = mapped_column("Indice", String(100))
    variable: Mapped[str] = mapped_column("Variable", String(100))
    frecuencia: Mapped[int] = mapped_column(
        "Frecuencia_ID", Integer, ForeignKey(Frecuencias.id)
    )
    categoria: Mapped[int] = mapped_column(
        "Categoria_ID", Integer, ForeignKey(Categoria.id)
    )
    fuente_id: Mapped[int] = mapped_column("Fuente_ID", Integer, ForeignKey(Fuentes.id))
    moneda_id: Mapped[int | None] = mapped_column(
        "Moneda_ID", Integer, ForeignKey(Moneda.id)
    )
    metodo_extraccion_id: Mapped[int] = mapped_column(
        "Metodo_Extraccion_ID", Integer, ForeignKey(Metodo_Extraccion.id)
    )
    link: Mapped[str | None] = mapped_column("Link", String(100))
    sheet: Mapped[int] = mapped_column("Sheet", Integer)
    identificador: Mapped[str | None] = mapped_column("Identificador", String(50))
    firstcolumn: Mapped[int | None] = mapped_column("Firstcolumn", Integer)
    rowtitle: Mapped[str | None] = mapped_column("Rowtitle", String(100))
    frecuency: Mapped[int | None] = mapped_column("Frecuency", String(50))
    years: Mapped[int | None] = mapped_column("Years", Integer)
    months: Mapped[int | None] = mapped_column("Months", Integer)

    columnas: Mapped[str | None] = mapped_column("Columnas", String(50))
    inicio: Mapped[int | None] = mapped_column("Inicio", String(50))

    moneda: Mapped[str | None] = mapped_column("Moneda", String(50))
    cut: Mapped[int | None] = mapped_column("cut", Integer)
    fila: Mapped[int | None] = mapped_column("Fila", Integer)
    date_column: Mapped[int | None] = mapped_column("Datecolumn", Integer)
    metodo_transformacion: Mapped[int | None] = mapped_column(
        "Metodo_Transformacion", Integer, ForeignKey(Transformacion.id)
    )
    metodo_extraccion: Mapped[int | None] = mapped_column(
        "Metodo_Extraccion", Integer, ForeignKey(Metodo_Extraccion.id)
    )
    metodo_carga: Mapped[int | None] = mapped_column(
        "Metodo_Carga", Integer, ForeignKey(Cargas.id)
    )


class Fechas(Base):
    __tablename__ = "Fechas"
    __table_args__ = ARGS

    dates: Mapped[time] = mapped_column("Date", Date, primary_key=True)
    year: Mapped[int] = mapped_column("Year", Integer)
    semester: Mapped[int] = mapped_column("Semester", Integer)
    quarter: Mapped[int] = mapped_column("Quarter", Integer)
    month: Mapped[int] = mapped_column("Month", Integer)
    week: Mapped[int] = mapped_column("Week", Integer)
    day: Mapped[int] = mapped_column("Day", Integer)


class Datos(Base):
    __tablename__ = "Datos"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(
        "Datos_ID", Integer, primary_key=True, autoincrement=True
    )
    fecha: Mapped[time] = mapped_column("Fecha", Date, ForeignKey(Fechas.dates))
    frecuencia: Mapped[int] = mapped_column(
        "Frecuencia_ID", Integer, ForeignKey(Frecuencias.id)
    )
    categoria: Mapped[int] = mapped_column(
        "Categoria_ID", Integer, ForeignKey(Categoria.id)
    )
    fuente: Mapped[int] = mapped_column("Fuente_ID", Integer, ForeignKey(Fuentes.id))
    variable_id: Mapped[int] = mapped_column(
        "Variable_ID", Integer, ForeignKey(Variables.id)
    )
    moneda: Mapped[int] = mapped_column("Moneda_ID", Integer, ForeignKey(Moneda.id))
    valor: Mapped[float] = mapped_column("Valor", Float)

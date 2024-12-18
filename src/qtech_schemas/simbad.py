from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from qtech_schemas.dbo import Base

ARGS = {"schema": "SIMBAD", "extend_existing": True}


class TIPO_ENTIDAD(Base):
    __tablename__ = "TIPO_ENTIDAD"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    tipo_entidad: Mapped[str | None] = mapped_column("TIPO_ENTIDAD", String(100))

    def __repr__(self) -> str:
        return f"TIPO_ENTIDAD(ID={self.id!r}, TIPO_ENTIDAD={self.tipo_entidad!r})"


class ENTIDAD(Base):
    __tablename__ = "ENTIDAD"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    entidad: Mapped[str | None] = mapped_column("ENTIDAD", String(100))

    def __repr__(self) -> str:
        return f"ENTIDAD(ID={self.id!r}, ENTIDAD={self.entidad!r})"


class REGION(Base):
    __tablename__ = "REGION"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    region: Mapped[str | None] = mapped_column("REGION", String(100))

    def __repr__(self) -> str:
        return f"REGION(ID={self.id!r}, REGION={self.region!r})"


class PROVINCIA(Base):
    __tablename__ = "PROVINCIA"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    provincia: Mapped[str | None] = mapped_column("PROVINCIA", String(100))

    def __repr__(self) -> str:
        return f"PROVINCIA(ID={self.id!r}, PROVINCIA={self.provincia!r})"


class PERSONA(Base):
    __tablename__ = "PERSONA"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    persona: Mapped[str | None] = mapped_column("PERSONA", String(100))

    def __repr__(self) -> str:
        return f"PERSONA(ID={self.id!r}, PERSONA={self.persona!r})"


class GENERO(Base):
    __tablename__ = "GENERO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    genero: Mapped[str | None] = mapped_column("GENERO", String(100))

    def __repr__(self) -> str:
        return f"GENERO(ID={self.id!r}, GENERO={self.genero!r})"


class TIPO_CLIENTE(Base):
    __tablename__ = "TIPO_CLIENTE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    tipo_cliente: Mapped[str | None] = mapped_column("TIPO_CLIENTE", String(100))

    def __repr__(self) -> str:
        return f"TIPO_CLIENTE(ID={self.id!r}, TIPO_CLIENTE={self.tipo_cliente!r})"


class INSTRUMENTO_CAPTACION(Base):
    __tablename__ = "INSTRUMENTO_CAPTACION"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    instrumento_captacion: Mapped[str | None] = mapped_column(
        "INSTRUMENTO_CAPTACION", String(100)
    )

    def __repr__(self) -> str:
        return (
            f"INSTRUMENTO_CAPTACION("
            f"ID={self.id!r}, "
            f"INSTRUMENTO_CAPTACION={self.instrumento_captacion!r})"
        )


class MONEDA(Base):
    __tablename__ = "MONEDA"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    moneda: Mapped[str | None] = mapped_column("MONEDA", String(100))

    def __repr__(self) -> str:
        return f"MONEDA(ID={self.id!r}, MONEDA={self.moneda!r})"


class DIVISA(Base):
    __tablename__ = "DIVISA"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    divisa: Mapped[str | None] = mapped_column("DIVISA", String(100))

    def __repr__(self) -> str:
        return f"DIVISA(ID={self.id!r}, DIVISA={self.divisa!r})"


class PARTIDA_NIVEL_1(Base):
    __tablename__ = "PARTIDA_NIVEL_1"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    partida_nivel_1: Mapped[str | None] = mapped_column(
        "PUBLICO_PRIVADO_NIVEL_1", String(100)
    )

    def __repr__(self) -> str:
        return (
            f"PARTIDA_NIVEL_1("
            f"ID={self.id!r}, "
            f"PUBLICO_PRIVADO_NIVEL_1={self.partida_nivel_1!r})"
        )


class PARTIDA_NIVEL_2(Base):
    __tablename__ = "PARTIDA_NIVEL_2"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    partida_nivel_2: Mapped[str | None] = mapped_column("PARTIDA_NIVEL_2", String(100))

    def __repr__(self) -> str:
        return (
            f"PARTIDA_NIVEL_2(ID={self.id!r}, PARTIDA_NIVEL_2={self.partida_nivel_2!r})"
        )


class PUBLICO_PRIVADO_1(Base):
    __tablename__ = "PUBLICO_PRIVADO_1"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    publica_privado_1: Mapped[str | None] = mapped_column(
        "PUBLICO_PRIVADO_NIVEL_1", String(100)
    )

    def __repr__(self) -> str:
        return (
            f"PUBLICO_PRIVADO_1("
            f"ID={self.id!r}, "
            f"PUBLICO_PRIVADO_NIVEL_1={self.publica_privado_1!r})"
        )


class PUBLICO_PRIVADO_2(Base):
    __tablename__ = "PUBLICO_PRIVADO_2"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    publica_privado_2: Mapped[str | None] = mapped_column(
        "PUBLICO_PRIVADO_NIVEL_2", String(100)
    )

    def __repr__(self) -> str:
        return (
            f"PUBLICO_PRIVADO_2("
            f"ID={self.id!r}, "
            f"PUBLICO_PRIVADO_NIVEL_2={self.publica_privado_2!r})"
        )


class RESIDENTE_NORESIDENTE(Base):
    __tablename__ = "RESIDENTE_NORESIDENTE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    residente_noresidente: Mapped[str | None] = mapped_column(
        "RESIDENTE_NO_NORESIDENTE", String(100)
    )

    def __repr__(self) -> str:
        return (
            f"RESIDENTE_NORESIDENTE("
            f"ID={self.id!r}, "
            f"RESIDENTE_NO_NORESIDENTE={self.residente_noresidente!r})"
        )


class COMPONENTE(Base):
    __tablename__ = "COMPONENTE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    componente: Mapped[str | None] = mapped_column("COMPONENTE", String(100))

    def __repr__(self) -> str:
        return f"COMPONENTE(ID={self.id!r}, COMPONENTE={self.componente!r})"


class INSTRUMENTO_MEDIO(Base):
    __tablename__ = "INSTRUMENTO_MEDIO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    instrumento_medio: Mapped[str | None] = mapped_column(
        "INSTRUMENTO_MEDIO", String(100)
    )

    def __repr__(self) -> str:
        return (
            f"INSTRUMENTO_MEDIO("
            f"ID={self.id!r}, "
            f"INSTRUMENTO_MEDIO={self.instrumento_medio!r})"
        )


class CONTRAPARTE(Base):
    __tablename__ = "CONTRAPARTE"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    contraparte: Mapped[str | None] = mapped_column("CONTRA_PARTE", String(100))

    def __repr__(self) -> str:
        return f"CONTRAPARTE(ID={self.id!r}, CONTRA_PARTE={self.contraparte!r})"


class SITUACION_NIVEL1(Base):
    __tablename__ = "SITUACION_NIVEL1"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    situacion_nivel_1: Mapped[str | None] = mapped_column(
        "SITUACION_NIVEL_1", String(100)
    )

    def __repr__(self) -> str:
        return (
            f"SITUACION_NIVEL1("
            f"ID={self.id!r}, "
            f"SITUACION_NIVEL_1={self.situacion_nivel_1!r})"
        )


class SITUACION_NIVEL2(Base):
    __tablename__ = "SITUACION_NIVEL2"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    situacion_nivel_2: Mapped[str | None] = mapped_column(
        "SITUACION_NIVEL_2", String(100)
    )

    def __repr__(self) -> str:
        return (
            f"SITUACION_NIVEL2("
            f"ID={self.id!r}, "
            f"SITUACION_NIVEL_2={self.situacion_nivel_2!r})"
        )


class FINANCIERO_NOFINANCIERO(Base):
    __tablename__ = "FINANCIERO_NOFINANCIERO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    financiero_no_financiero: Mapped[str | None] = mapped_column(
        "FINANCIERO_NO_FINANCIERO", String(100)
    )

    def __repr__(self) -> str:
        return (
            f"FINANCIERO_NOFINANCIERO("
            f"ID={self.id!r}, "
            f"FINANCIERO_NO_FINANCIERO={self.financiero_no_financiero!r})"
        )


class CAPTACIONES(Base):
    __tablename__ = "CAPTACIONES"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    periodo: Mapped[str | None] = mapped_column("PERIODO", String(100))
    tipo_entidad: Mapped[int | None] = mapped_column(
        "TIPO_ENTIDAD", Integer, ForeignKey(TIPO_ENTIDAD.id)
    )
    entidad: Mapped[int | None] = mapped_column(
        "ENTIDAD", Integer, ForeignKey(ENTIDAD.id)
    )
    region: Mapped[int | None] = mapped_column("REGION", Integer, ForeignKey(REGION.id))
    provincia: Mapped[int | None] = mapped_column(
        "PROVINCIA", Integer, ForeignKey(PROVINCIA.id)
    )
    persona: Mapped[int | None] = mapped_column(
        "PERSONA", Integer, ForeignKey(PERSONA.id)
    )
    genero: Mapped[int | None] = mapped_column("GENERO", Integer, ForeignKey(GENERO.id))
    tipo_cliente: Mapped[int | None] = mapped_column(
        "TIPO_CLIENTE", Integer, ForeignKey(TIPO_CLIENTE.id)
    )
    instrumento_captacion: Mapped[int | None] = mapped_column(
        "INSTRUMENTO_CAPTACION", Integer, ForeignKey(INSTRUMENTO_CAPTACION.id)
    )
    moneda: Mapped[int | None] = mapped_column("MONEDA", Integer, ForeignKey(MONEDA.id))
    divisa: Mapped[int | None] = mapped_column("DIVISA", Integer, ForeignKey(DIVISA.id))
    partida_nivel_1: Mapped[int | None] = mapped_column(
        "PARTIDA_NIVEL_1", Integer, ForeignKey(PARTIDA_NIVEL_1.id)
    )
    partida_nivel_2: Mapped[int | None] = mapped_column(
        "PARTIDA_NIVEL_2", Integer, ForeignKey(PARTIDA_NIVEL_2.id)
    )
    publico_privado_nivel_1: Mapped[int | None] = mapped_column(
        "PUBLICO_PRIVADO_NIVEL_1", Integer, ForeignKey(PUBLICO_PRIVADO_1.id)
    )
    publico_privado_nivel_2: Mapped[int | None] = mapped_column(
        "PUBLICO_PRIVADO_NIVEL_2", Integer, ForeignKey(PUBLICO_PRIVADO_2.id)
    )
    financiero_no_financiero: Mapped[int | None] = mapped_column(
        "FINANCIERO_NO_FINANCIERO", Integer, ForeignKey(FINANCIERO_NOFINANCIERO.id)
    )
    residente_noresidente: Mapped[int | None] = mapped_column(
        "RESIDENTE_NO_RESIDENTE", Integer, ForeignKey(RESIDENTE_NORESIDENTE.id)
    )
    componente: Mapped[int | None] = mapped_column(
        "COMPONENTE", Integer, ForeignKey(COMPONENTE.id)
    )
    instrumento_medio: Mapped[int | None] = mapped_column(
        "INSTRUMENTO_MEDIO", Integer, ForeignKey(INSTRUMENTO_MEDIO.id)
    )
    contraparte: Mapped[int | None] = mapped_column(
        "CONTRA_PARTE", Integer, ForeignKey(CONTRAPARTE.id)
    )
    situacion_nivel_1: Mapped[int | None] = mapped_column(
        "SITUACION_NIVEL_1", Integer, ForeignKey(SITUACION_NIVEL1.id)
    )
    situacion_nivel_2: Mapped[int | None] = mapped_column(
        "SITUACION_NIVEL_2", Integer, ForeignKey(SITUACION_NIVEL2.id)
    )
    cantidad_instrumento: Mapped[float | None] = mapped_column(
        "CANTIDAD_INSTRUMENTO", Float
    )
    balance: Mapped[float | None] = mapped_column("BALANCE", Float)
    tasa_promedio_ponderado_balance: Mapped[float | None] = mapped_column(
        "TASA_PROMEDIO_PONDERADO_POR_BALANCE", Float
    )
    tasa_promedio_ponderado: Mapped[float | None] = mapped_column(
        "TASA_PROMEDIO_PONDERADO", Float
    )

    def __repr__(self) -> str:
        return (
            f"CAPTACIONES("
            f"ID={self.id!r}, "
            f"PERIODO={self.periodo!r}, "
            f"TIPO_ENTIDAD={self.tipo_entidad!r}, "
            f"ENTIDAD={self.entidad!r}, "
            f"REGION={self.region!r}, "
            f"PROVINCIA={self.provincia!r}, "
            f"PERSONA={self.persona!r}, "
            f"GENERO={self.genero!r}, "
            f"TIPO_CLIENTE={self.tipo_cliente!r}, "
            f"INSTRUMENTO_CAPTACION={self.instrumento_captacion!r}, "
            f"MONEDA={self.moneda!r}, "
            f"DIVISA={self.divisa!r}, "
            f"PARTIDA_NIVEL_1={self.partida_nivel_1!r}, "
            f"PARTIDA_NIVEL_2={self.partida_nivel_2!r}, "
            f"PUBLICO_PRIVADO_NIVEL_1={self.publico_privado_nivel_1!r}, "
            f"PUBLICO_PRIVADO_NIVEL_2={self.publico_privado_nivel_2!r}, "
            f"FINANCIERO_NO_FINANCIERO={self.financiero_no_financiero!r}, "
            f"RESIDENTE_NORESIDENTE={self.residente_noresidente!r}, "
            f"COMPONENTE={self.componente!r}, "
            f"INSTRUMENTO_MEDIO={self.instrumento_medio!r}, "
            f"CONTRAPARTE={self.contraparte!r}, "
            f"SITUACION_NIVEL_1={self.situacion_nivel_1!r}, "
            f"SITUACION_NIVEL_2={self.situacion_nivel_2!r}, "
            f"CANTIDAD_INSTRUMENTO={self.cantidad_instrumento!r}, "
            f"BALANCE={self.balance!r}, "
            f"TASA_PROMEDIO_PONDERADO_POR_BALANCE="
            f"{self.tasa_promedio_ponderado_balance!r}, "
            f"TASA_PROMEDIO_PONDERADO={self.tasa_promedio_ponderado!r})"
        )

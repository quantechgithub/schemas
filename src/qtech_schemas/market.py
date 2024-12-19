from pandas import Timestamp as time
from sqlalchemy import BigInteger, Date, Float, ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from qtech_schemas.dbo import Base

ARGS = {"schema": "MARKET", "extend_existing": True}


class Amortiza(Base):
    __tablename__ = "AMORTIZA"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    amortiza: Mapped[str] = mapped_column("AMORTIZA", String(20))

    def __repr__(self) -> str:
        return f"User(ID={self.id!r}, AMORTIZA={self.amortiza!r},"


class Sector(Base):
    __tablename__ = "SECTOR"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    sector: Mapped[str | None] = mapped_column("SECTOR", String(100))

    def __repr__(self) -> str:
        return f"Sector(ID={self.id!r}, SECTOR={self.sector!r})"


class Emisor(Base):
    __tablename__ = "EMISORES"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    siglas: Mapped[str | None] = mapped_column("SIGLAS", String(100))
    nombre: Mapped[str] = mapped_column("NOMBRE", String(200))
    sector_id: Mapped[int | None] = mapped_column(
        "SECTOR_ID", Integer, ForeignKey(Sector.id)
    )

    def __repr__(self) -> str:
        return (
            f"Emisores("
            f"ID={self.id!r}, "
            f"SIGLAS={self.siglas!r}, "
            f"NOMBRE={self.nombre!r}, "
            f"SECTOR={self.sector_id!r})"
        )


class SerieEmision(Base):
    __tablename__ = "SERIES_EMISION"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    siglas: Mapped[str | None] = mapped_column("SIGLAS", String(100))
    nombre: Mapped[str] = mapped_column("NOMBRE", String(260))
    nombre_bvrd: Mapped[str | None] = mapped_column("NOMBRE_BVRD", String(260))
    emisor_id: Mapped[int] = mapped_column("EMISOR_ID", ForeignKey(Emisor.id))

    def __repr__(self) -> str:
        return (
            f"User("
            f"ID={self.id!r}, "
            f"SIGLAS={self.siglas!r}, "
            f"NOMBRE={self.nombre!r}, "
            f"NOMBRE_BVRD={self.nombre_bvrd!r}, "
            f"EMISOR_ID={self.emisor_id!r})"
        )


class Moneda(Base):
    __tablename__ = "MONEDA"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    moneda: Mapped[str] = mapped_column("MONEDA", String(30))


class ClaseInstrumento(Base):
    __tablename__ = "CLASE_INSTRUMENTO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    clase: Mapped[str] = mapped_column("CLASE", String(30))


class TipoInstrumento(Base):
    __tablename__ = "TIPO_INSTRUMENTO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    tipo_instrumento: Mapped[str] = mapped_column("TIPO_INSTRUMENTO", String(100))
    siglas: Mapped[str | None] = mapped_column("SIGLAS", String(20))
    clase_instrumento: Mapped[int | None] = mapped_column(
        "CLASE_INSTRUMENTO_ID", Integer, ForeignKey(ClaseInstrumento.id)
    )
    titulos: Mapped[list["Maestro"]] = relationship(back_populates="tipo_instrumento")


class BasePago(Base):
    __tablename__ = "BASE_PAGO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    base_pago: Mapped[str] = mapped_column("BASE_PAGO", String(100))


class Periodicidad(Base):
    __tablename__ = "PERIODICIDAD_PAGO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    periodicidad: Mapped[str] = mapped_column("PERIODICIDAD_PAGO", String(50))
    periodicidad_bvrd: Mapped[str | None] = mapped_column(
        "PERIODICIDAD_BVRD", String(50)
    )


class EmisorMoneda(Base):
    __tablename__ = "EMISOR_MONEDA"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    emisor_moneda: Mapped[str] = mapped_column("EMISOR_MONEDA", String(100))

    titulos: Mapped[list["Maestro"]] = relationship(back_populates="emisor_moneda")


class MetodoCalculo(Base):
    __tablename__ = "METODO_CALCULO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    metodo_calculo: Mapped[str] = mapped_column("METODO_CALCULO", String(100))


class TipoTasa(Base):
    __tablename__ = "TIPO_TASA"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    tipo: Mapped[str] = mapped_column("TIPO_TASA", String(50))


class TipoEmisor(Base):
    __tablename__ = "TIPO_EMISOR"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    tipo: Mapped[str] = mapped_column("TIPO_EMISOR", String(50))


class TipoOperacion(Base):
    __tablename__ = "TIPO_OPERACIONES"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    tipo_operacion: Mapped[str] = mapped_column("TIPO_OPERACION", String(50))


class Parte(Base):
    __tablename__ = "PARTES"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    partes: Mapped[str] = mapped_column("PARTE", String(50))


class Sistema_Mercado(Base):
    __tablename__ = "SISTEMA_MERCADO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    registro: Mapped[str] = mapped_column("REGISTRO", String(100))


class Estado(Base):
    __tablename__ = "ESTADO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    estados: Mapped[str] = mapped_column("ESTADOS", String(50))


class Maestro(Base):
    __tablename__ = "MAESTRO_TITULOS"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    isin: Mapped[str] = mapped_column("ISIN", String(100), unique=True)
    fecha_emision: Mapped[time | None] = mapped_column("EMISION", Date)
    fecha_vencimiento: Mapped[time | None] = mapped_column("VENCIMIENTO", Date)
    cupon: Mapped[float | None] = mapped_column("CUPON", Float)
    amortiza_id: Mapped[int | None] = mapped_column(
        "AMORTIZA", Integer, ForeignKey(Amortiza.id)
    )
    serie_id: Mapped[int | None] = mapped_column(
        "SERIES_ID", Integer, ForeignKey(SerieEmision.id)
    )
    moneda_id: Mapped[int | None] = mapped_column(
        "MONEDA_ID", Integer, ForeignKey(Moneda.id)
    )
    tipo_id: Mapped[int | None] = mapped_column(
        "TIPO_ID", Integer, ForeignKey(TipoInstrumento.id)
    )
    base_id: Mapped[int | None] = mapped_column(
        "BASE_ID", Integer, ForeignKey(BasePago.id)
    )
    periodicidad_id: Mapped[int | None] = mapped_column(
        "PERIODICIDAD_ID", Integer, ForeignKey(Periodicidad.id)
    )
    monto_total_programa: Mapped[float | None] = mapped_column(
        "MONTO_TOTAL_PROGRAMA", Float
    )
    nemotecnico: Mapped[str | None] = mapped_column("NEMOTECNICO", String(100))
    option_call: Mapped[int | None] = mapped_column("OPTION_CALL", Integer)
    call_date: Mapped[time | None] = mapped_column("CALL_DATE", Date)
    emisor_moneda_id: Mapped[int | None] = mapped_column(
        "EMISOR_MONEDA_ID", Integer, ForeignKey(EmisorMoneda.id)
    )
    metodo_calculo_id: Mapped[int | None] = mapped_column(
        "METODO_CALCULO_ID", Integer, ForeignKey(MetodoCalculo.id)
    )
    calificacion_riesgo: Mapped[str | None] = mapped_column(
        "CALIFICACION_RIESGO", String(50)
    )
    tipo_tasa: Mapped[int | None] = mapped_column(
        "TIPO_TASA_ID", Integer, ForeignKey(TipoTasa.id)
    )
    sobre_tasa: Mapped[float | None] = mapped_column("SOBRE_TASA", Float)
    tipo_emisor: Mapped[int | None] = mapped_column(
        "TIPO_EMISOR", Integer, ForeignKey(TipoEmisor.id)
    )

    emisor_moneda: Mapped["EmisorMoneda"] = relationship(back_populates="titulos")
    tipo_instrumento: Mapped["TipoInstrumento"] = relationship(back_populates="titulos")
    emisor_moneda: Mapped["EmisorMoneda"] = relationship(back_populates="titulos")
    tipo_instrumento: Mapped["TipoInstrumento"] = relationship(back_populates="titulos")
    montos: Mapped[list["Monto"]] = relationship("Monto", back_populates="titulo")

    def __repr__(self) -> str:
        return (
            f"<Maestro("
            f"ID={self.id}, "
            f"ISIN={self.isin}, "
            f"EMISION={self.fecha_emision}, "
            f"VENCIMIENTO={self.fecha_vencimiento}, "
            f"CUPON={self.cupon}, "
            f"AMORTIZA={self.amortiza_id}, "
            f"SERIES_ID={self.serie_id}, "
            f"MONEDA_ID={self.moneda_id}, "
            f"TIPO_ID={self.tipo_id}, "
            f"BASE_ID={self.base_id}, "
            f"PERIODICIDAD_ID={self.periodicidad_id}, "
            f"MONTO_TOTAL_PROGRAMA={self.monto_total_programa}, "
            f"NEMOTECNICO={self.nemotecnico}, "
            f"OPTION_CALL={self.option_call}, "
            f"CALL_DATE={self.call_date}, "
            f"EMISOR_MONEDA_ID={self.emisor_moneda_id}, "
            f"METODO_CALCULO_ID={self.metodo_calculo_id}, "
            f"CALIFICACION_RIESGO={self.calificacion_riesgo}, "
            f"TIPO_TASA_ID={self.tipo_tasa}, "
            f"SOBRE_TASA={self.sobre_tasa}, "
            f"TIPO_EMISOR={self.tipo_emisor})>"
        )


class VectorMonto(Base):
    __tablename__ = "VECTOR_MONTO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column("ISIN_ID", Integer, ForeignKey(Maestro.id))
    fecha: Mapped[time | None] = mapped_column("FECHA", Date)
    monto_emitido: Mapped[float | None] = mapped_column("MONTO_EMITIDO", Float)
    moneda: Mapped[float | None] = mapped_column(
        "MONEDA_ID", Integer, ForeignKey(Moneda.id)
    )
    monto_circulante: Mapped[float | None] = mapped_column("MONTO_CIRCULANTE", Float)


class ContraccionExpansion(Base):
    __tablename__ = "CONTRACCION_EXPANSION"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    fecha_operacion: Mapped[time | None] = mapped_column("FECHA_DE_OPERACION", Date)
    dias_vencimiento: Mapped[int | None] = mapped_column("DIAS_AL_VENCIMIENTO", Integer)
    fecha_vencimiento: Mapped[time | None] = mapped_column("FECHA_DE_VENCIMIENTO", Date)
    monto_subastado: Mapped[float | None] = mapped_column("MONTO_SUBASTADO", Float)
    valor_nominal_ofertado: Mapped[float | None] = mapped_column(
        "VALOR_NOMINAL_OFERTADO", Float
    )
    precio_promedio_ponderado: Mapped[float | None] = mapped_column(
        "PRECIO_PROMEDIO_PONDERADO", Float
    )
    valor_nominal_ofertado_millones_rd: Mapped[float | None] = mapped_column(
        "VALOR_NOMINAL_OFERTADO_EN_MILLONES_DE_RD", Float
    )
    precio_corte: Mapped[float | None] = mapped_column("PRECIO_DE_CORTE", Float)
    precio_promedio_ponderado_adjudicado: Mapped[float | None] = mapped_column(
        "PRECIO_PROMEDIO_PONDERADO_ADJUDICADO", Float
    )
    tasa_rendimiento_promedio_ponderado: Mapped[float | None] = mapped_column(
        "TASA_DE_RENDIMIENTO_PROM_POND", Float
    )
    precio_promedio_ponderado_rechazado: Mapped[float | None] = mapped_column(
        "PRECIO_PROMEDIO_PONDERADO_RECHAZADO", Float
    )
    monto_rd_millones: Mapped[float | None] = mapped_column(
        "MONTO_EN_RD_MILLONES", Float
    )
    tasa_interes: Mapped[float | None] = mapped_column("TASA_DE_INTERES", Float)
    total_contraccion: Mapped[float | None] = mapped_column("TOTAL_CONTRACCION", Float)
    monto_colocacion: Mapped[float | None] = mapped_column(
        "MONTO_DE_COLOCACION_DIRECTA_EN_RD_MILLONES", Float
    )
    tasa_de_interes_colocacion_directa: Mapped[float | None] = mapped_column(
        "TASA_DE_INTERES_DE_COLOCACION_DIRECTA", Float
    )


class Monto(Base):
    __tablename__ = "MONTOS"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    fecha: Mapped[time | None] = mapped_column("FECHA", Date)
    monto_emitido: Mapped[float | None] = mapped_column("MONTO_EMITIDO", Float)
    monto_circulacion: Mapped[float | None] = mapped_column("MONTO_CIRCULACION", Float)
    isin_id: Mapped[int] = mapped_column("ISIN_ID", Integer, ForeignKey(Maestro.id))

    titulo: Mapped["Maestro"] = relationship(back_populates="montos")


class SubastaCredito(Base):
    __tablename__ = "SUBASTAS_CREDITO_PUBLICO"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column("ISIN_ID", Integer, ForeignKey(Maestro.id))
    fecha_subasta: Mapped[time | None] = mapped_column("FECHA_SUBASTA", Date)
    fecha_liquidacion: Mapped[time | None] = mapped_column("FECHA_LIQUIDACION", Date)
    monto_ofertado: Mapped[float | None] = mapped_column("MONTO_OFERTADO", Float)
    valor_nominal_recibido: Mapped[float | None] = mapped_column(
        "VALOR_NOMINAL_RECIBIDO", Float
    )
    precio_promedio_ponderado: Mapped[float | None] = mapped_column(
        "PRECIO_PROMEDIO_PONDERADO", Float
    )
    tasa_promedio_ponderada: Mapped[float | None] = mapped_column(
        "TASA_PROMEDIO_PONDERADA", Float
    )
    valor_nominal_adjudicada: Mapped[float | None] = mapped_column(
        "VALOR_NOMINAL_ADJUDICADA", Float
    )
    precio_adjudicacion: Mapped[float | None] = mapped_column(
        "PRECIO_DE_ADJUDICACION", Float
    )
    tasa_de_adjudicacion: Mapped[float | None] = mapped_column(
        "TASA_DE_ADJUDICACION", Float
    )
    valor_nominal_rechazado: Mapped[float | None] = mapped_column(
        "VALOR_NOMINAL_RECHAZADO", Float
    )
    precio_promedio_ponderado_rechazado: Mapped[float | None] = mapped_column(
        "PRECIO_PROMEDIO_PONDERADO_RECHAZADO", Float
    )
    tasa_promedio_ponderado_rechazado: Mapped[float | None] = mapped_column(
        "TASA_PROMEDIO_PONDERADO_RECHAZADO", Float
    )


class SubastaBCRD(Base):
    __tablename__ = "SUBASTAS_BCRD"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column("ISIN_ID", Integer, ForeignKey(Maestro.id))
    fecha_subasta: Mapped[time | None] = mapped_column("FECHA_SUBASTA", Date)
    valor_nominal_recibido: Mapped[float | None] = mapped_column(
        "VALOR_NOMINAL_RECIBIDO", Float
    )
    precio_de_oferta: Mapped[float | None] = mapped_column("PRECIO_DE_LA_OFERTA", Float)
    valor_nominal_adjudicada: Mapped[float | None] = mapped_column(
        "VALOR_NOMINAL_ADJUDICADA", Float
    )
    precio_de_corte: Mapped[Float | None] = mapped_column("PRECIO_DE_CORTE", Float)
    precio_promedio_ponderado: Mapped[float | None] = mapped_column(
        "PRECIO_PROMEDIO_PONDERADO", Float
    )
    precio_rechazado: Mapped[float | None] = mapped_column("PRECIO_RECHAZADO", Float)
    yield_promedio_ponderada_referencias_bcrd: Mapped[float | None] = mapped_column(
        "YIELD_PROMEDIO_PONDERADA_REFERENCIAS_BCRD", Float
    )
    dias_vencimiento: Mapped[int | None] = mapped_column("DIAS_VENCIMIENTO", Integer)


class VectorSubastasBCRD(Base):
    __tablename__ = "VECTOR_SUBASTAS_BCRD"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    subasta_id: Mapped[int] = mapped_column(
        "SUBASTA_ID", Integer, ForeignKey(SubastaBCRD.id)
    )
    isin_id: Mapped[int] = mapped_column("ISIN_ID", Integer, ForeignKey(Maestro.id))
    fecha_subasta: Mapped[time | None] = mapped_column("FECHA_SUBASTA", Date)
    valor_nominal_recibido: Mapped[float | None] = mapped_column(
        "VALOR_NOMINAL_RECIBIDO", Float
    )
    precio_de_oferta: Mapped[float | None] = mapped_column("PRECIO_DE_LA_OFERTA", Float)
    valor_nominal_adjudicada: Mapped[float | None] = mapped_column(
        "VALOR_NOMINAL_ADJUDICADA", Float
    )
    precio_de_corte: Mapped[Float | None] = mapped_column("PRECIO_DE_CORTE", Float)
    precio_promedio_ponderado: Mapped[float | None] = mapped_column(
        "PRECIO_PROMEDIO_PONDERADO", Float
    )
    precio_rechazado: Mapped[float | None] = mapped_column("PRECIO_RECHAZADO", Float)
    yield_promedio_ponderada_referencias_bcrd: Mapped[float | None] = mapped_column(
        "YIELD_PROMEDIO_PONDERADA_REFERENCIAS_BCRD", Float
    )
    yield_oferta: Mapped[float | None] = mapped_column("YIELD_OFERTA", Float)
    yield_corte: Mapped[float | None] = mapped_column("YIELD_CORTE", Float)
    yield_promedio_ponderada: Mapped[Float | None] = mapped_column(
        "YIELD_PROMEDIO_PONDERADA", Float
    )
    yield_promedio_ponderada_consolidada: Mapped[Float | None] = mapped_column(
        "YIELD_PROMEDIO_PONDERADA_CONSOLIDADA", Float
    )
    yield_rechazada: Mapped[Float | None] = mapped_column("YIELD_RECHAZADA", Float)
    bid_to_cover: Mapped[float | None] = mapped_column("BID_TO_COVER", Float)


class OperacionMM(Base):
    __tablename__ = "OPERACIONES_MARKETMAKERS"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    isin_id: Mapped[int] = mapped_column("ISIN_ID", Integer, ForeignKey(Maestro.id))
    fecha_valor: Mapped[time | None] = mapped_column("FECHA_VALOR", Date)
    cantidad_titulos: Mapped[int | None] = mapped_column("CANTIDAD_TITULOS", Integer)
    valor_transado: Mapped[float | None] = mapped_column("VALOR_TRANSDO", Float)
    dias_interes: Mapped[int | None] = mapped_column("DIAS_INTERES", Integer)
    monto_interes: Mapped[float | None] = mapped_column("MONTO_INTERES", Float)
    monto_limpio: Mapped[float | None] = mapped_column("MONTO_LIMPIO", Float)
    precio_limpio: Mapped[float | None] = mapped_column("PRECIO_LIMPIO", Float)
    rendimiento_vencimiento: Mapped[float | None] = mapped_column(
        "RENDIMIENTO_VENCIMIENTO"
    )


class OperacionesCevaldom(Base):
    __tablename__ = "OPERACIONES_CEVALDOM"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column("ID", Integer, primary_key=True, autoincrement=True)
    fisn: Mapped[str] = mapped_column("FISN", String(100))
    isin_id: Mapped[int] = mapped_column("ISIN_ID", Integer, ForeignKey(Maestro.id))
    monto_nominal_operacion: Mapped[int | None] = mapped_column(
        "MONTO_NOMINAL_OPERACION", BigInteger
    )
    moneda_id: Mapped[int | None] = mapped_column(
        "MONEDA_ID", Integer, ForeignKey(Moneda.id)
    )
    cantidad_valores: Mapped[int | None] = mapped_column("CANTIDAD_VALORES", BigInteger)
    _yield: Mapped[float | None] = mapped_column("YIELD", Float)
    precio_limpio: Mapped[float | None] = mapped_column("PRECIO_LIMPIO", Float)
    fecha_pacto: Mapped[time | None] = mapped_column("FECHA_PACTO", Date)
    hora_pacto: Mapped[time | None] = mapped_column("HORA_PACTO", Time)
    tipo_operacion: Mapped[int | None] = mapped_column(
        "TIPO_OPERACION_ID", Integer, ForeignKey(TipoOperacion.id)
    )
    parte: Mapped[int | None] = mapped_column(
        "PARTE_ID", Integer, ForeignKey("MARKET.PARTES.ID")
    )
    sistema_registro: Mapped[int | None] = mapped_column(
        "SISTEMA_REGISTRO_OTC_MERCADO_ID", Integer, ForeignKey(Sistema_Mercado.id)
    )
    fecha_liquidacion: Mapped[time | None] = mapped_column("FECHA_LIQUIDACION", Date)
    estados: Mapped[int | None] = mapped_column(
        "ESTADOS_ID", Integer, ForeignKey("MARKET.ESTADO.ID")
    )
    subida: Mapped[time] = mapped_column("SUBIDA", Date, server_default=func.now())
    grupo: Mapped[int | None] = mapped_column("GRUPO", BigInteger)
    vector_precio: Mapped["VectorPrecioOTC"] = relationship(back_populates="operacion")


class VectorPrecioOTC(Base):
    __tablename__ = "VECTOR_PRECIO_OTC"
    __table_args__ = ARGS

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    operacion_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OperacionesCevaldom.id)
    )
    facial_value: Mapped[float | None] = mapped_column(Float)
    traded_value: Mapped[float | None] = mapped_column(Float)
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
    duration_to_convexity: Mapped[float | None] = mapped_column(Float)

    operacion: Mapped[OperacionesCevaldom] = relationship(
        back_populates="vector_precio"
    )


class MaestroView(Base):
    __tablename__ = "MAESTRO_TITULO_CALC"
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

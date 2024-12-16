"""
QTech Schemas Library
--------------------
This module provides database schema definitions and utilities for the QTech platform.
"""

# Database connection utilities
from sqlalchemy import Engine, create_engine

# Yield models
from qtech_schemas._yield import (
    BenchmarkDerivative,
    BenchmarkFact,
    Curve,
    CurveBenchmark,
    CurveInput,
    CurveMethod,
    CurveMode,
    CurveType,
    DatoView,
    DerivativeFact,
    Parametro,
    Quote,
    SondeoEurobono,
    SondeoLocal,
    Titulo,
    TituloView,
    TypeDerivative,
    ValuationMethod,
    VectorPrecio,
)

# BVRD models
from qtech_schemas.bvrd import (
    CodigoRueda,
    CompraVenta,
    DescripcionInstrumento,
    EstatusOperacion,
    EstatusOrden,
    Flujos,
    MejorEjecucion,
    NombreMercado,
    OperacionesBVRD,
    OperacionesTotales,
    Rueda,
)

# DBO models
from qtech_schemas.dbo import (
    Cargas,
    Categoria,
    Datos,
    Extraccion,
    Fechas,
    Frecuencias,
    Fuentes,
    Metodo_Extraccion,
    Moneda,
    Transformacion,
    Variables,
)

# Market models
from qtech_schemas.market import (
    Amortiza,
    Base,
    BasePago,
    ContraccionExpansion,
    Emisor,
    EmisorMoneda,
    Estado,
    Maestro,
    Mercado,
    MetodoCalculo,
    OperacionesCevaldom,
    OperacionMM,
    Parte,
    Periodicidad,
    Ranking,
    Sector,
    SerieEmision,
    Sistema_Mercado,
    SubastaBCRD,
    SubastaCredito,
    TipoEmisor,
    TipoInstrumento,
    TipoOperacion,
    TipoTasa,
)

# SIMBAD models
from qtech_schemas.simbad import (
    CAPTACIONES,
    COMPONENTE,
    CONTRAPARTE,
    DIVISA,
    ENTIDAD,
    FINANCIERO_NOFINANCIERO,
    GENERO,
    INSTRUMENTO_CAPTACION,
    INSTRUMENTO_MEDIO,
    PARTIDA_NIVEL_1,
    PARTIDA_NIVEL_2,
    PERSONA,
    PROVINCIA,
    PUBLICO_PRIVADO_1,
    PUBLICO_PRIVADO_2,
    REGION,
    RESIDENTE_NORESIDENTE,
    SITUACION_NIVEL1,
    SITUACION_NIVEL2,
    TIPO_CLIENTE,
    TIPO_ENTIDAD,
)
from qtech_schemas.simbad import MONEDA as SIMBAD_MONEDA  # Renamed to avoid conflict


def conectar_db(
    server: str, database: str, username: str, password: str, driver: str
) -> Engine:
    """
    Create a SQLAlchemy engine connection to the database.

    Args:
        server (str): Database server address
        database (str): Database name
        username (str): Database username
        password (str): Database password
        driver (str): ODBC driver to use

    Returns:
        Engine: SQLAlchemy engine instance
    """
    connection_string = (
        f"mssql+pyodbc://{username}:{password}" f"@{server}/{database}?driver={driver}"
    )
    return create_engine(connection_string, pool_pre_ping=True)


# Define public API
__all__ = [
    # Connection utility
    "conectar_db",
    # Base classes
    "Base",
    # Market models
    "Amortiza",
    "Sector",
    "Emisor",
    "SerieEmision",
    "Moneda",
    "TipoInstrumento",
    "BasePago",
    "Periodicidad",
    "EmisorMoneda",
    "MetodoCalculo",
    "Maestro",
    "SubastaCredito",
    "SubastaBCRD",
    "OperacionMM",
    "TipoOperacion",
    "Parte",
    "Estado",
    "OperacionesCevaldom",
    "Sistema_Mercado",
    "TipoTasa",
    "TipoEmisor",
    "Ranking",
    "Mercado",
    "ContraccionExpansion",
    # BVRD models
    "CodigoRueda",
    "CompraVenta",
    "DescripcionInstrumento",
    "EstatusOperacion",
    "EstatusOrden",
    "Rueda",
    "NombreMercado",
    "MejorEjecucion",
    "OperacionesBVRD",
    "OperacionesTotales",
    "Flujos",
    # Yield models
    "Titulo",
    "EmisorMoneda",
    "CurveInput",
    "CurveType",
    "CurveMethod",
    "CurveMode",
    "Quote",
    "Curve",
    "SondeoLocal",
    "SondeoEurobono",
    "Parametro",
    "ValuationMethod",
    "VectorPrecio",
    "CurveBenchmark",
    "BenchmarkFact",
    "TypeDerivative",
    "BenchmarkDerivative",
    "DerivativeFact",
    "TituloView",
    "DatoView",
    # DBO models
    "Frecuencias",
    "Categoria",
    "Fuentes",
    "Moneda",
    "Metodo_Extraccion",
    "Transformacion",
    "Extraccion",
    "Cargas",
    "Variables",
    "Fechas",
    "Datos",
    # SIMBAD models
    "TIPO_ENTIDAD",
    "ENTIDAD",
    "REGION",
    "PROVINCIA",
    "PERSONA",
    "GENERO",
    "TIPO_CLIENTE",
    "INSTRUMENTO_CAPTACION",
    "SIMBAD_MONEDA",
    "DIVISA",
    "PARTIDA_NIVEL_1",
    "PARTIDA_NIVEL_2",
    "PUBLICO_PRIVADO_1",
    "PUBLICO_PRIVADO_2",
    "RESIDENTE_NORESIDENTE",
    "COMPONENTE",
    "INSTRUMENTO_MEDIO",
    "CONTRAPARTE",
    "SITUACION_NIVEL1",
    "SITUACION_NIVEL2",
    "FINANCIERO_NOFINANCIERO",
    "CAPTACIONES",
]

# Version information
__version__ = "2.12.1"

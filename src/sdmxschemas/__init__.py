"""Accessors to SDMX schemas."""
from pathlib import Path

# SDMX-JSON 1.0 schemas

SDMX_JSON_10_BASE_PATH: Path = Path(__file__).parent / "json" / "sdmx10"
SDMX_JSON_10_DATA_PATH: Path = SDMX_JSON_10_BASE_PATH / "sdmx-json-data-schema.json"
SDMX_JSON_10_STRUCTURE_PATH: Path = SDMX_JSON_10_BASE_PATH / "sdmx-json-structure-schema.json"
SDMX_JSON_10_METADATA_PATH: Path = SDMX_JSON_10_BASE_PATH / "sdmx-json-metadata-schema.json"

# SDMX-JSON 2.0 schemas

SDMX_JSON_20_BASE_PATH: Path = Path(__file__).parent / "json" / "sdmx20"
SDMX_JSON_20_DATA_PATH: Path = SDMX_JSON_20_BASE_PATH / "sdmx-json-data-schema.json"
SDMX_JSON_20_STRUCTURE_PATH: Path = SDMX_JSON_20_BASE_PATH / "sdmx-json-structure-schema.json"
SDMX_JSON_20_METADATA_PATH: Path = SDMX_JSON_20_BASE_PATH / "sdmx-json-metadata-schema.json"

# SDMX-ML 1.0 schemas

SDMX_ML_10_BASE_PATH: Path = Path(__file__).parent / "xml" / "sdmx10"
SDMX_ML_10_MESSAGE_PATH: Path = SDMX_ML_10_BASE_PATH / "SDMXMessage.xsd"

# SDMX-ML 2.0 schemas

SDMX_ML_20_BASE_PATH: Path = Path(__file__).parent / "xml" / "sdmx20"
SDMX_ML_20_MESSAGE_PATH: Path = SDMX_ML_20_BASE_PATH / "SDMXMessage.xsd"

# SDMX-ML 2.1 schemas
SDMX_ML_21_BASE_PATH: Path = Path(__file__).parent / "xml" / "sdmx21"
SDMX_ML_21_MESSAGE_PATH: Path = SDMX_ML_21_BASE_PATH / "SDMXMessage.xsd"

# SDMX-ML 3.0 schemas
SDMX_ML_30_BASE_PATH: Path = Path(__file__).parent / "xml" / "sdmx30"
SDMX_ML_30_MESSAGE_PATH: Path = SDMX_ML_30_BASE_PATH / "SDMXMessage.xsd"

# SDMX-ML 3.1 schemas
SDMX_ML_31_BASE_PATH: Path = Path(__file__).parent / "xml" / "sdmx31"
SDMX_ML_31_MESSAGE_PATH: Path = SDMX_ML_31_BASE_PATH / "SDMXMessage.xsd"

__version__ = "1.0.0"

from src.sdmxschemas import SDMX_JSON_10_DATA_PATH, SDMX_JSON_10_METADATA_PATH, SDMX_JSON_10_STRUCTURE_PATH, SDMX_JSON_20_DATA_PATH, \
    SDMX_JSON_20_METADATA_PATH, SDMX_JSON_20_STRUCTURE_PATH, SDMX_ML_10_MESSAGE_PATH, SDMX_ML_20_MESSAGE_PATH, SDMX_ML_21_MESSAGE_PATH, \
    SDMX_ML_30_MESSAGE_PATH


def test_reading_sdmx_json_10():
    assert SDMX_JSON_10_DATA_PATH.exists()
    assert SDMX_JSON_10_STRUCTURE_PATH.exists()
    assert SDMX_JSON_10_METADATA_PATH.exists()


def test_reading_sdmx_json_20():
    assert SDMX_JSON_20_DATA_PATH.exists()
    assert SDMX_JSON_20_STRUCTURE_PATH.exists()
    assert SDMX_JSON_20_METADATA_PATH.exists()


def test_reading_sdmx_ml_10():
    assert SDMX_ML_10_MESSAGE_PATH.exists()


def test_reading_sdmx_ml_20():
    assert SDMX_ML_20_MESSAGE_PATH.exists()


def test_reading_sdmx_ml_21():
    assert SDMX_ML_21_MESSAGE_PATH.exists()


def test_reading_sdmx_ml_30():
    assert SDMX_ML_30_MESSAGE_PATH.exists()

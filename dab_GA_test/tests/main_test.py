from unittest.mock import patch, MagicMock
from dab_GA_test.main import get_taxis, get_spark

@patch("databricks.connect.DatabricksSession")
def test_main(mock_session_cls):
    mock_spark = MagicMock()
    mock_session_cls.builder.getOrCreate.return_value = mock_spark

    # Fake return value for get_taxis()
    mock_result = MagicMock()
    mock_spark.some_spark_method.return_value = mock_result  # update if needed

    result = get_taxis(mock_spark)
    assert result is not None

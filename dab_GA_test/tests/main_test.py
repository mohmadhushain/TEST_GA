from unittest.mock import patch
from dab_GA_test.main import get_taxis

@patch("dab_GA_test.main.DatabricksSession")
def test_main(mock_session):
    mock_spark = mock_session.builder.getOrCreate.return_value
    # Configure fake data on mock_spark if needed
    taxis = get_taxis(mock_spark)
    assert taxis is not None

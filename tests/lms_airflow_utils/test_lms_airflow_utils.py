import sys
import lms_airflow_utils


def test_ping():
    sys.argv = ['foo', '10']
    lms_airflow_utils.ping()


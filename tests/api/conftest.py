import pytest

from utilities import Log

@pytest.fixture(scope = "class")
def setupApi(request):
    log = Log.log()
    request.cls.log = log
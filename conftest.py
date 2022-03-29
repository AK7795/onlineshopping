import pytest
@pytest.fixture(scope="session",autouse=True)

def setUp():
    print("open amazon")
    print('logged in')
    yield
    print("logged out")
    print("closed amazon")

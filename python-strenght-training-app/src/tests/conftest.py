from tests.initialize_test_database import initialize_test_database

def pytest_configure():
    initialize_test_database()
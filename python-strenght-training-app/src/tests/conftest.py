from initialize_test_database import initialize_database

def pytest_configure():
    initialize_database()
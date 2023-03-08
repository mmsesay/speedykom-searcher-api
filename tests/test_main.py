import os
import tempfile

import pytest

from app import src


@pytest.fixture
def client():
    db_fd, src.config['DATABASE'] = 'sqlite:///users.db' # tempfile.mkstemp()
    src.config['TESTING'] = True

    with src.test_client() as client:
        with src.app_context():
            src.init_db()
        yield client

    os.close(db_fd)
    os.unlink(src.config['DATABASE'])

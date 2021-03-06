from __future__ import absolute_import, unicode_literals

import pytest

pytest_plugins = [
    'tests.fixtures'
]


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    from wagtail.core.models import Page, Site

    with django_db_blocker.unblock():
        # Remove some initial data that is brought by the tests.site module
        Site.objects.all().delete()
        Page.objects.all().exclude(depth=1).delete()

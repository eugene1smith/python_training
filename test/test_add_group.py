# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.group import group



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="Name", header="Head", footer="Footer"))

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="", header="", footer=""))
    app.session.logout()

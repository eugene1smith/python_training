# -*- coding: utf-8 -*-
from application import Application
import pytest
from group import group



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(group(name="Name", header="Head", footer="Footer"))

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(group(name="", header="", footer=""))
    app.logout()

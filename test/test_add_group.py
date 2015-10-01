# -*- coding: utf-8 -*-

from model.group import group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="Name", header="Head", footer="Footer"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="", header="", footer=""))
    app.session.logout()

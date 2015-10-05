# -*- coding: utf-8 -*-

from model.group import group


def test_add_group(app):
    app.group.create(group(name="Name", header="Head", footer="Footer"))

def test_add_empty_group(app):
    app.group.create(group(name="", header="", footer=""))

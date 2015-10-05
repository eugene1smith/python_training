__author__ = 'Eugene'

from model.group import group


def test_big_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(group(name="Groups name for modify"))
    app.group.modify_first_group(group(name="New Name"))

def test_big_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(group(header="Groups header for modify"))
    app.group.modify_first_group(group(header="New Header"))
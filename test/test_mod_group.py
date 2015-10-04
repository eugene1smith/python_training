__author__ = 'Eugene'

from model.group import group


def test_big_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(group(name="New Name",footer='',header=''))
    app.session.logout()
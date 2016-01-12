__author__ = 'Eugene'

from model.group import Group


def test_big_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Groups name for modify"))
    old_groups = app.group.get_group_list()
    group = Group(name="New Name")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_big_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="Groups header for modify"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New Header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
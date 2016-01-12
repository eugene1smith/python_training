__author__ = 'Eugene'


from model.contact import Contact
from random import randrange

def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="Eugene", last_name="Kuznetsov", nickname="eugene_smith",
                                    title="LLC", company_name="Lazada", address="Moscow, Presnenskaya, 10",
                                    home="84951112233", mobile="89001112233", work="80001122333", fax="88003332211",
                                    first="eugene.kuznetsov@lazada.com", second="second@lazada.com", third="third@lazada.com",
                                    homepage="www.homepage.com", birth_year="1980", an_year="1990",
                                    second_address="Second address", home_address="My home address",
                                    notes="Some note for this test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Max", last_name="Green", nickname="eugene_smith",
                                    title="LLC", company_name="Lazada", address="Moscow, Presnenskaya, 10",
                                    home="84951112233", mobile="89001112233", work="80001122333", fax="88003332211",
                                    first="eugene.kuznetsov@lazada.com", second="second@lazada.com", third="third@lazada.com",
                                    homepage="www.homepage.com", birth_year="1999", an_year="1907",
                                    second_address="Second address", home_address="My home address",
                                    notes="Another note for this test")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

__author__ = 'Eugene'


from model.contact import Contact


def test_mod_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(first_name="Max", last_name="Green", nickname="eugene_smith",
                                    title="LLC", company_name="Lazada", address="Moscow, Presnenskaya, 10",
                                    home="84951112233", mobile="89001112233", work="80001122333", fax="88003332211",
                                    first="eugene.kuznetsov@lazada.com", second="second@lazada.com", third="third@lazada.com",
                                    homepage="www.homepage.com", birth_year="1999", an_year="1907",
                                    second_address="Second address", home_address="My home address",
                                    notes="Another note for this test"))
    app.session.logout()
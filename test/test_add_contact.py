from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(first_name="Eugene", last_name="Kuznetsov", nickname="eugene_smith",
                                    title="LLC", company_name="Lazada", address="Moscow, Presnenskaya, 10",
                                    home="84951112233", mobile="89001112233", work="80001122333", fax="88003332211",
                                    first="eugene.kuznetsov@lazada.com", second="second@lazada.com", third="third@lazada.com",
                                    homepage="www.homepage.com", birth_year="1980", an_year="1990",
                                    second_address="Second address", home_address="My home address",
                                    notes="Some note for this test"))
    app.session.logout()


from model.contact import Contact


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testname"))
    app.contact.edit_first_contact(Contact(firstname="First1"))


def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testname"))
    app.contact.edit_first_contact(Contact(lastname="Last1"))


def test_edit_contact_birthmonth(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testname"))
    app.contact.edit_first_contact(Contact(bmonth="February"))

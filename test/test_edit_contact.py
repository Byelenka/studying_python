from model.contact import Contact


def test_edit_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="First1"))


def test_edit_contact_lastname(app):
    app.contact.edit_first_contact(Contact(lastname="Last1"))


def test_edit_contact_birthmonth(app):
    app.contact.edit_first_contact(Contact(bmonth="February"))

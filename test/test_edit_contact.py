from random import randrange

from model.contact import Contact


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testname", lastname="testlastname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="First1", lastname="Lastname1")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_contact_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="testname"))
#     app.contact.edit_first_contact(Contact(lastname="Last1"))
#
#
# def test_edit_contact_birthmonth(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="testname"))
#     app.contact.edit_first_contact(Contact(bmonth="February"))

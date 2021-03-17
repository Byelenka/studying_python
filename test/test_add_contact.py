# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname",
                               title="Title", company="Company", address="address", home_phone="123", mobile_phone="222",
                               work_phone="333", fax="444", email="1@test.com", email2="2@test.com", email3="3@test.com",
                               homepage="google.com", bday="1", bmonth="January", byear="1999",
                               address2="secondary address", phone2="456", notes="some text")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home_phone="", mobile_phone="",
                               work_phone="", fax="", email="", email2="", email3="",
                               homepage="", bday="", bmonth="-", byear="",
                               address2="", phone2="", notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


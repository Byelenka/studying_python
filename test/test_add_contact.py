# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname",
                               title="Title", company="Company", address="address", home_phone="123", mobile_phone="222",
                               work_phone="333", fax="444", email="1@test.com", email2="2@test.com", email3="3@test.com",
                               homepage="google.com", bday="1", bmonth="January", byear="1999",
                               address2="secondary address", phone2="456", notes="some text"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home_phone="", mobile_phone="",
                               work_phone="", fax="", email="", email2="", email3="",
                               homepage="", bday="", bmonth="-", byear="",
                               address2="", phone2="", notes=""))
    app.session.logout()


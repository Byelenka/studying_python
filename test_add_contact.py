# -*- coding: utf-8 -*-
from contact import Contact
from application_contact import ApplicationContact
import pytest


@pytest.fixture
def app_con(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app_con):
    app_con.login(username="admin", password="secret")
    app_con.create_contact(Contact(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname",
                            title="Title", company="Company", address="address", home_phone="123", mobile_phone="222",
                            work_phone="333", fax="444", email="1@test.com", email2="2@test.com", email3="3@test.com",
                            homepage="google.com", bday="1", bmonth="January", byear="1999",
                            address2="secondary address", phone2="456", notes="some text"))
    app_con.logout()


def test_add_empty_contact(app_con):
    app_con.login(username="admin", password="secret")
    app_con.create_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                            title="", company="", address="", home_phone="", mobile_phone="",
                            work_phone="", fax="", email="", email2="", email3="",
                            homepage="", bday="", bmonth="-", byear="",
                            address2="", phone2="", notes=""))
    app_con.logout()


from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="First1", middlename="Middle1", lastname="Last1", nickname="Nickname1",
                               title="Title1", company="Company1", address="address", home_phone="123",
                               mobile_phone="222",
                               work_phone="333", fax="444", email="1@test.com", email2="2@test.com",
                               email3="3@test.com",
                               homepage="google.com", bday="2", bmonth="February", byear="1998",
                               address2="secondary address", phone2="456", notes="some text1"))

from author import Author

author = Author("Tan Ah Teck","ahTeck@somewhere.com","m")

def test_author():
    expected = "Author[name=Tan Ah Teck,email=ahTeck@somewhere.com,gender=m]"
    actual = author.toString()
    assert expected == actual
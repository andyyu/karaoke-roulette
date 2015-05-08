from opentok import OpenTok

opentok = OpenTok(45228402, cc334f55939e584275f9c3ba975114c4635953ec)

session = opentok.create_session()

token = session.generate_token()
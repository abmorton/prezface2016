from app import app, db
from models import Candidate

# Create the db if needed.

db.create_all()

# This is a helper script to populate our databases with info
 # about the candidates.

hillaryclinton = Candidate('Hillary', 'Clinton', 'New York', 'Democratic Party', 'hillaryclinton.com', 'http://www.facebook.com/hillaryclinton', 'HillaryClinton')
martinomalley = Candidate("Martin", "O'Malley", "Maryland", "Democratic Party", "martinomalley.com", "http://www.facebook.com/MartinOMalley", "MartinOMalley")
berniesanders = Candidate("Bernie", "Sanders", "Vermont", "Democratic Party", "berniesanders.com", "http://www.facebook.com/berniesanders", "SenSanders")
jebbush = Candidate("Jeb", "Bush", "Florida", "Republican Party", "jeb2016.com", "http://www.facebook.com/jebbush", "JebBush")
bencarson = Candidate("Ben", "Carson", "Florida", "Republican Party", "bencarson.com", "http://www.facebook.com/DrBenjaminCarson", "RealBenCarson")
chrischristie = Candidate("Chris", "Christie", "New Jersey", "Republican Party", "ChrisChristie.com", "http://www.facebook.com/GovChrisChristie", "GovChristie")
tedcruz = Candidate("Ted", "Cruz", "Texas", "Republican Party", "TedCruz.org", "http://www.facebook.com/TedCruzPage", "TedCruz")
carlyfiorina = Candidate("Carly", "Fiorina", "Virginia", "Republican Party", "CarlyForPresident.com", "http://www.facebook.com/CarlyFiorina", "CarlyFiorina")
jimgilmore = Candidate("Jim", "Gilmore", "Virginia", "Republican Party", "GilmoreForAmerica.com", "http://www.facebook.com/JimGilmore", "Gov_Gilmore")
lindseygraham = Candidate("Lindsey", "Graham", "South Carolina", "Republican Party", "LindseyGraham.com", "http://www.facebook.com/LindseGrahamSC", "LindseyGrahamSC")
mikehuckabee = Candidate("Mike", "Huckabee", "Florida", "Republican Party", "MikeHuckabee.com", "http://www.facebook.com/MikeHuckabee", "GovMikeHuckabee")
bobbyjindal = Candidate("Bobby", "Jindal", "Louisiana", "Republican Party", "BobbyJindal.com", "http://www.facebook.com/BobbyJindal", "BobbyJindal")
johnkasich = Candidate("John", "Kasich", "Ohio", "Republican Party", "JohnKasich.com", "http://www.facebook.com/JohnRKasich", "JohnKasich")
georgepataki = Candidate("George", "Pataki", "New York", "Republican Party", "GeorgePataki.com", "http://www.facebook.com/GovGeorgePataki", "GovernorPataki")
randpaul = Candidate("Rand", "Paul", "Kentucky", "Republican Party", "RandPaul.com", "http://www.facebook.com/RandPaul", "RandPaul")
marcorubio = Candidate("Marco", "Rubio", "Florida", "Republican Party", "MarcoRubio.com", "http://www.facebook.com/MarcoRubio", "MarcoRubio")
ricksantorum = Candidate("Rick", "Santorum", "Pennsylvania", "Republican Party", "RickSantorum.com", "http://www.facebook.com/RickSantorum", "RickSantorum")
donaldtrump = Candidate("Donald", "Trump", "New York", "Republican Party", "DonaldJTrump.com", "http://www.facebook.com/DonaldTrump", "RealDonaldTrump")

# Add them into the db session
db.session.add(hillaryclinton)
db.session.add(martinomalley)
db.session.add(berniesanders)
db.session.add(jebbush)
db.session.add(bencarson)
db.session.add(chrischristie)
db.session.add(tedcruz)
db.session.add(carlyfiorina)
db.session.add(jimgilmore)
db.session.add(lindseygraham)
db.session.add(mikehuckabee)
db.session.add(bobbyjindal)
db.session.add(johnkasich)
db.session.add(georgepataki)
db.session.add(randpaul)
db.session.add(marcorubio)
db.session.add(ricksantorum)
db.session.add(donaldtrump)

db.session.commit()


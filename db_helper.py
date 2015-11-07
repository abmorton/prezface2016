from app import app, db
from models import Candidate

# Create the db if needed.

# db.create_all()

# This is a helper script to populate our databases with info
 # about the candidates.

hillaryclinton = Candidate('Hillary Clinton', 'New York', 'Democratic Party', 'http://hillaryclinton.com', 'http://www.facebook.com/hillaryclinton', 'http://twitter.com/hillaryclinton')
martinomalley = Candidate("Martin O'Malley", "Maryland", "Democratic Party", "http://www.martinomalley.com/", "http://www.facebook.com/MartinOMalley", "http://twitter.com/GovernorOMalley")
berniesanders = Candidate("Bernie Sanders", "Vermont", "Democratic Party", "http://www.berniesanders.com/", "http://www.facebook.com/berniesanders", "http://twitter.com/SenSanders")

jebbush = Candidate("Jeb Bush", "Florida", "Republican Party", "http://jeb2016.com/", "http://www.facebook.com/jebbush", "http://twitter.com/JebBush")
bencarson = Candidate("Ben Carson", "Florida", "Republican Party", "http://bencarson.com/", "http://www.facebook.com/DrBenjaminCarson", "http://twitter.com/RealBenCarson")
chrischristie = Candidate("Chris Christie", "New Jersey", "Republican Party", "http://ChrisChristie.com", "http://www.facebook.com/GovChrisChristie", "http://twitter.com/GovChristie")
tedcruz = Candidate("Ted Cruz", "Texas", "Republican Party", "http://TedCruz.org", "http://www.facebook.com/TedCruzPage", "http://twitter.com/TedCruz")
carlyfiorina = Candidate("Carly Fiorina", "Virginia", "Republican Party", "http://CarlyForPresident.com", "http://www.facebook.com/CarlyFiorina", "http://twitter.com/CarlyFiorina")
jimgilmore = Candidate("Jim Gilmore", "Virginia", "Republican Party", "http://GilmoreForAmerica.com", "http://www.facebook.com/JimGilmore", "http://twitter.com/GovernorGilmore")
lindseygraham = Candidate("Lindsey Graham", "South Carolina", "Republican Party", "http://LindseyGraham.com", "http://www.facebook.com/LindseGrahamSC", "http://twitter.com/LindseyGrahamSC")
mikehuckabee = Candidate("Mike Huckabee", "Florida", "Republican Party", "http://MikeHuckabee.com", "http://www.facebook.com/MikeHuckabee", "http://twitter.com/GovMikeHuckabee")
bobbyjindal = Candidate("Bobby Jindal", "Louisiana", "Republican Party", "http://BobbyJindal.com", "http://www.facebook.com/BobbyJindal", "http://twitter.com/BobbyJindal")
johnkasich = Candidate("John Kasich", "Ohio", "Republican Party", "http://JohnKasich.com", "http://www.facebook.com/JohnRKasich", "http://twitter.com/JohnRKasich")
georgepataki = Candidate("George Pataki", "New York", "Republican Party", "http://GeorgePataki.com", "http://www.facebook.com/GovGeorgePataki", "http://twitter.com/GovernorPataki")
randpaul = Candidate("Rand Paul", "Kentucky", "Republican Party", "http://RandPaul.com", "http://www.facebook.com/RandPaul", "http://twitter.com/RandPaul")
marcorubio = Candidate("Marco Rubio", "Florida", "Republican Party", "http://MarcoRubio.com", "http://www.facebook.com/MarcoRubio", "http://twitter.com/MarcoRubio")
ricksantorum = Candidate("Rick Santorum", "Pennsylvania", "Republican Party", "http://RickSantorum.com", "http://www.facebook.com/RickSantorum", "http://twitter.com/RickSantorum")
donaldtrump = Candidate("Donald Trump", "New York", "Republican Party", "http://DonaldJTrump.com", "http://www.facebook.com/DonaldTrump", "http://twitter.com/RealDonaldTrump")

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


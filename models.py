from app import db

class Candidate(db.Model):
	__tablename__ = 'candidates'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String, nullable=False, unique=True)
	last_name = db.Column(db.String, nullable=False, unique=True)
	state = db.Column(db.String)
	party = db.Column(db.String)
	campaign_site = db.Column(db.String, unique=True)
	government_site = db.Column(db.String, unique=True)
	facebook_site = db.Column(db.String, unique=True)
	twitter_name = db.Column(db.String, unique=True)
	# photo = 
	# word_cloud = 

	def __init__(self, first_name, last_name, state, party, campaign_site, facebook_site, twitter_name):
		self.first_name = first_name
		self.last_name = last_name
		self.state = state
		self.party = party
		self.campaign_site = campaign_site
		self.facebook_site = facebook_site
		self.twitter_name = twitter_name

	def __repr__(self):
		return 'id: {}, last_name: {}, state: {}, party: {}'.format(self.id, self.last_name, self.state, self.party)

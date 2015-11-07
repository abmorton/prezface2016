from app import db

class Candidate(db.Model):
	__tablename__ = 'candidates'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False, unique=True)
	state = db.Column(db.String)
	party = db.Column(db.String)
	campaign_site = db.Column(db.String, unique=True)
	government_site = db.Column(db.String, unique=True)
	facebook_site = db.Column(db.String, unique=True)
	twitter_site = db.Column(db.String, unique=True)
	# photo = 
	# word_cloud = 

	def __init__(self, name, state, party, campaign_site, facebook_site, twitter_site):
		self.name = name
		self.state = state
		self.party = party
		self.campaign_site = campaign_site
		self.facebook_site = facebook_site
		self.twitter_site = twitter_site

	def __repr__(self):
		return 'id: {}, name: {}, state: {}, party: {}'.format(self.id, self.name, self.state, self.party)

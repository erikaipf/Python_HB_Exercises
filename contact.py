class Contact(object):
	def __init__(self, first_name, last_name, mobile_phone = "", work_phone = "", email ="", twitter_handle =""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile_phone = mobile_phone
		self.email = email
		self.twitter_handle = twitter_handle
		self.work_phone = work_phone
	
	def change_first_name(self,first_name):
		self.first_name = first_name

	def change_last_name(self,last_name):
		self.last_name = last_name

	def change_mobile_phone(self,mobile_phone):
		self.mobile_phone = mobile_phone

	def change_work_phone(self,work_phone):
		self.work_phone = work_phone	

	def change_email(self, email):
		self.email = email

	def change_twitter_handle(self, twitter_handle):
		self.twitter_handle = twitter_handle

	def display_contact(self):
		'''Print the contact information'''
		# print """
		# 	    First Name     : %s
		# 	    Last Name      : %s
		# 	    Mobile Phone   : %s
		# 	    Work Phone     : %s
		# 	    Email          : %s
		# 	    Twitter Handle : %s
		# 	  """ % (self.first_name, self.last_name, self.mobile_phone, self.work_phone, self.email, self.twitter_handle)
		# OR
		print "\nFirst Name     :", self.first_name.title()
		print "Last Name      :", self.last_name.title()
		print "Mobile Phone   :", self.mobile_phone
		print "Work Phone     :", self.work_phone
		print "Email          :", self.email
		print "Twitter Handle :", self.twitter_handle

	def send_email(self, email_from, email_subject, email_message):
		'''Send email to contact'''
		if self.email == "":
			print "Please add the Contact Email first."
		elif email_from.strip(' ') == "":
			print "The Email Origin is blank.  Please try again."
		elif email_subject.strip(' ') == "":
			print "The Email Subject is blank.  Please try again."
		elif email_message.strip(' ') == "":
			print "The Email Message is blank.  Please try again."
		else:
			print """
			         Email Message
					 From   : %s
					 To     : %s
					 Subject: %s
					 Message:
					 %s
				  """ % (email_from, self.email, email_subject, message)

	def send_twitter(self, twitter_from, twitter_message):
		'''Send a Twiiter message to contact'''
		if self.twitter_handle == "":
			print "Please add the Contact Twitter Handle first and try again."
		elif twitter_from.strip(' ') == "":
			print "The Twitter Handle Origin is blank.  Please try again."
		elif twitter_message == "":
			print "The Twiiter Message is blank.  Please try again."
		else:
			print """
			         Twitter Message
			         From    : %s
			         To      : %s
			         Message : %s
			      """ % (twitter_from, self.twitter_handle, twitter_message)
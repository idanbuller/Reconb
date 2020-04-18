#!/usr/bin/env python3
import re
import smtplib
import dns.resolver

# Address used for SMTP MAIL FROM command

class Verify():

	def __init__(self, address):
		self.fromAddress = address

	def check(self):
		# Simple Regex for syntax checking
		regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

		# Email address to verify
		inputAddress = self.fromAddress
		addressToVerify = str(inputAddress)

		# Syntax check
		match = re.match(regex, addressToVerify)
		if match == None:
			print('Bad Syntax')
			raise ValueError('Bad Syntax')

		# Get domain for DNS lookup
		splitAddress = addressToVerify.split('@')
		domain = str(splitAddress[1])
		# print('Domain:', domain)

		# MX record lookup
		records = dns.resolver.query(domain, 'MX')
		mxRecord = records[0].exchange
		mxRecord = str(mxRecord)


		# SMTP lib setup (use debug level for full output)
		server = smtplib.SMTP()
		server.set_debuglevel(0)

		# SMTP Conversation
		try:
			server.connect(mxRecord)
		except TimeoutError as e:
			print(f"Email not verifiied")
		server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
		server.mail(self.fromAddress)
		code, message = server.rcpt(str(addressToVerify))
		server.quit()

		#print(code)
		#print(message)

		# Assume SMTP response 250 is success
		if code == 250:
			return True
		else:
			return False
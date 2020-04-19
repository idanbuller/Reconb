#!/usr/bin/env python3
import re
import smtplib
import dns.resolver


class Verify():

	def __init__(self, address):
		self.fromAddress = address

	def check(self):

		regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'


		inputAddress = self.fromAddress
		addressToVerify = str(inputAddress)


		match = re.match(regex, addressToVerify)
		if match == None:
			print('Bad Syntax')
			raise ValueError('Bad Syntax')


		splitAddress = addressToVerify.split('@')
		domain = str(splitAddress[1])
		# print('Domain:', domain)

		records = dns.resolver.query(domain, 'MX')
		mxRecord = records[0].exchange
		mxRecord = str(mxRecord)

		server = smtplib.SMTP()
		server.set_debuglevel(0)


		try:
			server.connect(mxRecord)
		except TimeoutError as e:
			print(f"Email not verifiied")
		server.helo(server.local_hostname) 
		server.mail(self.fromAddress)
		code, message = server.rcpt(str(addressToVerify))
		server.quit()

		if code == 250:
			return True
		else:
			return False

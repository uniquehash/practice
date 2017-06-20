
from __future__ import unicode_literals

from imapclient import IMAPClient
import imapclient
from backports import ssl

import os
import pprint
import email
from email.parser import Parser

pp = pprint.PrettyPrinter(indent=4)
ENV = os.environ

HOST = ENV['MAIL_A']
USERNAME = ENV['MAIL_U']
PASSWORD = ENV['MAIL_P']
ssl_bool = True
port = 993
ssl_verify_cert = False

context = imapclient.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

server = IMAPClient(HOST, use_uid=True, ssl=ssl_bool, port=port, ssl_context=context)
server.login(USERNAME, PASSWORD)

print "retreiving info..."

folder = "dorms"


select_info = server.select_folder(folder)
print('{0} messages in {1}'.format(select_info['EXISTS'], folder))

messages = server.search(['NOT', 'DELETED', 'NOT', 'Answered'])
print("%d messages that aren't deleted" % len(messages))


##
##	usefull SO link i guess for getting the body
##	https://stackoverflow.com/questions/24075732/read-body-of-email-using-imapclient-in-python
##

# print("data")
# response = server.fetch(messages, ['RFC822', 'BODY[TEXT]', 'ENVELOPE'])
# for msgid, data in response.iteritems():	
# 	parsedEmail = email.message_from_string(data['RFC822'])
# 	body = email.message_from_string(data['BODY[TEXT]'])
# 	parsedBody = parsedEmail.get_payload(0)	
# 	print "id: {0}".format(msgid)
# 	print "subject: {0}".format(data['ENVELOPE'][1])
# 	print ""
# 	print parsedBody
# 	print ""
# 	print "end of message"
# 	print "<------------------------------------------------------------->"
# 	print ""
# 	print ""
# 	print ""


print("data")
response = server.fetch(messages, ['RFC822', 'ENVELOPE', 'BODY[TEXT]'])
for msgid, data in response.iteritems():		
	parsedEmail = email.message_from_string(data['RFC822'])
	parsedBody = parsedEmail.get_payload(0)
	body = email.message_from_string(data['BODY[TEXT]'])
	# body_payload = body.get_payload(0)
	print "id: {0}".format(msgid)
	print "subject: {0}".format(data['ENVELOPE'][1])
	print ""
	print parsedBody	
	print ""
	# print body_payload
	print "end of message"
	print "<------------------------------------------------------------->"
	print ""
	print ""
	print ""




# print("Metadata")
# response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE'])
# for msgid, data in response.iteritems():
#     print('   ID %d: %d bytes, flags=%s' % (msgid,
#                                             data[b'RFC822.SIZE'],
#                                             data[b'FLAGS']))    
#     print ("{0}".format(data))
#     print 




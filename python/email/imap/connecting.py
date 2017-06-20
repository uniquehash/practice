
from __future__ import unicode_literals

from imapclient import IMAPClient
import imapclient
from backports import ssl

import os


ENV = os.environ

HOST = ENV['MAIL_A']
USERNAME = ENV['MAIL_U']
PASSWORD = ENV['MAIL_P']
ssl_bool = True
port = 993
ssl_verify_cert = False


context = imapclient.create_default_context()

# don't check if certificate hostname doesn't match target hostname
context.check_hostname = False
# don't check if the certificate is trusted by a certificate authority
context.verify_mode = ssl.CERT_NONE


print "setting up class..."

server = IMAPClient(HOST, use_uid=True, ssl=ssl_bool, port=port, ssl_context=context)

print "logging in..."

server.login(USERNAME, PASSWORD)

print "logged in!"
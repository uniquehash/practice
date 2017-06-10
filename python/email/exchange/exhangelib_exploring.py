from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
    EWSDateTime, EWSTimeZone, Configuration, NTLM, CalendarItem, Message, \
    Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
    HTMLBody, Build, Version

import time
import inspect

### setup and connecting

# Username in WINDOMAIN\username format. Office365 wants usernames in PrimarySMTPAddress
# ('myusername@example.com') format. UPN format is also supported.
credentials = Credentials(username=ENV['MAIL_U'], password=ENV['MAIL_P'])

# If you're running long-running jobs, you may want to enable fault-tolerance. Fault-tolerance
# means that requests to the server do an exponential backoff and sleep for up to a certain
# threshold before giving up, if the server is unavailable or responding with error messages.
# This prevents automated scripts from overwhelming a failing or overloaded server, and hides
# intermittent service outages that often happen in large Exchange installations.

# # If you want to enable the fault tolerance, create credentials as a service account instead:
# credentials = ServiceAccount(username='FOO\\bar', password='topsecret')

# # Set up a target account and do an autodiscover lookup to find the target EWS endpoint:
# account = Account(primary_smtp_address='obelanger@42.us.org', credentials=credentials,
                  # autodiscover=True, access_type=DELEGATE)

# # If your credentials have been given impersonation access to the target account, set a
# # different 'access_type':
# account = Account(primary_smtp_address='john@example.com', credentials=credentials,
#                   autodiscover=True, access_type=IMPERSONATION)


# # If the server doesn't support autodiscover, use a Configuration object to set the server
# # location:
config = Configuration(server=ENV['MAIL_A'], credentials=credentials)
account = Account(primary_smtp_address=ENV['MAIL_U'], config=config,
                  autodiscover=False, access_type=DELEGATE)

# # 'exchangelib' will attempt to guess the server version and authentication method. If you
# # have a really bizarre or locked-down installation and the guessing fails, or you want to avoid
# # the extra network traffic, you can set the auth method and version explicitly instead:
# version = Version(build=Build(15, 0, 12, 34))
# config = Configuration(server='example.com', credentials=credentials, version=version, auth_type=NTLM)

# # If you're connecting to the same account very often, you can cache the autodiscover result for
# # later so you can skip the autodiscover lookup:
# ews_url = account.protocol.service_endpoint
# ews_auth_type = account.protocol.auth_type
# primary_smtp_address = account.primary_smtp_address

# # 5 minutes later, fetch the cached values and create the account without autodiscovering:
# config = Configuration(service_endpoint=ews_url, credentials=credentials, auth_type=ews_auth_type)
# account = Account(
#     primary_smtp_address=primary_smtp_address, config=config, autodiscover=False, access_type=DELEGATE
# )

### Folders

# # The most common folders are available as account.calendar, account.trash, account.drafts, account.inbox,
# # account.outbox, account.sent, account.junk, account.tasks, and account.contacts.
# #
# # If you want to access other folders, you can either traverse the account.folders dictionary, or find
# # the folder by name, starting at a direct or indirect parent of the folder you want to find. To search
# # the full folder hirarchy, start the search from account.root:
# python_dev_mail_folder = account.root.get_folder_by_name('python-dev')
# # If you have multiple folders with the same name in your folder hierarchy, start your search further down
# # the hierarchy:
# foo1_folder = account.inbox.get_folder_by_name('foo')
# foo2_folder = python_dev_mail_folder.get_folder_by_name('foo')
# # For more advanced folder traversing, use some_folder.get_folders()

# # Folders have some useful counters:
# account.inbox.total_count
# account.inbox.child_folder_count
# account.inbox.unread_count
# # Update the counters
# account.inbox.refresh()

# i = 2
# while (i > 0):
# 	account.inbox.refresh()	
# 	inbox_count = account.inbox.total_count
# 	inbox_child_folder_count = account.inbox.child_folder_count
# 	inbox_unread_count = account.inbox.unread_count
# 	print "i: {0}".format(i)
# 	print "inbox_count: {0}".format(inbox_count)
# 	print "inbox_child_folder_count: {0}".format(inbox_child_folder_count)
# 	print "inbox_unread_count: {0}".format(inbox_unread_count)
	
# 	i -= 1
# 	time.sleep(10)

print dir(account)
print ""

var_dict = vars(account)
for k in var_dict.keys():
	print "{0}: {1}".format(k, var_dict[k])

print ""
print "inbox: {0}".format(account.inbox)
print dir(account.inbox)
print "inbox.unread_count: {0}".format(account.inbox.unread_count)


print ""
print "fullname: {0}".format(account.fullname)
print "access_type: {0}".format(account.access_type)

print ""
print "sent: {0}".format(account.sent)
print dir(account.sent)
print "sent.unread_count: {0}".format(account.sent.unread_count)

print ""
print "calendar.__doc__: {0}".format(account.calendar.__doc__)
print dir(account.calendar)
print ""
print "calendar.account: {0}".format(account.calendar.account)
print "calendar.folder_class: {0}".format(account.calendar.folder_class)
print "calendar.from_xml: {0}".format(account.calendar.from_xml)
print "calendar.get: {0}".format(account.calendar.get)
print "calendar.get_folders: {0}".format(account.calendar.get_folders)
print "calendar.name: {0}".format(account.calendar.name)
print "calendar.folder_class: {0}".format(account.calendar.folder_class)
print "calendar.test_access: {0}".format(account.calendar.test_access)
print "calendar.to_xml: {0}".format(account.calendar.to_xml)
print "calendar.total_count: {0}".format(account.calendar.total_count)
print "calendar.view: {0}".format(account.calendar.view)



print ""
# print "folders: {0}".format(account.folders)
# print dir(account.sent)
# print "sent.unread_count: {0}".format(account.sent.unread_count)

# item = CalendarItem(folder=account.calendar, subject='foo')
# item.save()
# print item.__class__
# print item.__doc__
# print dir(item.save)
# print item.save.__call__
# print item.save.__class__
# print item.save.__cmp__
# print item.save.__delattr__
# print item.save.__doc__
# print item.save.__format__
# print item.save.__func__
# print item.save.__get__
# print item.save.__getattribute__
# print item.save.__hash__
# print item.save.__init__
# print item.save.__new__
# print item.save.__reduce__
# print item.save.__reduce_ex__
# print item.save.__self__
# print item.save.__setattr__
# print item.save.__str__
# print item.save.__subclasshook__
# print item.save.im_class
# print item.save.im_func
# print item.save.im_self
# print item.__code__.co_varnames
print ""
# item.subject = 'bar'
# item.save()
# item.delete()






























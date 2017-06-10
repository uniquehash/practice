from pythonzimbra.tools import auth
from pythonzimbra.communication import Communication
import pprint
import os
pp = pprint.PrettyPrinter(indent=4)

ENV = os.environ
url = "https://"+ ENV['MAIL_A']+ "/service/soap"

def send_handle_request(comm, request_tupple):
	info_request = comm.gen_request(token=token)	
	info_request.add_request(request_tupple[0], request_tupple[1], request_tupple[2])
	info_response = comm.send_request(info_request)
	if not info_response.is_fault():
		# print info_response.get_response()['GetFolderResponse']['folder']['n']
		# print info_response.get_body()
		pp.pprint(info_response.get_response())

	else:
		print "error"
		print "fault_message: {0}".format(info_response.get_fault_message())
		print "fault_code: {0}".format(info_response.get_fault_code())	


comm = Communication(url)

token = auth.authenticate(
    url,
    ENV['MAIL_U'],
    ENV['MAIL_P'],
    use_password=True
)


folder_request = (
	"GetFolderRequest", 
	{
		"folder": {
			"path": "/inbox"
		}
	},
	"urn:zimbraMail"
)

calendar_item_summaries = (
	"GetCalendarItemSummariesRequest",
	{
		"s": 1496387562,
		"e": 1596388562,
		"l": "262"
	},
	"urn:zimbraMail"
)

send_msg = (
	"SendMsgRequest",
	{
		"m": {
			"su": "testing_baby",
			"content": "testing work it."
		}
	},
	"urn:zimbraMail"
)

get_data_sources_request = (
	"GetDataSourcesRequest",
	{

	},
	"urn:zimbraMail"
)

send_handle_request(comm, send_msg)
# send_handle_request(comm, calendar_item_summaries)








require "rb-scpt"
include Appscript

app('TextEdit').documents.end.make(
	:new => :document,
	:with_properties => {:text => "Hello World!\n"}
	)


puts app('TextEdit').documents[4].paragraphs[1].get

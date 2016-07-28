require 'rb-scpt'
include Appscript

te = app ('TextEdit')
doc = te.make(:new => :document)

te.set(doc.text, :to => 'Hello World')

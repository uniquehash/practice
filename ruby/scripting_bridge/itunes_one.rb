require "rb-scpt"
include Appscript

it = app('iTunes')
puts it

puts it.name.get

puts it.version.get

puts it.properties

puts "-----------------------------------"

puts it.elements

puts '-----------------------------------'

puts "1: " + it.play

puts it.items.get


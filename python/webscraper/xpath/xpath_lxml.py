#! /usr/local/bin/python

from lxml import html
import requests

page = requests.get('http://www.zappos.com/product/8586818/color/19861')

tree = html.fromstring(page.content)

a = [	"<li>These bold Kendra Scott\u2122 earrings add a pop of modern chic.</li>", 
        "<li>14K gold plate over brass with prong-set mother-of-pearl or blue onyx stone.</li>", 
        "<li>French hooks.</li>", 
        "<li class=\"measurements\">Measurements:\n<ul>\n<li> Width: 1 in</li>\n<li> Height: 2 in</li>\n<li> Weight: 0.38 oz</li>\n</ul>\n</li>", 
        "<li><strong>Store your accessories in an elegant Mele &amp; Co.\u2122 jewelry box:</strong><br><br><a href=\"http://www.zappos.com/mele-maria-plush-compartment-travel-case-jewelry-box-pink\"><img src=\"/download/m/e/l/meleadd-on7750651.jpg\" alt=\"\"></a></li>"]

d = "s"

for x in a:
	d = d.join(x)
	print x


print d
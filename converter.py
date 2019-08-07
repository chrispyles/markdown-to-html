########################################################
##### Markdown to HTML Converter for Documentation #####
#####                by Chris Pyles                #####
########################################################

import markdown2 as md
import sys

if len(sys.argv) == 1:
	print("Please enter a filename.")
else:
	for file_name in sys.argv[1:]:
		markdowner = md.Markdown()

		with open(file_name) as f:
			html = markdowner.convert(f.read())

		with open(file_name[:-2] + "html", "w+") as f:
			f.write(html)
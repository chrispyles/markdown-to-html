########################################################
##### Markdown to HTML Converter for Documentation #####
#####                by Chris Pyles                #####
########################################################

import markdown2 as md
import sys
import glob

if len(sys.argv) == 1:
	print("Please enter a filename.")
elif len(sys.argv) == 2 and "*" in sys.argv[2]:
	file_names = glob.glob(sys.argv[2])
else:
	file_names = sys.argv[1:]

for file_name in file_names:
	markdowner = md.Markdown()

	with open(file_name) as f:
		html = markdowner.convert(f.read())

	with open(file_name[:-2] + "html", "w+") as f:
		f.write(html)
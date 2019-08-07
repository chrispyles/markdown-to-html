########################################################
##### Markdown to HTML Converter for Documentation #####
#####                by Chris Pyles                #####
########################################################

import markdown2 as md
import sys
import glob


html_head = """
<!DOCTYPE html>
<html>
<head>
	<link href="https://fonts.googleapis.com/css?family=Poppins:400,400i,600,700|Roboto:400,400i,700&display=swap" rel="stylesheet">
	<style type="text/css">
		h1, h2, h3, h4, h5, h6 {
			font-family: 'Roboto', sans-serif;
			font-weight: 600;
		}

		h1, h2 {
			letter-spacing: 1px;
		}

		h1 {
			font-size: 30pt;
		}

		h2 {
			font-size: 20pt;
		}

		h3 {
			font-size: 14pt;
		}

		p {
			font-family: 'Roboto', sans-serif;
			font-size: 12pt;
		}

		div {
			width: 65%;
			margin: 0 auto;
		}
	</style>
</head>
<body><div>
"""

html_end = """
</div></body>
</html>
"""



if len(sys.argv) == 1:
	print("Please enter a filename.")
elif len(sys.argv) == 2 and "*" in sys.argv[1]:
	file_names = glob.glob(sys.argv[1])
else:
	file_names = sys.argv[1:]

for file_name in file_names:
	markdowner = md.Markdown()

	with open(file_name) as f:
		html = markdowner.convert(f.read())

	with open(file_name[:-2] + "html", "w+") as f:
		f.write(html_head + html + html_end)
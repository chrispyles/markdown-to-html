########################################################
##### HTML & CSS Template for MD to HTML Converter #####
#####                by Chris Pyles                #####
########################################################

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments_style import Monokai

# get css from pygments for syntax highlighting
code_css = HtmlFormatter(style=Monokai).get_style_defs("")

html_template = """<!DOCTYPE html>

<!--
		Generated using Markdown to HTML Converter by Chris Pyles.
		More at https://github.com/chrispyles/markdown-to-html

		Color scheme from https://colorhunt.co/palette/155146
-->

<html>
<head>
	<link href="https://fonts.googleapis.com/css?family=Poppins:400,400i,600,700|Roboto:400,400i,700&display=swap" rel="stylesheet">
	<style type="text/css">

		/* CSS for MD to HTML Converter
			by Chris Pyles */

    	body {{
    		margin-top: -27px;
    		margin-left: 0;
    		background-color: #ebefd0;
    	}}

		h1, h2, h3, h4, h5, h6 {{
			font-family: 'Roboto', sans-serif;
			font-weight: 600;
		}}

		h1, h2 {{
			letter-spacing: 1px;
		}}

		h1 {{
			font-size: 30pt;
		}}

		h2 {{
			font-size: 20pt;
		}}

		h3 {{
			font-size: 14pt;
		}}

		p, ul, th, td, ol {{
			font-family: 'Roboto', sans-serif;
			font-size: 12pt;
		}}

		ul.nav {{
			list-style-type: none;
			padding-left: 0;
		}}

		li.nav {{
			padding-left: 20px;
			width: 230px;
		}}

		li.nav:hover {{
			background-color: rgba(256, 256, 256, 0.5);
		}}

		th, td {{
			border-top: 1px solid black;
			border-left: 1px solid black;
			text-align: center;
			padding: 5px 2px;
		}}

		th {{
			font-weight: 600;
		}}

		div {{
			width: 800px;
			margin: 0 0 0 255px;
			background-color: white;
			padding: 0 20px;
			margin-top: -27px;
		}}

		div#top {{
			background-color: #ff502f;
			margin-top: 27px;
			width: 100%;
			height: 10px;
			margin-left: 0;
			position: fixed;
			z-index: 1;
		}}

		div#body {{
			position: fixed;
			margin-top: 15px;
			height: 100%;
			padding-bottom: 100%;
			overflow: scroll;
		}}

		table {{
			width: 75%;
			margin: 0 auto;
			border-right: 1px solid black;
			border-bottom: 1px solid black;
			border-spacing: 0;
			table-layout: fixed;
		}}

		p.code {{
			width: 95%;
			margin: 10px auto;
			padding: 10px;
			background-color: rgba(222, 222, 222, 0.5);
		}}

		nav {{
			position: fixed;
			width: 250px;
			padding-left: 5px;
			height: 100%;
			background-color: #49beb7;
			color: white;
			margin-top: 36px;
		}}

		/* Resize div for Pygments. */
		div.highlight {{
			font-size: 12pt;
			width: 95%;
			margin: 10px auto;
			padding: 10px;
			background-color: #1d1e19;
			color: #f6f7ee;
			overflow: scroll;
		}}

		pre {{
			margin: 0;
		}}

		/* Below is imported the style from Pygments. */

		{}

	</style>
</head>
<body><div id="body">
</div></body>
</html>
""".format(code_css)

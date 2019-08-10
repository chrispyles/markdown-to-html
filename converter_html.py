from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments_style import MDtoHTMLStyle

# get css from pygments for syntax highlighting
code_css = HtmlFormatter(style=MDtoHTMLStyle).get_style_defs("")

html_template = """
<!DOCTYPE html>
<html>
<head>
	<link href="https://fonts.googleapis.com/css?family=Poppins:400,400i,600,700|Roboto:400,400i,700&display=swap" rel="stylesheet">
	<style type="text/css">

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
			width: 65%;
			margin: 0 auto;
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
			width: 30%;
			padding-left: 5px;
		}}

		/* Resize div for Pygments. */
		div.highlight {{
			font-size: 12pt;
			width: 95%;
			margin: 10px auto;
			padding: 10px;
			background-color: #1d1e19;
		}}

		pre {{
			margin: 0;
		}}

		/* Below is imported the style from Pygments. */

		{}

	</style>
</head>
<body><div>
</div></body>
</html>
""".format(code_css)

########################################################
##### HTML & CSS Template for MD to HTML Converter #####
#####                by Chris Pyles                #####
########################################################

import re
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from .pygments_style import Monokai
from .pygments_style import Colors

# get css from pygments for syntax highlighting
code_css = HtmlFormatter(style=Monokai).get_style_defs("")

# color palette
palette = ["#00b0da", "#46535e", "#46535e"]

# imported fonts
font_url = "https://fonts.googleapis.com/css?family=Roboto:400,400i,700&display=swap"
font_regex = r"(=|\|)(\w+)(:|&)"
font_name = re.search(font_regex, font_url)[1]

html_template = f"""<!DOCTYPE html>

<!--
		Generated using Markdown to HTML Converter by Chris Pyles.
		More at https://github.com/chrispyles/markdown-to-html
-->

<html>
<head>
	<!-- <link href="{font_url}" rel="stylesheet"> -->

	<!-- Boostrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>

    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    
	<style type="text/css">

		/* CSS for MD to HTML Converter
			by Chris Pyles

    	body {{
    		margin-top: -27px;
    		margin-left: 0;
    		background-color: {palette[0]};
    	}}

		h1, h2, h3, h4, h5, h6 {{
			font-family: '{font_name}', sans-serif;
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
			font-family: '{font_name}', sans-serif;
			font-size: 12pt;
		}}

		p#header {{
			color: white;
			padding-left: 235px;
		}}

		ul.nav {{
			list-style-type: none;
			padding-left: 15px;
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
			background-color: {palette[1]};
			margin-top: 27px;
			width: 100%;
			height: 52px;
			margin-left: 0;
			position: fixed;
			z-index: 1;
		}}

		div#body {{
			position: absolute;
			margin-top: 60px;
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

		table#header {{
			width: 100%;
		    height: auto;
		    border: none;
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
			background-color: {palette[2]};
			color: white;
			margin-top: 36px;
			padding-top: 6px;
			z-index: 2;
		}}

		a.nav:link, a.nav:hover, a.nav:visited, a.nav:active {{
			color: white;
		}}

		*/

		/* Resize div for Pygments. */
		div.highlight {{
			font-size: 12pt;
			width: 98%;
			margin: 10px auto;
			padding: 10px;
			background-color: {Colors.BLACK};
			color: {Colors.WHITE} !important;
			overflow: scroll;
			border-radius: 5px;
		}}

		pre {{
			margin: 0;
			color: {Colors.WHITE} !important;
		}}

		.p {{
			color: {Colors.WHITE} !important;
		}}

		/* Below is imported the style from Pygments. */

		{code_css}

	</style>
	
</head>
<body><div class="container" id="body">
</div></body>
</html>
"""

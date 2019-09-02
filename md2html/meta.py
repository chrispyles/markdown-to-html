###########################
##### Metadata Parser #####
##### by Chris Pyles  #####
###########################

import yaml

def create_meta(path):
	"""
	Creates HTML metadata from information in YAML file located at PATH

	Args:

	* `path` (`str`): path to a YAML metadata file

	Returns:

	* `str`. The HTML head
	"""
	with open(path) as f:
		global meta
		meta = yaml.safe_load(f)
	
	new_head = "<head>\n\t<title>{}</title>\n".format(meta["title"])

	if "description" in meta:
		new_head += "\t<meta name=\"description\" content=\"{}\">\n".format(meta["description"])
	
	if "author" in meta:
		new_head += "\t<meta name=\"author\" content=\"{}\">\n".format(meta["author"])
	
	new_head += "\t<!-- <link"

	return new_head

def create_nav(path=None, meta=None):
	"""
	Creates HTML navbar from YAML metadata at PATH or from existing dict META

	Args:

	* `path = None` (`str`): Location of nav YAML file
	* `meta = None` (`dict`): Dictionary of site metadata with navigation info

	Returns:

	* `str`. The HTML nav element
	"""
	if meta:
		with open(meta) as f:
			meta = yaml.safe_load(f)
		nav = meta["navigation"]
	else:
		with open(namespace["nav"]) as f:
			nav = yaml.safe_load(f)

	nav_html = """<body><nav class=\"navbar navbar-expand-md navbar-light bg-light\">
	
	<a class=\"navbar-brand\" href=\"#\">""" + nav["nav_title"] + """</a>
	
	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    	<span class="navbar-toggler-icon"></span>
 	</button>

 	<div class="collapse navbar-collapse" id="navbarSupportedContent">
 		<ul class="navbar-nav ml-auto">
	"""

	for link in nav["links"]:
		nav_html += "\t\t\t<li class=\"nav-item active\"><a class=\"nav-link\" href=\"" + link["url"] + "\">" + link["title"] + "</a></li>\n"
		if link["url"] == "index.html":
			home_page_name = link["title"]

	nav_html += "</ul></div></nav>\n\n<div class=\"container\" id=\"body\">\n"

	return nav_html
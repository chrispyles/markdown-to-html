###########################################################
##### Cystom Pygments Styles for MD to HTML Converter #####
#####                  by Chris Pyles                 #####
###########################################################

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic

blue = "#53d1ed"
green = "#96e309"
orange = "#fd8700"
pink = "#f7005f"
purple = "#9d60ff"
yellow = "#e0d75a"
black = "#1d1e19"
white = "#f6f7ee"
grey = "#625f4b"

class Monokai(Style):
	default_style = ""
	styles = {
		Comment: "italic {}".format(grey),
		Keyword: "bold {}".format(blue),
		Name: "{}".format(white),
		Name.Function: "{}".format(green),
		Name.Class: "bold {}".format(blue),
		String: "{}".format(yellow),
		Number: "{}".format(purple),
		Operator: "{}".format(pink),
		Generic: "{}".format(orange)
	}
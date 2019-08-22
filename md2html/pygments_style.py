###########################################################
##### Cystom Pygments Styles for MD to HTML Converter #####
#####                  by Chris Pyles                 #####
###########################################################

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic

class Colors:
	BLUE = "#53d1ed"
	GREEN = "#96e309"
	ORANGE = "#fd8700"
	PINK = "#f7005f"
	PURPLE = "#9d60ff"
	YELLOW = "#e0d75a"
	BLACK = "#1d1e19"
	WHITE = "#f6f7ee"
	GREY = "#625f4b"

class Monokai(Style):
	default_style = ""
	styles = {
		Comment: "italic {}".format(Colors.ORANGE),
		Keyword: "bold {}".format(Colors.BLUE),
		Name: "{}".format(Colors.WHITE),
		Name.Function: "{}".format(Colors.GREEN),
		Name.Class: "bold {}".format(Colors.BLUE),
		String: "{}".format(Colors.YELLOW),
		Number: "{}".format(Colors.PURPLE),
		Operator: "{}".format(Colors.PINK),
		Generic: "{}".format(Colors.ORANGE)
	}
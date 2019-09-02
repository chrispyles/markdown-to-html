########################################################
##### Syntax Highlighting for MD to HTML Converter #####
#####                by Chris Pyles                #####
########################################################

from pygments import highlight
from pygments.formatters import HtmlFormatter
import pygments.lexers as lx
import re

lexers = {
	"python" : lx.PythonLexer,
	"bash" : lx.BashLexer,
	"julia" : lx.JuliaLexer,
	"java" : lx.JavaLexer,
	"yaml" : lx.YamlLexer
}

code_regex = r"\`\`\`\w*\n(.*\n)+?\`\`\`"
code_start_regex = r"```\w*"

def get_syntax(code):
	"""
	Gets the code syntax from Markdown code

	Args:

	* `code` (`str`): Markdown block code

	Returns:

	* `str`. The name of the language
	"""
	return re.match(code_start_regex, code)[0][3:]

def get_lexer(syntax):
	"""
	Returns the pygments lexer for the specified language SYNTAX

	Args:

	* `syntax` (`str`): The language name

	Returns:

	* `pygments.RegexLexer`. The pygments lexer subclass for that language
	"""
	if syntax not in lexers:
		return None
	return lexers[syntax]

def run_lexer(code):
	"""
	Runs the lexer on the code in the Markdown, stripping out all backticks

	Args:

	* `code` (`str`): Markdown block code

	Returns:

	* `str`. HTML formatted code from pygments lexer
	"""
	syntax = get_syntax(code)
	lexer = get_lexer(syntax)
	if lexer == None:
		lexer = lx.TextLexer
	code = re.sub(code_start_regex, "", code)
	return highlight(code, lexer(), HtmlFormatter())

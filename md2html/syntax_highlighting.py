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
	"java" : lx.JavaLexer
}

code_regex = r"```\w*\n(.*\n)+?```"
code_start_regex = r"```\w*"

def get_syntax(code):
	return re.match(code_start_regex, code)[0][3:]

def get_lexer(syntax):
	if syntax not in lexers:
		return None
	return lexers[syntax]

def run_lexer(code):
	syntax = get_syntax(code)
	lexer = get_lexer(syntax)
	if lexer == None:
		lexer = lx.TextLexer
	code = re.sub(code_start_regex, "", code)
	return highlight(code, lexer(), HtmlFormatter())

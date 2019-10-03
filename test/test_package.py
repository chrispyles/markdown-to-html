##################################
##### Unit Tests for MD2HTML #####
##################################

from md2html import *
import unittest
import subprocess
import os
import re

class TestMainMethod(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		"""Sets paths to input and output files"""
		self._meta_path = "test/meta.yml"
		self._test_path = "test/test.md"
		self._usage_path = "test/usage.md"
		self._test_output_path = "test/test_output.html"
		self._usage_output_path = "test/usage_output.html"

	def test_test_output(self):
		"""Runs test on test/test.md"""
		namespace = dict(
			nav = None,
			site = self._meta_path,
			files = [self._test_path]
		)
		main(namespace)
		with open(self._test_output_path) as f:
			correct_output = f.read()
		with open(self._test_path[:-3] + ".html") as f:
			output = f.read()

		self.assertEqual(correct_output, output)

	def test_usage_output(self):
		"""Runs test on test/usage.md"""
		namespace = dict(
			nav = None,
			site = self._meta_path,
			files = [self._usage_path]
		)
		main(namespace)
		with open(self._usage_output_path) as f:
			correct_output = f.read()
		with open(self._usage_path[:-3] + ".html") as f:
			output = f.read()

		self.assertEqual(correct_output, output)

	@classmethod
	def tearDownClass(self):
		"""Removes output HTML files"""
		remove = ["rm", self._test_path[:-3] + ".html", self._usage_path[:-3] + ".html"]
		subprocess.run(remove)


class TestCLI(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		"""Sets paths to input and output files"""
		self._meta_path = "test/meta.yml"
		self._test_path = "test/test.md"
		self._usage_path = "test/usage.md"
		self._star_path = "test/*.md"
		self._single_input_namespace = {
			"nav": None,
			"site": self._meta_path,
			"files": [self._test_path]
		}
		self._star_input_namespace = {
			"nav": None,
			"site": self._meta_path,
			"files": [self._star_path]
		}

		with open("bin/md2html") as read_file:
			with open("test/cli.py", "w+") as write_file:
				write_file.write(read_file.read())

		from .cli import make_parser
		self._make_parser = lambda self: make_parser()

	def test_single_input(self):
		"""Runs test on test/test.md"""
		parser = self._make_parser()
		args = ["-s", self._meta_path, self._test_path]
		namespace = vars(parser.parse_args(args))
		self.assertEqual(namespace, self._single_input_namespace)

	def test_star_input(self):
		"""Runs test on test/*.md"""
		parser = self._make_parser()
		args = ["-s", self._meta_path, self._star_path]
		namespace = vars(parser.parse_args(args))
		self.assertEqual(namespace, self._star_input_namespace)

	@classmethod
	def tearDownClass(self):
		remove = ["rm", "test/cli.py"]
		subprocess.run(remove)

import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "md2html",
	version = "1.2",
	author = "Chris Pyles",
	author_email = "cpyles@berkeley.edu",
	description = "MD to HTML converter",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/chrispyles/markdown-to-html",
	license = "BSD-3-Clause",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
	],
	scripts=["bin/md2html"]
)
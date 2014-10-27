import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "couchcushion",
	version = "0.0.1",
	author = "Jamie Bliss",
	author_email = "astronouth7303@gmail.com",
	description = "Installation tool for CouchDB server-side components",
	long_description=read('README.rst')
	# license = "BSD",
	keywords = "example documentation tutorial",
	url = "https://github.com/astronouth7303/couchcusion-py",
	packages=find_packages(),
	long_description=read('README'),
	# classifiers=[
	#	 "Development Status :: 3 - Alpha",
	#	 "Topic :: Utilities",
	#	 "License :: OSI Approved :: BSD License",
	# ],
	setup_requires = [ "setuptools_git >= 0.3", ],
	entry_points = {
		# "distutils.commands": [
		# 	"foo = mypackage.some_module:foo",
		# ],
		"distutils.setup_keywords": [
			"couchdb = couchcushion:validate_config",
		],
	},
)

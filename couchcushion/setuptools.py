import setuptools.command.install
import setuptools.command.develop
from pprint import pprint

def validate_config(dist, attr, value):
	print("ValidateConfig:", dist, attr, value)

class install(setuptools.command.install.install):
	def initialize_options(self):
		print("install.initialize_options")
		return super().initialize_options()

	def finalize_options(self):
		print("install.finalize_options")
		return super().finalize_options()

	def run(self):
		print("install.run")
		return super().run()

class develop(setuptools.command.develop.develop):
	def initialize_options(self):
		print("develop.initialize_options")
		return super().initialize_options()

	def finalize_options(self):
		print("develop.finalize_options")
		return super().finalize_options()

	def run(self):
		print("develop.run")
		pprint(vars(self.distribution))
		pprint(self.distribution.couchdb)
		return super().run()

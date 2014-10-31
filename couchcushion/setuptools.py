import setuptools.command.install
import setuptools.command.develop
from pprint import pprint
from . import register_external, register_static

def validate_config(dist, attr, value):
	print("ValidateConfig:", dist, attr, value)

class cdb_helper:
	def process(self, cdb):
		if 'statics' in cdb:
			self.process_statics(cdb['statics'])

	def process_statics(self, statics):
		for prefix, path in statics.items():
			# FIXME: Resolve path
			register_static(prefix, path)

	def process_daemons(self, daemons):
		pass

class install(setuptools.command.install.install, cdb_helper):
	def initialize_options(self):
		print("install.initialize_options")
		return super().initialize_options()

	def finalize_options(self):
		print("install.finalize_options")
		return super().finalize_options()

	def run(self):
		print("install.run")
		return super().run()

class develop(setuptools.command.develop.develop, cdb_helper):
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

		cdb = self.distribution.couchdb
		if cdb is not None:
			self.process(cdb)
		return super().run()

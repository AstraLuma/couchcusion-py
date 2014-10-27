===============================
CouchCusion (Python setuptools)
===============================
CouchCusion is a complement to CouchApp to easy deployment of server-side code: 
externals, os daemons, static dirs, and other config-based hooks.

This is the version for Python, based on setuptools. You configure hooks/paths 
in your ``setup.py`` and CouchDB is configured when you run ``install`` or 
``develop``.

::
	setup(
		...
		couchdb={
			'daemons': [
				'myscript.py',
				'mypackage',
			],
			'handlers': {
				'_spam': 'eggs.py',
				'_foo': 'bar.quux',
			},
		},
		...
	)
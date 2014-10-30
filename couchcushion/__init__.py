import os

def register_external(prefix, host,port=None, *, secure=False):
	"""register_external(str, [str,] int, [secure=bool])
	Registers an external with CouchDB. If host is not given, assumed to be localhost
	"""
	if port is None:
		port, host = host, 'localhost'

	if secure:
		url = 'https://{}:{}'.format(host, port)
	else:
		url = 'http://{}:{}'.format(host, port)

	setting = 'httpd_global_handlers/{}'.format(prefix)
	value = '{couch_httpd_proxy, handle_proxy_req, <<"{}">>}'.format(url)

	print("TODO: set {!r} to {!r}".format(setting, value))

def register_daemon(name, command):
	setting = 'os_daemons/{}'.format(name)
	print("TODO: set {!r} to {!r}".format(setting, command))

def register_static(prefix, path):
	path = os.path.abspath(path)
	setting = 'httpd_global_handlers/{}'.format(prefix)
	value = '{couch_httpd_misc_handlers, handle_utils_dir_req, "{}"}'.format(path)

	print("TODO: set {!r} to {!r}".format(setting, value))

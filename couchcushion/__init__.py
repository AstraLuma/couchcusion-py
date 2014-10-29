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

	print("TODO: register {} on prefix {}".format(url, prefix))
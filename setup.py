from setuptools import setup, find_packages

setup(
	name = "django-locality",
	version = "0.2.0-0.0.1",
	url = 'https://github.com/chrisdpratt/django-locality',
	license = 'AGPL',
	description = 'Countries and territories, made usable.',
	author = 'TK Kocheran',
	author_email = 'rfkrocktk@gmail.com',
	maintainer = 'Chris Pratt',
	maintainer_email = 'chrisdpratt@gmail.com',
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	package_data = {
		'': ['locality/fixtures/*.json']
	},
	install_requires = [
		'Django>=1.3.0',
		'setuptools'
	],
	zip_safe = False,
)

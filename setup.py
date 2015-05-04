#!/usr/bin/python

from setuptools import setup

setup(
	# Basic package information.
	name = 'Zendesk',
	author = 'Max Gutman, Stefan Tjarks, Matthew de Verteuil',
	version = '1.3-vmf',
	author_email = 'max@eventbrite.com',
	packages = ['zendesk'],
	include_package_data = True,
	install_requires = ['requests', 'simplejson'],
	license='LICENSE.txt',
	url = 'https://github.com/eventbrite/zendesk',
	keywords = 'zendesk api helpdesk',
	description = 'Python API Wrapper for Zendesk',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	],
)



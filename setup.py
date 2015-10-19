from setuptools import setup, find_packages

setup(
    name = 'kis.apache_wsgi',
    version = '0.1.0',
    description = 'Request url',
    url = 'https://github.com/juliengk/python-apache-wsgi',
    author = 'Julien Kassar',
    author_email = 'code@kassisol.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['kis'],
    install_requires = [
        'setuptools',
    ],
    zip_safe = False,
)


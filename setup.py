import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tabular-permissions',
<<<<<<< HEAD
    version='1.1',
=======
    version='1.0.9',
>>>>>>> parent of 005082d... Version 1.10. Support for django 1.11
    packages=['tabular_permissions'],
    include_package_data=True,
    license='BSD License',
    description='Display django permissions in a tabular format that is user friendly, and highly customisable',
    long_description=README,
    url='https://github.com/RamezIssac/django-tabular-permissions',
    author='Ramez Ashraf',
    author_email='ramez@radev.io',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
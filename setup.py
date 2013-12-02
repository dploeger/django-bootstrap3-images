import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bootstrap3-images',
    version='1.0-rc1',
    packages=['bootstrap3_images'],
    include_package_data=True,
    license='BSD 2-clause License',  # example license
    description='Django model field and widget for storing, retrieving and displaying bootstrap3 glyphicon-images',
    long_description=README,
    url='https://github.com/dploeger/django-bootstrap3-images',
    author='Dennis Ploeger',
    author_email='develop@dieploegers.de',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires = [
        "Django >= 1.5",
    ]
)

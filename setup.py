import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tagconstants',
    version='0.1',
    packages=['tagconstants', 'tagconstants.templatetags'],
    include_package_data=True,
    install_requires='django >= 1.7',
    license='MIT License',
    description='Define constants in your settings, and make them available in your templates.',
    long_description=README,
    maintainer="Nick Lourie",
    maintainer_email="developer@nicholaslourie.com",
    keywords = "django constants templates settings templatetags",
    url='https://github.com/nalourie/django-tagconstants',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)


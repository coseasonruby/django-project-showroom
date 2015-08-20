from setuptools import setup, find_packages

import os

setup(
    name='django-website-showroom',
    version='0.2',
    description='General purpose showroom for presenting a collection of categorized websites',
    author='Holger Drewes',
    author_email='Holger.Drewes@gmail.com',
    url='https://github.com/holgerd77/django-website-showroom/',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    packages=find_packages(),
    include_package_data=True,
    #install_requires=[
        #'Django>=1.2',
        #'Scrapy>=0.14',
        # Scheduling
        #'django-kombu',
        #'django-celery',
    #],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)

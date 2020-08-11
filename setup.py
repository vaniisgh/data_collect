from setuptools import (setup, find_packages)

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='data-collect',
    version='0.0.1',
    author='Vani Singh',
    author_email='vani11537@one.ducic.ac.in',
    description='Flask-app powered to upload csv files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='',
    url='https://github.com/vaniisgh/data_collect',
    packages=find_packages(),
    keywords=(
        'celery pandas csv '
        'python flask'
    ),
    classifiers=[
        'License :: ',
        'Development Status :: Alpha',
        'Intended Audience :: ',
        'Topic :: ',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

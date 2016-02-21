from distutils.core import setup

setup(
    name='phpunit-files-selector',
    version='0.1dev',
    license='MIT',
    packages=['phpunit-files-selector',],
    long_description=open('README.txt').read(),
    scripts=['phpunit-files-selector/phpunit-files-selector.py']
)

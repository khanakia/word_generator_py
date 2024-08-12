from setuptools import setup

setup(
   name='foo',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   # packages=['foo'],  #same as name
   install_requires=['sqlalchemy', 'psycopg2', 'python-whois'], #external packages as dependencies
)
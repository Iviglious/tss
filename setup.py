"""Module defining the setup of the app"""

from setuptools import setup

setup(name='TreatSmaSophie'
      , version='1.0'
      , description='Charity website for helping Sophie'
      , author='Ivaylo Shalev'
      , author_email='ivoshalev@gmail.com'
      , url='https://github.com/Iviglious/tss'
      , install_requires=['Flask>=0.7.2'
                          , 'flask-wtf'
                          , 'flask-babel'
                          , 'markdown'
                          , 'flup'
                          , 'unirest'
                          , 'bokeh']
     )

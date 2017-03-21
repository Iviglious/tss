from setuptools import setup

setup(name='FBA',
      version='1.0',
      description='OpenShift App',
      author='Ivaylo Shalev',
      author_email='ivoshalev@gmail.com',
      url='https://github.com/Iviglious',
      #install_requires=['Flask>=0.7.2', 'MarkupSafe'],
      install_requires=['Flask>=0.7.2','flask-wtf','flask-babel','markdown','flup']
      )

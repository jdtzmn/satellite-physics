from setuptools import setup, find_packages

with open('LICENSE') as f:
      license = f.read()

setup(name='satellite-physics',
      version='0.1.0',
      description='A simulation of planets orbitting a central mass',
      author='Jacob Daitzman',
      author_email='jdtzmn@gmail.com',
      url='https://github.com/jdtzmn/satellite-physics',
      license=license,
      packages=find_packages()
)

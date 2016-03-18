try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

# EDIT
#
# FROM HERE
author = 'Pedro Pinto da Silva'

download_url = 'https://github.com/PedrosWits/CasinoRoyale.py'

url = download_url

author_email = 'ppintodasilva@gmail.com'

version = '0.1'

dependencies = []

packages = ['casino']

scripts = []

name = 'Casino Royale dot py'

description = 'A small python library for tossing biased coins and ' \
              'rolling loaded dices based on Keith Schwarz excellent ' \
              'post: "Darts, Dice and Coins: Sampling from a Discrete ' \
              'Distribution" - http://www.keithschwarz.com/darts-dice-coins'
#
# TO HERE
#

config = {
  'description': description,
  'author': author,
  'url': url,
  'download_url': download_url,
  'author_email': author_email,
  'version': version,
  'install_requires': dependencies,
  'packages': packages,
  'scripts': scripts,
  'name': name
}

setup(**config)

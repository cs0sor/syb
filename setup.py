import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'pyramid_beaker',
    'pyramid_mailer',
    'deform_bootstrap',
    'pyramid_layout'
    ]

setup(name='stuff_your_boss',
      version='0.0',
      description='stuff_your_boss',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='stuff_your_boss',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = stuff_your_boss:main
      [console_scripts]
      initialize_stuff_your_boss_db = stuff_your_boss.scripts.initializedb:main
      """,
      )

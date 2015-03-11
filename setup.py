from setuptools import setup

tests_require = []

setup(name='statswriter',
      version='0.6',
      description='Tool which reads a stream of metrics and pushes them into statsd.',
      url='http://github.com/andrewguy9/statswriter',
      author='andrew thomson',
      author_email='athomsonguy@gmail.com',
      license='MIT',
      packages=['statswriter'],
      install_requires = ['docopt', 'statsd'],
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points = {
        'console_scripts': [
            'statswriter = statswriter:main'
          ],
      },
      zip_safe=False)

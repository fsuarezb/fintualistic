from setuptools import setup, find_packages


setup(
    name='fintualistic',
    version='0.0',
    author="Fernando Suarez",
    author_email='fernando@fintual.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/fsuarezb/fintualistic',
    keywords='fintual fintualistic',
    install_requires=[
          'pandas', 'plotly'
      ],

)
from setuptools import setup, find_packages


setup(
    name='fintualistic',
    version='0.0',
    author="Fernando Suarez",
    author_email='fsuarez1@uc.cl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/fsuarezb/fintualistic',
    keywords='fintual fintualistic',
    install_requires=[
          'pandas', 'plotly'
      ],

)
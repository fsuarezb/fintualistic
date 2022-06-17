from setuptools import setup, find_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    name='fintualistic',
    version='0.4',
    author="Fernando Suarez",
    author_email='fsuarez1@uc.cl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/fsuarezb/fintualistic',
    keywords='fintual fintualistic',
    install_requires=[
          'pandas', 'plotly'
      ],
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown'

)
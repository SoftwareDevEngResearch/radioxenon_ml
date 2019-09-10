from setuptools import setup, find_packages
from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'radioxenon_ml', '_version.py')) as version_file:
    exec(version_file.read())
print(version_file)
with open(path.join(here, 'README.md')) as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'CHANGELOG.md')) as changelog_file:
    changelog = changelog_file.read()

desc = readme + '\n\n' + changelog
try:
    import pypandoc
    long_description = pypandoc.convert_text(desc, 'rst', format='md')
    with open(path.join(here, 'README.rst'), 'w') as rst_readme:
        rst_readme.write(long_description)
except (ImportError, OSError, IOError):
    long_description = desc

install_requires = [
    'numpy',
]

tests_require = [
    'pytest',
    'pytest-cov',
]

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
setup_requires = ['pytest-runner'] if needs_pytest else []

setup(
    name='radioxenon_ml',
    version=__version__,
    description='Maximum Likelihood analysis of combined radioxenon spectra',
    long_description=long_description,
    author='Steven A. Czyz',
    author_email='czyzs@oregonstate.edu',
    url='https://github.com/SoftwareDevEngResearch/radioxenon_ml',
    classifiers=[
        'License :: MIT License',
        'Intended Audience :: Those studying combined spectra',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    license='MIT License',
    install_requires=install_requires,
    python_requires='>=3',
    packages=['radioxenon_ml', 'radioxenon_ml.read_in', 
              'radioxenon_ml.solve','radioxenon_ml.test_files'],
    package_dir={
        'radioxenon_ml': 'radioxenon_ml',
        'radioxenon_ml.read_in': 'radioxenon_ml/read_in',
        'radioxenon_ml.solve': 'radioxenon_ml/solve',
        'radioxenon_ml.test_files': 'radioxenon_ml/test_files',
        
        },
    include_package_data=True,
    tests_require=tests_require,
    setup_requires=setup_requires,
    zip_safe=False,
)

# get_ipython().system('pip install -U pip setuptools')
import setuptools

with open('README.md', 'r') as file:
    desc = file.read()
setuptools.setup(name='TextPrepR',
                 version='0.0.1',
                 author='Rumeysa Keskin',
                 author_email='rumeyskeskn@gmail.com',
                 long_description=desc,
                 long_description_content_type = 'text/markdown',
                 package =setuptools.find_packages(),
                 classifiers=['Programming Language:: Python :: 3',
                               'License :: OSI Aproved :: MIT License'
                               'Operating System:: OS Independent'],
                               python_requires = ">=3.8")

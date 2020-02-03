import setuptools

with open('README.rst') as file:

    readme = file.read()

name = 'sandbox'

version = '0.0.0'

author = 'HealthyGamer'

url = f'https://github.com/{author}/{name}'

setuptools.setup(name=name,
                 version=version,
                 author=author,
                 url=url,
                 packages=setuptools.find_packages(),
                 license='MIT',
                 description='Workshop Examples',
                 long_description=readme,
                 extras_require={'docs': ['sphinx', 'sphinx_rtd_theme']})

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="pipenv-test",
    version='0.0.1',
    description="Test with cython",
    ext_modules= cythonize('helloworld.pyx'),
    include_package_data=True,
)
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="pipenv-test",
    version='0.0.1',
    description="Test with cython",
    ext_modules= cythonize('print_json.pyx'),
    data_files=[('config/config.json')],
    include_package_data=True,
)
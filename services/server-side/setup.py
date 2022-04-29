import re
from pathlib import Path

import setuptools

NAME = 'flint'
HERE = Path(__file__).parent


__version__ = re.findall(
    r"""__version__\s*=\s*['"](.*)['"]""",
    (HERE / 'src' / NAME / '_version.py').read_text()
)[0]


setuptools.setup(
    name=NAME,
    version=__version__,
    description='a web application for FLINT',
    include_package_data=True,
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    zip_safe=False,
    entry_points=dict(
        console_scripts=["flint=flint.main:app"]
    ),
    install_requires=[
        'fastapi'
    ]
)

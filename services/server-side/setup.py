import re
from pathlib import Path

import setuptools

NAME = "fastdemo"
HERE = Path(__file__).parent


__version__ = re.findall(
    r"""__version__\s*=\s*['"](.*)['"]""",
    (HERE / "src" / NAME / "_version.py").read_text(),
)[0]


setuptools.setup(
    name=NAME,
    version=__version__,
    description="a fast api implementation demo",
    include_package_data=True,
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    zip_safe=False,
    install_requires=["fastapi"],
)

from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="moviepy_clipper",
    version="0.1.0",
    # license="ライセンス",
    description="Customize MoviePy",
    author="ryofujimotox",
    # author_email="contact@ryo1999.com",
    url="https://github.com/ryofujimotox/moviepy_clipper",
    # packages=find_packages(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=_requires_from_file("requirements.txt"),
    include_package_data=True,
)

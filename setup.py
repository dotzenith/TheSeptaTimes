import setuptools

with open("README.md", "r") as lg:
    long_description = lg.read()
with open("requirements.txt", "r") as rq:
    dependecies = rq.readlines()

current_version = "0.0.2"

setuptools.setup(
    name="RegionalSeptaTimes",
    version=current_version,
    author="Danshu Sharma",
    author_email="contact@danshu.dev",
    description="A Python package to get data about regional trains from the Septa API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZenithDS/RegionalSeptaTimes",
    packages=["RegionalSeptaTimes"],
    install_requires=dependecies,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "rst = RegionalSeptaTimes.__main__:main"
        ]
    }
)

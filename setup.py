import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="huobiApi",
    version="0.0.5",
    author="Jeremy.Zhang",
    author_email="zhangyue9306@gmail.com",
    description="helper functions of huobi rest api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MJeremy2017/HuobiApi",
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt').readlines(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
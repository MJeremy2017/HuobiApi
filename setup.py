import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autoetl",
    version="0.0.15",
    author="Jeremy.Zhang, Randen.Rosete",
    author_email="jeremy.zhang@grabtaxi.com",
    description="automate etl tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.myteksi.net/data-science/food/autoetl",
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt').readlines(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
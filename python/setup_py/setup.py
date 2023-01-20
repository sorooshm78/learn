from setuptools import setup, find_packages

setup(
    name='pack',
    version='0.0.0',
    author='sm',
    description='pack test for understand dist',
    packages=find_packages(exclude=["root"]),
    scripts=[
        'scripts/sprint',
    ],
    entry_points = {
        'console_scripts': [
            'joke=bar.bmain:main',
        ],
    }
)

# then in terminal you enter:
# $joke 
# result run function main in bmain file
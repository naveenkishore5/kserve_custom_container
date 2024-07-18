from setuptools import setup, find_packages

setup(
    name='your-package-name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas==2.1.0',
        'scikit-learn==1.4.2',
        'joblib==1.4.2',
        'numpy==1.26.4',
        'kserve==0.12.0',
        'ray==2.9.2'
    ],
)
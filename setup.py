from setuptools import setup, find_packages

setup(
    name='FastTtanslate',  
    version='0.0.1',  #
    author='Lencho',
    author_email='lenchomengistu100@gmail.com',
    description='A Simple Python Library Used To Translate Texts.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-metoo650/FastTtanslate',
    packages=find_packages(),  
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    install_requires=[
        'mtranslate',
    ],
)

from distutils.core import setup

setup(
    name="makikaka-covid19",
    packages=['makikaka-covid19'],
    version='0.1',
    license='MIT',
    description='covid19 timely stats',
    author='Mladen Tasevski',
    author_email="mladen.tasevski@gmail.com",
    url='https://github.com/makikaka/makikaka-covid19',
    download_url='https://github.com/makikaka/makikaka-covid19/archive/v_01.tar.gz',
    keywords=['covid19', 'http', 'sqlite'],
    install_requires=[
        'sys',
        'http.server',
        'os',
        'utils',
        'logging',
        'datetime',
        'python-memcached',
        'config-parser',
        'sys',
        'sqlite3',
        'json',
        'requests',
        're',
        'bs4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

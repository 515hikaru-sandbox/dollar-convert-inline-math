import setuptools 

setuptools.setup(
    name='do2im',
    version='0.0.1',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'do2im = do2im.main:main',
        ],
    },
)

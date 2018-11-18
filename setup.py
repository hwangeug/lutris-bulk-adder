from distutils.core import setup

setup(
    name = 'lutris-bulk-adder',
    packages = ['lutris_bulk_adder'],
    version = '0.1.4',
    license='MIT',
    description = 'Python script to bulk import a directory of ROM files into Lutris',
    author = 'Eugene Hwang',
    author_email = 'hwang.eug@gmail.com',
    url = 'https://github.com/hwangeug/lutris-bulk-adder',
    keywords = ['Lutris', 'ROMs', 'Emulation'],
    entry_points = {'console_scripts': ['lutris_bulk_adder=lutris_bulk_adder.lutris_bulk_adder:main']},
    install_requires = [
        'PyYAML'
    ]
)

from setuptools import setup

package_name = 'ffs'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='julian',
    maintainer_email='julian.w.francis@gmail.com',
    description='Fast FoundationStereo',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "ffs_node = ffs.ffs_node"
        ],
    },
)

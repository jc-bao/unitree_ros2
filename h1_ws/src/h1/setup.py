from setuptools import setup

package_name = 'h1'

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
    maintainer='tairanhe',
    maintainer_email='1065593158@qq.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'h1_sub = h1.h1_sub:main',
            'h1_fake_pub = h1.h1_fake_pub:main', 
            'h1_cmd = h1.h1_cmd:main'
        ],
    },
)
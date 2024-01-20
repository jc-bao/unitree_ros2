# H1 Commander Python Package

## Create a new node

```bash
cd h1_ws/src/h1/h1
touch h1_cmd.py
```

edit setup.py

```python
    entry_points={
        'console_scripts': [
            'h1_sub = h1.h1_sub:main',
            'h1_fake_pub = h1.h1_fake_pub:main'
            'h1_cmd = h1.h1_cmd:main'
        ],
    },
```

edit package.xml

```xml
  <build_depend>h1_msgs</build_depend>
  <exec_depend>h1_msgs</exec_depend>
```

build

```bash
cd h1_ws
colcon build --packages-select h1 --symlink-install
```

run h1_cmd

```bash
# source local setup.bash
source h1_ws/install/local_setup.bash

ros2 run h1 h1_cmd
```
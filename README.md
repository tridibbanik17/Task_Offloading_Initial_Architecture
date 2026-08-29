## Create the ROS2 package first: 

```bash
ros2 pkg create --build-type ament_python task_offloading
```

This generates all the scaffolding (package.xml, setup.py, __init__.py, etc.) so no need to hand-write them.

## Run the demo

```bash
cp -r "/mnt/c/Users/OWNER/OneDrive/Study-Fall2026/Task_Offloading_Architecture/task_offloading" ~/ros2_ws/src/
cd ~/ros2_ws
colcon build --packages-select task_offloading
source install/setup.bash
python3 -m task_offloading.demo
```

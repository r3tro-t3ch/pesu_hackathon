# Robofest 3.0 PESU Autonomous UGV

### Setup

Create a workspace 

`mkdir pesu_hackathon_ws`

Create a src directory in the workspace 

`cd pesu_hackthon_ws && mkdir src`

Clone the repository into src

`git clone https://github.com/r3tro-t3ch/pesu_hackathon.git src/`

Install turtlebot3 dependencies

`sudo apt install ros-humble-turtlebot3 ros-humble-turtlebot3-msgs -y`


Add env to spawn waffle_pi

`export TURTLEBOT3_MODEL=waffle_pi`

Go to pesu_hackthon_ws folder and build the workspace

`colcon build --symlink-install`

Source the bash script

`. ./install/setup.bash`

Launch the arena

`ros2 launch pesu_hackathon_ws arena.launch.py`

### Topics

RGB camera info

`/camera/camera_info`

Depth camera info

`/camera/depth/camera_info`

Depth image

`/camera/depth/image_raw`

RGB image

`/camera/image_raw`

Point cloud

`/camera/points`

Command velocity (use to move the robot - control output)

`/cmd_vel`

IMU sensor

`/imu`

Robot odometry

`/odom`

Laser scan

`/scan`

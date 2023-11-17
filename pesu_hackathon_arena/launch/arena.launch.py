from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackagePrefix
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration

import os


def generate_launch_description():

    ld = LaunchDescription()

    
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    x_pose = LaunchConfiguration('x_pose', default='0.0')
    y_pose = LaunchConfiguration('y_pose', default='0.0')
    package_name = 'pesu_hackathon_arena'


    launch_file_dir = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    arena_pkg_gazebo_ros = FindPackagePrefix(package=package_name).find(package_name).replace("install","src")

    sdf_path = "models/pesu_hackathon_arena_1/model.sdf"

    sdf_path_ros = os.path.join(arena_pkg_gazebo_ros, sdf_path)
    
    world = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'worlds',
        'empty_world.world'
    )

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    robot_state_publisher_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    spawn_turtlebot_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': x_pose,
            'y_pose': y_pose
        }.items()
    )

    spawner = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        output="screen",
        arguments=[
            "-file", sdf_path_ros,
            "-entity","arena_1","-x" ,"1.5", "-y","0.75"
        ]
    )


    ld.add_action(gzclient_cmd)
    ld.add_action(gzserver_cmd)
    ld.add_action(spawner)
    ld.add_action(robot_state_publisher_cmd)
    ld.add_action(spawn_turtlebot_cmd)

    return ld
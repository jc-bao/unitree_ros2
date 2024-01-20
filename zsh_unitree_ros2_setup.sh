#!usr/bin/zsh
echo "Setup unitree ros2 environment"
source /opt/ros/foxy/setup.zsh
source $HOME/workspace/foxy-unitree/unitree_ros2/cyclonedds_ws/install/setup.zsh
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI='<CycloneDDS><Domain><General><Interfaces>
                            <NetworkInterface name="eno1" priority="default" multicast="default" />
                        </Interfaces></General></Domain></CycloneDDS>'
cd h1_ws
source ./install/local_setup.zsh
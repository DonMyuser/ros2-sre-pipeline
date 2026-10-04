FROM ros:jazzy
SHELL ["/bin/bash", "-c"]
WORKDIR /ws
COPY src/ /ws/src/
RUN source /opt/ros/jazzy/setup.bash && colcon build
CMD ["bash", "-c", "source /opt/ros/jazzy/setup.bash && source /ws/install/setup.bash && ros2 run hello_world_node talker"]
# generated from ros_environment/env-hooks/1.ros_ip.sh.in

# If neither ROS_IP nor ROS_HOSTNAME are set, ROS uses what's returned by "hostname". Unfortunately, minimal OE doesn't arrange
# to resolve this to an IP address, so when this is the case, force ROS to use the loopback and require that users set one of
# ROS_IP or ROS_HOSTNAME if they want to talk to remote ROS nodes.
if [ -z "$ROS_IP$ROS_HOSTNAME" ] && ! hostname -i > /dev/null 2>/dev/null; then
    export ROS_IP="127.0.0.1"
fi

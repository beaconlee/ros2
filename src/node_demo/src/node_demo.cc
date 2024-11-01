#include <rclcpp/rclcpp.hpp>

int
main(int argc, char* argv[])
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("beacon");
  RCLCPP_INFO(node->get_logger(), "beacon day");
  // 用来清理资源
  rclcpp::shutdown();
  return 0;
}
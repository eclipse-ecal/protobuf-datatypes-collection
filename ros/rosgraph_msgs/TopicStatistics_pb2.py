# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ros/rosgraph_msgs/TopicStatistics.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ros import builtins_pb2 as ros_dot_builtins__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'ros/rosgraph_msgs/TopicStatistics.proto\x12\x11ros.rosgraph_msgs\x1a\x12ros/builtins.proto\"\xa7\x03\n\x0fTopicStatistics\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x10\n\x08node_pub\x18\x02 \x01(\t\x12\x10\n\x08node_sub\x18\x03 \x01(\t\x12\x1f\n\x0cwindow_start\x18\x04 \x01(\x0b\x32\t.ros.Time\x12\x1e\n\x0bwindow_stop\x18\x05 \x01(\x0b\x32\t.ros.Time\x12\x16\n\x0e\x64\x65livered_msgs\x18\x06 \x01(\x05\x12\x14\n\x0c\x64ropped_msgs\x18\x07 \x01(\x05\x12\x0f\n\x07traffic\x18\x08 \x01(\x05\x12\"\n\x0bperiod_mean\x18\t \x01(\x0b\x32\r.ros.Duration\x12$\n\rperiod_stddev\x18\n \x01(\x0b\x32\r.ros.Duration\x12!\n\nperiod_max\x18\x0b \x01(\x0b\x32\r.ros.Duration\x12%\n\x0estamp_age_mean\x18\x0c \x01(\x0b\x32\r.ros.Duration\x12\'\n\x10stamp_age_stddev\x18\r \x01(\x0b\x32\r.ros.Duration\x12$\n\rstamp_age_max\x18\x0e \x01(\x0b\x32\r.ros.Durationb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ros.rosgraph_msgs.TopicStatistics_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TOPICSTATISTICS._serialized_start=83
  _TOPICSTATISTICS._serialized_end=506
# @@protoc_insertion_point(module_scope)

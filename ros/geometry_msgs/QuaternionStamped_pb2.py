# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ros/geometry_msgs/QuaternionStamped.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ros.geometry_msgs import Quaternion_pb2 as ros_dot_geometry__msgs_dot_Quaternion__pb2
from ros.std_msgs import Header_pb2 as ros_dot_std__msgs_dot_Header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)ros/geometry_msgs/QuaternionStamped.proto\x12\x11ros.geometry_msgs\x1a\"ros/geometry_msgs/Quaternion.proto\x1a\x19ros/std_msgs/Header.proto\"l\n\x11QuaternionStamped\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.ros.std_msgs.Header\x12\x31\n\nquaternion\x18\x02 \x01(\x0b\x32\x1d.ros.geometry_msgs.Quaternionb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ros.geometry_msgs.QuaternionStamped_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUATERNIONSTAMPED._serialized_start=127
  _QUATERNIONSTAMPED._serialized_end=235
# @@protoc_insertion_point(module_scope)

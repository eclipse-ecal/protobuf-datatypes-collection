# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ros/rosgraph_msgs/Log.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ros.std_msgs import Header_pb2 as ros_dot_std__msgs_dot_Header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bros/rosgraph_msgs/Log.proto\x12\x11ros.rosgraph_msgs\x1a\x19ros/std_msgs/Header.proto\"\x93\x01\n\x03Log\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.ros.std_msgs.Header\x12\r\n\x05level\x18\x02 \x01(\x11\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0b\n\x03msg\x18\x04 \x01(\t\x12\x0c\n\x04\x66ile\x18\x05 \x01(\t\x12\x10\n\x08\x66unction\x18\x06 \x01(\t\x12\x0c\n\x04line\x18\x07 \x01(\r\x12\x0e\n\x06topics\x18\x08 \x03(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ros.rosgraph_msgs.Log_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOG._serialized_start=78
  _LOG._serialized_end=225
# @@protoc_insertion_point(module_scope)

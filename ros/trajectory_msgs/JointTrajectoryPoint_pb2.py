# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ros/trajectory_msgs/JointTrajectoryPoint.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ros import builtins_pb2 as ros_dot_builtins__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.ros/trajectory_msgs/JointTrajectoryPoint.proto\x12\x13ros.trajectory_msgs\x1a\x12ros/builtins.proto\"\x8c\x01\n\x14JointTrajectoryPoint\x12\x11\n\tpositions\x18\x01 \x03(\x01\x12\x12\n\nvelocities\x18\x02 \x03(\x01\x12\x15\n\raccelerations\x18\x03 \x03(\x01\x12\x0e\n\x06\x65\x66\x66ort\x18\x04 \x03(\x01\x12&\n\x0ftime_from_start\x18\x05 \x01(\x0b\x32\r.ros.Durationb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ros.trajectory_msgs.JointTrajectoryPoint_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _JOINTTRAJECTORYPOINT._serialized_start=92
  _JOINTTRAJECTORYPOINT._serialized_end=232
# @@protoc_insertion_point(module_scope)

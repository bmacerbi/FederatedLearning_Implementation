# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fed_grpc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x66\x65\x64_grpc.proto\x12\x04main\"5\n\x0cregisterArgs\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x0b\n\x03\x63id\x18\x03 \x01(\t\"5\n\x0bregisterOut\x12\x17\n\x0f\x63onnectedClient\x18\x01 \x01(\x08\x12\r\n\x05round\x18\x02 \x01(\x05\"\x1a\n\nsampleSize\x12\x0c\n\x04size\x18\x01 \x01(\x05\"\x17\n\x08\x61\x63\x63uracy\x12\x0b\n\x03\x61\x63\x63\x18\x01 \x01(\x02\"\x1c\n\nweightList\x12\x0e\n\x06weight\x18\x01 \x03(\x02\"\x06\n\x04void2\xde\x01\n\x10\x46\x65\x64\x65ratedService\x12\x37\n\x0e\x63lientRegister\x12\x12.main.registerArgs\x1a\x11.main.registerOut\x12-\n\rstartLearning\x12\n.main.void\x1a\x10.main.weightList\x12-\n\rgetSampleSize\x12\n.main.void\x1a\x10.main.sampleSize\x12\x33\n\x0fmodelValidation\x12\x10.main.weightList\x1a\x0e.main.accuracyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fed_grpc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERARGS._serialized_start=24
  _REGISTERARGS._serialized_end=77
  _REGISTEROUT._serialized_start=79
  _REGISTEROUT._serialized_end=132
  _SAMPLESIZE._serialized_start=134
  _SAMPLESIZE._serialized_end=160
  _ACCURACY._serialized_start=162
  _ACCURACY._serialized_end=185
  _WEIGHTLIST._serialized_start=187
  _WEIGHTLIST._serialized_end=215
  _VOID._serialized_start=217
  _VOID._serialized_end=223
  _FEDERATEDSERVICE._serialized_start=226
  _FEDERATEDSERVICE._serialized_end=448
# @@protoc_insertion_point(module_scope)

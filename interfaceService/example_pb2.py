# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\x12\x07\x65xample\"/\n\x11HelloWorldRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\"\n\x12HelloWorldResponse\x12\x0c\n\x04text\x18\x01 \x01(\t2U\n\x0cHelloService\x12\x45\n\nHelloWorld\x12\x1a.example.HelloWorldRequest\x1a\x1b.example.HelloWorldResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOWORLDREQUEST._serialized_start=26
  _HELLOWORLDREQUEST._serialized_end=73
  _HELLOWORLDRESPONSE._serialized_start=75
  _HELLOWORLDRESPONSE._serialized_end=109
  _HELLOSERVICE._serialized_start=111
  _HELLOSERVICE._serialized_end=196
# @@protoc_insertion_point(module_scope)
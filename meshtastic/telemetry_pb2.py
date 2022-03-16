# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: telemetry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='telemetry.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z!github.com/meshtastic/gomeshproto',
  serialized_pb=b'\n\x0ftelemetry.proto\"\x92\x01\n\tTelemetry\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\x19\n\x11relative_humidity\x18\x02 \x01(\x02\x12\x1b\n\x13\x62\x61rometric_pressure\x18\x03 \x01(\x02\x12\x16\n\x0egas_resistance\x18\x04 \x01(\x02\x12\x0f\n\x07voltage\x18\x05 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x06 \x01(\x02\x42#Z!github.com/meshtastic/gomeshprotob\x06proto3'
)




_TELEMETRY = _descriptor.Descriptor(
  name='Telemetry',
  full_name='Telemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperature', full_name='Telemetry.temperature', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_humidity', full_name='Telemetry.relative_humidity', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='barometric_pressure', full_name='Telemetry.barometric_pressure', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_resistance', full_name='Telemetry.gas_resistance', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voltage', full_name='Telemetry.voltage', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current', full_name='Telemetry.current', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=166,
)

DESCRIPTOR.message_types_by_name['Telemetry'] = _TELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Telemetry = _reflection.GeneratedProtocolMessageType('Telemetry', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRY,
  '__module__' : 'telemetry_pb2'
  # @@protoc_insertion_point(class_scope:Telemetry)
  })
_sym_db.RegisterMessage(Telemetry)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
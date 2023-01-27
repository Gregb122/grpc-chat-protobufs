# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat_service/v1/chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63hat_service/v1/chat.proto\x12\x0f\x63hat_service.v1\"\x14\n\x12GetAllUsersRequest\"F\n\x13GetAllUsersResponse\x12/\n\x05users\x18\x01 \x03(\x0b\x32\x19.chat_service.v1.UserInfoR\x05users\"<\n\x16RecieveMessagesRequest\x12\"\n\rto_user_login\x18\x01 \x01(\tR\x0btoUserLogin\"M\n\x17RecieveMessagesResponse\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.chat_service.v1.MessageR\x07message\"H\n\x12SendMessageRequest\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.chat_service.v1.MessageR\x07message\"\x15\n\x13SendMessageResponse\"=\n\x08UserInfo\x12\x14\n\x05login\x18\x01 \x01(\tR\x05login\x12\x1b\n\tfull_name\x18\x02 \x01(\tR\x08\x66ullName\"?\n\x0bMessageBody\x12\x12\n\x04\x62ody\x18\x01 \x01(\tR\x04\x62ody\x12\x1c\n\ttimestamp\x18\x02 \x01(\tR\ttimestamp\"\x87\x01\n\x07Message\x12&\n\x0f\x66rom_user_login\x18\x01 \x01(\tR\rfromUserLogin\x12\"\n\rto_user_login\x18\x02 \x01(\tR\x0btoUserLogin\x12\x30\n\x04\x62ody\x18\x03 \x01(\x0b\x32\x1c.chat_service.v1.MessageBodyR\x04\x62ody\"\xbb\x01\n\x0c\x45tcdUserInfo\x12\x36\n\tuser_info\x18\x01 \x01(\x0b\x32\x19.chat_service.v1.UserInfoR\x08userInfo\x12\x1b\n\tis_active\x18\x02 \x01(\x08R\x08isActive\x12\'\n\x0fhashed_password\x18\x03 \x01(\tR\x0ehashedPassword\x12-\n\x12register_timestamp\x18\x04 \x01(\tR\x11registerTimestamp\"D\n\x10LoginUserRequest\x12\x14\n\x05login\x18\x01 \x01(\tR\x05login\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password\"\x13\n\x11LoginUserResponse\"i\n\x13RegisterUserRequest\x12\x36\n\tuser_info\x18\x01 \x01(\x0b\x32\x19.chat_service.v1.UserInfoR\x08userInfo\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password\"\x16\n\x14RegisterUserResponse2\xda\x03\n\x0b\x43hatService\x12X\n\x0bGetAllUsers\x12#.chat_service.v1.GetAllUsersRequest\x1a$.chat_service.v1.GetAllUsersResponse\x12\x66\n\x0fRecieveMessages\x12\'.chat_service.v1.RecieveMessagesRequest\x1a(.chat_service.v1.RecieveMessagesResponse0\x01\x12X\n\x0bSendMessage\x12#.chat_service.v1.SendMessageRequest\x1a$.chat_service.v1.SendMessageResponse\x12[\n\x0cRegisterUser\x12$.chat_service.v1.RegisterUserRequest\x1a%.chat_service.v1.RegisterUserResponse\x12R\n\tLoginUser\x12!.chat_service.v1.LoginUserRequest\x1a\".chat_service.v1.LoginUserResponseB\xc1\x01\n\x13\x63om.chat_service.v1B\tChatProtoP\x01ZFgithub.com/gregb122/grpc-chat-protobufs/chat_service/v1;chat_servicev1\xa2\x02\x03\x43XX\xaa\x02\x0e\x43hatService.V1\xca\x02\x0e\x43hatService\\V1\xe2\x02\x1a\x43hatService\\V1\\GPBMetadata\xea\x02\x0f\x43hatService::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_service.v1.chat_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.chat_service.v1B\tChatProtoP\001ZFgithub.com/gregb122/grpc-chat-protobufs/chat_service/v1;chat_servicev1\242\002\003CXX\252\002\016ChatService.V1\312\002\016ChatService\\V1\342\002\032ChatService\\V1\\GPBMetadata\352\002\017ChatService::V1'
  _GETALLUSERSREQUEST._serialized_start=47
  _GETALLUSERSREQUEST._serialized_end=67
  _GETALLUSERSRESPONSE._serialized_start=69
  _GETALLUSERSRESPONSE._serialized_end=139
  _RECIEVEMESSAGESREQUEST._serialized_start=141
  _RECIEVEMESSAGESREQUEST._serialized_end=201
  _RECIEVEMESSAGESRESPONSE._serialized_start=203
  _RECIEVEMESSAGESRESPONSE._serialized_end=280
  _SENDMESSAGEREQUEST._serialized_start=282
  _SENDMESSAGEREQUEST._serialized_end=354
  _SENDMESSAGERESPONSE._serialized_start=356
  _SENDMESSAGERESPONSE._serialized_end=377
  _USERINFO._serialized_start=379
  _USERINFO._serialized_end=440
  _MESSAGEBODY._serialized_start=442
  _MESSAGEBODY._serialized_end=505
  _MESSAGE._serialized_start=508
  _MESSAGE._serialized_end=643
  _ETCDUSERINFO._serialized_start=646
  _ETCDUSERINFO._serialized_end=833
  _LOGINUSERREQUEST._serialized_start=835
  _LOGINUSERREQUEST._serialized_end=903
  _LOGINUSERRESPONSE._serialized_start=905
  _LOGINUSERRESPONSE._serialized_end=924
  _REGISTERUSERREQUEST._serialized_start=926
  _REGISTERUSERREQUEST._serialized_end=1031
  _REGISTERUSERRESPONSE._serialized_start=1033
  _REGISTERUSERRESPONSE._serialized_end=1055
  _CHATSERVICE._serialized_start=1058
  _CHATSERVICE._serialized_end=1532
# @@protoc_insertion_point(module_scope)
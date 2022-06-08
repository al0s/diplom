# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/box_predictor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_detection.protos import hyperparams_pb2 as object__detection_dot_protos_dot_hyperparams__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/box_predictor.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n+object_detection/protos/box_predictor.proto\x12\x17object_detection.protos\x1a)object_detection/protos/hyperparams.proto\"\x90\x03\n\x0c\x42oxPredictor\x12Y\n\x1b\x63onvolutional_box_predictor\x18\x01 \x01(\x0b\x32\x32.object_detection.protos.ConvolutionalBoxPredictorH\x00\x12P\n\x17mask_rcnn_box_predictor\x18\x02 \x01(\x0b\x32-.object_detection.protos.MaskRCNNBoxPredictorH\x00\x12G\n\x12rfcn_box_predictor\x18\x03 \x01(\x0b\x32).object_detection.protos.RfcnBoxPredictorH\x00\x12s\n)weight_shared_convolutional_box_predictor\x18\x04 \x01(\x0b\x32>.object_detection.protos.WeightSharedConvolutionalBoxPredictorH\x00\x42\x15\n\x13\x62ox_predictor_oneof\"c\n\x08MaskHead\x12\x17\n\x0bmask_height\x18\x01 \x01(\x05:\x02\x31\x35\x12\x16\n\nmask_width\x18\x02 \x01(\x05:\x02\x31\x35\x12&\n\x18masks_are_class_agnostic\x18\x03 \x01(\x08:\x04true\"\xc6\x03\n\x19\x43onvolutionalBoxPredictor\x12>\n\x10\x63onv_hyperparams\x18\x01 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12\x14\n\tmin_depth\x18\x02 \x01(\x05:\x01\x30\x12\x14\n\tmax_depth\x18\x03 \x01(\x05:\x01\x30\x12&\n\x1bnum_layers_before_predictor\x18\x04 \x01(\x05:\x01\x30\x12\x19\n\x0buse_dropout\x18\x05 \x01(\x08:\x04true\x12%\n\x18\x64ropout_keep_probability\x18\x06 \x01(\x02:\x03\x30.8\x12\x16\n\x0bkernel_size\x18\x07 \x01(\x05:\x01\x31\x12\x18\n\rbox_code_size\x18\x08 \x01(\x05:\x01\x34\x12&\n\x17\x61pply_sigmoid_to_scores\x18\t \x01(\x08:\x05\x66\x61lse\x12%\n\x1a\x63lass_prediction_bias_init\x18\n \x01(\x02:\x01\x30\x12\x1c\n\ruse_depthwise\x18\x0b \x01(\x08:\x05\x66\x61lse\x12\x34\n\tmask_head\x18\x0c \x01(\x0b\x32!.object_detection.protos.MaskHead\"\x82\x06\n%WeightSharedConvolutionalBoxPredictor\x12>\n\x10\x63onv_hyperparams\x18\x01 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12&\n\x1bnum_layers_before_predictor\x18\x04 \x01(\x05:\x01\x30\x12\x10\n\x05\x64\x65pth\x18\x02 \x01(\x05:\x01\x30\x12\x16\n\x0bkernel_size\x18\x07 \x01(\x05:\x01\x33\x12\x18\n\rbox_code_size\x18\x08 \x01(\x05:\x01\x34\x12%\n\x1a\x63lass_prediction_bias_init\x18\n \x01(\x02:\x01\x30\x12\x1a\n\x0buse_dropout\x18\x0b \x01(\x08:\x05\x66\x61lse\x12%\n\x18\x64ropout_keep_probability\x18\x0c \x01(\x02:\x03\x30.8\x12%\n\x16share_prediction_tower\x18\r \x01(\x08:\x05\x66\x61lse\x12\x1c\n\ruse_depthwise\x18\x0e \x01(\x08:\x05\x66\x61lse\x12\x34\n\tmask_head\x18\x0f \x01(\x0b\x32!.object_detection.protos.MaskHead\x12p\n\x0fscore_converter\x18\x10 \x01(\x0e\x32M.object_detection.protos.WeightSharedConvolutionalBoxPredictor.ScoreConverter:\x08IDENTITY\x12v\n\x18\x62ox_encodings_clip_range\x18\x11 \x01(\x0b\x32T.object_detection.protos.WeightSharedConvolutionalBoxPredictor.BoxEncodingsClipRange\x1a\x31\n\x15\x42oxEncodingsClipRange\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\"+\n\x0eScoreConverter\x12\x0c\n\x08IDENTITY\x10\x00\x12\x0b\n\x07SIGMOID\x10\x01\"\xbf\x04\n\x14MaskRCNNBoxPredictor\x12<\n\x0e\x66\x63_hyperparams\x18\x01 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12\x1a\n\x0buse_dropout\x18\x02 \x01(\x08:\x05\x66\x61lse\x12%\n\x18\x64ropout_keep_probability\x18\x03 \x01(\x02:\x03\x30.5\x12\x18\n\rbox_code_size\x18\x04 \x01(\x05:\x01\x34\x12>\n\x10\x63onv_hyperparams\x18\x05 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12%\n\x16predict_instance_masks\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\'\n\x1amask_prediction_conv_depth\x18\x07 \x01(\x05:\x03\x32\x35\x36\x12 \n\x11predict_keypoints\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\x17\n\x0bmask_height\x18\t \x01(\x05:\x02\x31\x35\x12\x16\n\nmask_width\x18\n \x01(\x05:\x02\x31\x35\x12*\n\x1fmask_prediction_num_conv_layers\x18\x0b \x01(\x05:\x01\x32\x12\'\n\x18masks_are_class_agnostic\x18\x0c \x01(\x08:\x05\x66\x61lse\x12\'\n\x18share_box_across_classes\x18\r \x01(\x08:\x05\x66\x61lse\x12+\n\x1c\x63onvolve_then_upsample_masks\x18\x0e \x01(\x08:\x05\x66\x61lse\"\xf9\x01\n\x10RfcnBoxPredictor\x12>\n\x10\x63onv_hyperparams\x18\x01 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12\"\n\x17num_spatial_bins_height\x18\x02 \x01(\x05:\x01\x33\x12!\n\x16num_spatial_bins_width\x18\x03 \x01(\x05:\x01\x33\x12\x13\n\x05\x64\x65pth\x18\x04 \x01(\x05:\x04\x31\x30\x32\x34\x12\x18\n\rbox_code_size\x18\x05 \x01(\x05:\x01\x34\x12\x17\n\x0b\x63rop_height\x18\x06 \x01(\x05:\x02\x31\x32\x12\x16\n\ncrop_width\x18\x07 \x01(\x05:\x02\x31\x32')
  ,
  dependencies=[object__detection_dot_protos_dot_hyperparams__pb2.DESCRIPTOR,])



_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_SCORECONVERTER = _descriptor.EnumDescriptor(
  name='ScoreConverter',
  full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.ScoreConverter',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDENTITY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGMOID', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1804,
  serialized_end=1847,
)
_sym_db.RegisterEnumDescriptor(_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_SCORECONVERTER)


_BOXPREDICTOR = _descriptor.Descriptor(
  name='BoxPredictor',
  full_name='object_detection.protos.BoxPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='convolutional_box_predictor', full_name='object_detection.protos.BoxPredictor.convolutional_box_predictor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_rcnn_box_predictor', full_name='object_detection.protos.BoxPredictor.mask_rcnn_box_predictor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rfcn_box_predictor', full_name='object_detection.protos.BoxPredictor.rfcn_box_predictor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_shared_convolutional_box_predictor', full_name='object_detection.protos.BoxPredictor.weight_shared_convolutional_box_predictor', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='box_predictor_oneof', full_name='object_detection.protos.BoxPredictor.box_predictor_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=116,
  serialized_end=516,
)


_MASKHEAD = _descriptor.Descriptor(
  name='MaskHead',
  full_name='object_detection.protos.MaskHead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mask_height', full_name='object_detection.protos.MaskHead.mask_height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=15,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_width', full_name='object_detection.protos.MaskHead.mask_width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=15,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='masks_are_class_agnostic', full_name='object_detection.protos.MaskHead.masks_are_class_agnostic', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=518,
  serialized_end=617,
)


_CONVOLUTIONALBOXPREDICTOR = _descriptor.Descriptor(
  name='ConvolutionalBoxPredictor',
  full_name='object_detection.protos.ConvolutionalBoxPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conv_hyperparams', full_name='object_detection.protos.ConvolutionalBoxPredictor.conv_hyperparams', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_depth', full_name='object_detection.protos.ConvolutionalBoxPredictor.min_depth', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_depth', full_name='object_detection.protos.ConvolutionalBoxPredictor.max_depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_layers_before_predictor', full_name='object_detection.protos.ConvolutionalBoxPredictor.num_layers_before_predictor', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_dropout', full_name='object_detection.protos.ConvolutionalBoxPredictor.use_dropout', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropout_keep_probability', full_name='object_detection.protos.ConvolutionalBoxPredictor.dropout_keep_probability', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.8),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kernel_size', full_name='object_detection.protos.ConvolutionalBoxPredictor.kernel_size', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_code_size', full_name='object_detection.protos.ConvolutionalBoxPredictor.box_code_size', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apply_sigmoid_to_scores', full_name='object_detection.protos.ConvolutionalBoxPredictor.apply_sigmoid_to_scores', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_prediction_bias_init', full_name='object_detection.protos.ConvolutionalBoxPredictor.class_prediction_bias_init', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_depthwise', full_name='object_detection.protos.ConvolutionalBoxPredictor.use_depthwise', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_head', full_name='object_detection.protos.ConvolutionalBoxPredictor.mask_head', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=1074,
)


_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_BOXENCODINGSCLIPRANGE = _descriptor.Descriptor(
  name='BoxEncodingsClipRange',
  full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.BoxEncodingsClipRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.BoxEncodingsClipRange.min', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.BoxEncodingsClipRange.max', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1753,
  serialized_end=1802,
)

_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR = _descriptor.Descriptor(
  name='WeightSharedConvolutionalBoxPredictor',
  full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conv_hyperparams', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.conv_hyperparams', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_layers_before_predictor', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.num_layers_before_predictor', index=1,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depth', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.depth', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kernel_size', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.kernel_size', index=3,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_code_size', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.box_code_size', index=4,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_prediction_bias_init', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.class_prediction_bias_init', index=5,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_dropout', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.use_dropout', index=6,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropout_keep_probability', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.dropout_keep_probability', index=7,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.8),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='share_prediction_tower', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.share_prediction_tower', index=8,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_depthwise', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.use_depthwise', index=9,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_head', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.mask_head', index=10,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score_converter', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.score_converter', index=11,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_encodings_clip_range', full_name='object_detection.protos.WeightSharedConvolutionalBoxPredictor.box_encodings_clip_range', index=12,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_BOXENCODINGSCLIPRANGE, ],
  enum_types=[
    _WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_SCORECONVERTER,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1077,
  serialized_end=1847,
)


_MASKRCNNBOXPREDICTOR = _descriptor.Descriptor(
  name='MaskRCNNBoxPredictor',
  full_name='object_detection.protos.MaskRCNNBoxPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fc_hyperparams', full_name='object_detection.protos.MaskRCNNBoxPredictor.fc_hyperparams', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_dropout', full_name='object_detection.protos.MaskRCNNBoxPredictor.use_dropout', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropout_keep_probability', full_name='object_detection.protos.MaskRCNNBoxPredictor.dropout_keep_probability', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_code_size', full_name='object_detection.protos.MaskRCNNBoxPredictor.box_code_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conv_hyperparams', full_name='object_detection.protos.MaskRCNNBoxPredictor.conv_hyperparams', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predict_instance_masks', full_name='object_detection.protos.MaskRCNNBoxPredictor.predict_instance_masks', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_prediction_conv_depth', full_name='object_detection.protos.MaskRCNNBoxPredictor.mask_prediction_conv_depth', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predict_keypoints', full_name='object_detection.protos.MaskRCNNBoxPredictor.predict_keypoints', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_height', full_name='object_detection.protos.MaskRCNNBoxPredictor.mask_height', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=15,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_width', full_name='object_detection.protos.MaskRCNNBoxPredictor.mask_width', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=15,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_prediction_num_conv_layers', full_name='object_detection.protos.MaskRCNNBoxPredictor.mask_prediction_num_conv_layers', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='masks_are_class_agnostic', full_name='object_detection.protos.MaskRCNNBoxPredictor.masks_are_class_agnostic', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='share_box_across_classes', full_name='object_detection.protos.MaskRCNNBoxPredictor.share_box_across_classes', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='convolve_then_upsample_masks', full_name='object_detection.protos.MaskRCNNBoxPredictor.convolve_then_upsample_masks', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1850,
  serialized_end=2425,
)


_RFCNBOXPREDICTOR = _descriptor.Descriptor(
  name='RfcnBoxPredictor',
  full_name='object_detection.protos.RfcnBoxPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conv_hyperparams', full_name='object_detection.protos.RfcnBoxPredictor.conv_hyperparams', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_spatial_bins_height', full_name='object_detection.protos.RfcnBoxPredictor.num_spatial_bins_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_spatial_bins_width', full_name='object_detection.protos.RfcnBoxPredictor.num_spatial_bins_width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depth', full_name='object_detection.protos.RfcnBoxPredictor.depth', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1024,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_code_size', full_name='object_detection.protos.RfcnBoxPredictor.box_code_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crop_height', full_name='object_detection.protos.RfcnBoxPredictor.crop_height', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=12,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crop_width', full_name='object_detection.protos.RfcnBoxPredictor.crop_width', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=12,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2428,
  serialized_end=2677,
)

_BOXPREDICTOR.fields_by_name['convolutional_box_predictor'].message_type = _CONVOLUTIONALBOXPREDICTOR
_BOXPREDICTOR.fields_by_name['mask_rcnn_box_predictor'].message_type = _MASKRCNNBOXPREDICTOR
_BOXPREDICTOR.fields_by_name['rfcn_box_predictor'].message_type = _RFCNBOXPREDICTOR
_BOXPREDICTOR.fields_by_name['weight_shared_convolutional_box_predictor'].message_type = _WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR
_BOXPREDICTOR.oneofs_by_name['box_predictor_oneof'].fields.append(
  _BOXPREDICTOR.fields_by_name['convolutional_box_predictor'])
_BOXPREDICTOR.fields_by_name['convolutional_box_predictor'].containing_oneof = _BOXPREDICTOR.oneofs_by_name['box_predictor_oneof']
_BOXPREDICTOR.oneofs_by_name['box_predictor_oneof'].fields.append(
  _BOXPREDICTOR.fields_by_name['mask_rcnn_box_predictor'])
_BOXPREDICTOR.fields_by_name['mask_rcnn_box_predictor'].containing_oneof = _BOXPREDICTOR.oneofs_by_name['box_predictor_oneof']
_BOXPREDICTOR.oneofs_by_name['box_predictor_oneof'].fields.append(
  _BOXPREDICTOR.fields_by_name['rfcn_box_predictor'])
_BOXPREDICTOR.fields_by_name['rfcn_box_predictor'].containing_oneof = _BOXPREDICTOR.oneofs_by_name['box_predictor_oneof']
_BOXPREDICTOR.oneofs_by_name['box_predictor_oneof'].fields.append(
  _BOXPREDICTOR.fields_by_name['weight_shared_convolutional_box_predictor'])
_BOXPREDICTOR.fields_by_name['weight_shared_convolutional_box_predictor'].containing_oneof = _BOXPREDICTOR.oneofs_by_name['box_predictor_oneof']
_CONVOLUTIONALBOXPREDICTOR.fields_by_name['conv_hyperparams'].message_type = object__detection_dot_protos_dot_hyperparams__pb2._HYPERPARAMS
_CONVOLUTIONALBOXPREDICTOR.fields_by_name['mask_head'].message_type = _MASKHEAD
_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_BOXENCODINGSCLIPRANGE.containing_type = _WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR
_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR.fields_by_name['conv_hyperparams'].message_type = object__detection_dot_protos_dot_hyperparams__pb2._HYPERPARAMS
_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR.fields_by_name['mask_head'].message_type = _MASKHEAD
_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR.fields_by_name['score_converter'].enum_type = _WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_SCORECONVERTER
_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR.fields_by_name['box_encodings_clip_range'].message_type = _WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_BOXENCODINGSCLIPRANGE
_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_SCORECONVERTER.containing_type = _WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR
_MASKRCNNBOXPREDICTOR.fields_by_name['fc_hyperparams'].message_type = object__detection_dot_protos_dot_hyperparams__pb2._HYPERPARAMS
_MASKRCNNBOXPREDICTOR.fields_by_name['conv_hyperparams'].message_type = object__detection_dot_protos_dot_hyperparams__pb2._HYPERPARAMS
_RFCNBOXPREDICTOR.fields_by_name['conv_hyperparams'].message_type = object__detection_dot_protos_dot_hyperparams__pb2._HYPERPARAMS
DESCRIPTOR.message_types_by_name['BoxPredictor'] = _BOXPREDICTOR
DESCRIPTOR.message_types_by_name['MaskHead'] = _MASKHEAD
DESCRIPTOR.message_types_by_name['ConvolutionalBoxPredictor'] = _CONVOLUTIONALBOXPREDICTOR
DESCRIPTOR.message_types_by_name['WeightSharedConvolutionalBoxPredictor'] = _WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR
DESCRIPTOR.message_types_by_name['MaskRCNNBoxPredictor'] = _MASKRCNNBOXPREDICTOR
DESCRIPTOR.message_types_by_name['RfcnBoxPredictor'] = _RFCNBOXPREDICTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BoxPredictor = _reflection.GeneratedProtocolMessageType('BoxPredictor', (_message.Message,), dict(
  DESCRIPTOR = _BOXPREDICTOR,
  __module__ = 'object_detection.protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.BoxPredictor)
  ))
_sym_db.RegisterMessage(BoxPredictor)

MaskHead = _reflection.GeneratedProtocolMessageType('MaskHead', (_message.Message,), dict(
  DESCRIPTOR = _MASKHEAD,
  __module__ = 'object_detection.protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.MaskHead)
  ))
_sym_db.RegisterMessage(MaskHead)

ConvolutionalBoxPredictor = _reflection.GeneratedProtocolMessageType('ConvolutionalBoxPredictor', (_message.Message,), dict(
  DESCRIPTOR = _CONVOLUTIONALBOXPREDICTOR,
  __module__ = 'object_detection.protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ConvolutionalBoxPredictor)
  ))
_sym_db.RegisterMessage(ConvolutionalBoxPredictor)

WeightSharedConvolutionalBoxPredictor = _reflection.GeneratedProtocolMessageType('WeightSharedConvolutionalBoxPredictor', (_message.Message,), dict(

  BoxEncodingsClipRange = _reflection.GeneratedProtocolMessageType('BoxEncodingsClipRange', (_message.Message,), dict(
    DESCRIPTOR = _WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_BOXENCODINGSCLIPRANGE,
    __module__ = 'object_detection.protos.box_predictor_pb2'
    # @@protoc_insertion_point(class_scope:object_detection.protos.WeightSharedConvolutionalBoxPredictor.BoxEncodingsClipRange)
    ))
  ,
  DESCRIPTOR = _WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR,
  __module__ = 'object_detection.protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.WeightSharedConvolutionalBoxPredictor)
  ))
_sym_db.RegisterMessage(WeightSharedConvolutionalBoxPredictor)
_sym_db.RegisterMessage(WeightSharedConvolutionalBoxPredictor.BoxEncodingsClipRange)

MaskRCNNBoxPredictor = _reflection.GeneratedProtocolMessageType('MaskRCNNBoxPredictor', (_message.Message,), dict(
  DESCRIPTOR = _MASKRCNNBOXPREDICTOR,
  __module__ = 'object_detection.protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.MaskRCNNBoxPredictor)
  ))
_sym_db.RegisterMessage(MaskRCNNBoxPredictor)

RfcnBoxPredictor = _reflection.GeneratedProtocolMessageType('RfcnBoxPredictor', (_message.Message,), dict(
  DESCRIPTOR = _RFCNBOXPREDICTOR,
  __module__ = 'object_detection.protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RfcnBoxPredictor)
  ))
_sym_db.RegisterMessage(RfcnBoxPredictor)


# @@protoc_insertion_point(module_scope)

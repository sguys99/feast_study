# importing dependencies
from google.protobuf.duration_pb2 import Duration
from feast import Entity, Feature, FeatureView, FileSource, ValueType


# Declaring and entity for the dataset
patient = Entity(
    name="patient_id",
    value_type=ValueType.INT64,
    description="The ID of the patient"
)


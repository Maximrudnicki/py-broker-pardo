import datetime
from google.protobuf.timestamp_pb2 import Timestamp

def timestamp_to_datetime(timestamp: Timestamp) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(timestamp.seconds + timestamp.nanos / 1e9)
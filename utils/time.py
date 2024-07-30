import datetime
from google.protobuf.timestamp_pb2 import Timestamp

def timestamp_to_datetime(timestamp: Timestamp) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(timestamp.seconds + timestamp.nanos / 1e9)

def datetime_to_timestamp(dt: datetime.datetime) -> Timestamp:
    timestamp = Timestamp()
    timestamp.seconds = int(dt.timestamp())
    timestamp.nanos = int((dt.timestamp() - timestamp.seconds) * 1e9)
    return {"seconds": timestamp.seconds, "nanos": timestamp.nanos}
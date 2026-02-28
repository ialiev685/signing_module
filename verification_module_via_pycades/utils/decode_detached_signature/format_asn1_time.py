from datetime import datetime
from pyasn1.type.useful import UTCTime

path_signature = "src/test_signature/test_detached_signature.sig"


def format_asn1_time(time_str: UTCTime):
    dt = datetime.strptime(str(time_str), "%y%m%d%H%M%SZ")
    return dt.strftime("%d.%m.%Y %H:%M")

### General helper methods that don't fit anywhere else

from simpleflake import simpleflake, parse_simpleflake
import base64

def flake_id():
    """Generate a new random Flake ID"""
    return simpleflake()

def printable_id(fid):
    """Create a printable string for a Flake ID: 12 URL-safe characters"""
    return base64.urlsafe_b64encode(fid.to_bytes(9, 'big')).decode()

def decode_printable_id(id_str):
    """Get the integer value from a Flake ID's string representation"""
    return int.from_bytes(base64.urlsafe_b64decode(id_str), 'big')

def id_timestamp(fid):
    """Get the timestamp from a Flake ID"""
    return parse_simpleflake(fid)
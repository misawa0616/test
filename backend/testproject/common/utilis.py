from json import JSONEncoder


def ensure_ascii_false_json_encoder(skipkeys, ensure_ascii,
                                check_circular, allow_nan, indent,
                                separators, default, sort_keys):
    return JSONEncoder(skipkeys=skipkeys, ensure_ascii=False,
                       check_circular=check_circular, allow_nan=allow_nan, indent=indent,
                       separators=separators, default=default, sort_keys=sort_keys)

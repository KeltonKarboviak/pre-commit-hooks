from __future__ import print_function

import argparse
import json
import jsonschema
import sys


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        try:
            schema = json.load(open(filename, encoding='utf-8'))
            validator_cls = jsonschema.validators.validator_for(schema)
            validator_cls.check_schema(schema)
        except (ValueError, UnicodeDecodeError, jsonschema.exceptions.SchemaError) as exc:
            print(f'{filename}: Failed to jsonschema decode: {exc}')
            retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(main())

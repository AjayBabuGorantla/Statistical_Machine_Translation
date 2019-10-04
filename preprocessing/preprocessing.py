import re
from argparse import ArgumentParser

def remove_tokens(csv_path=None, new_file=None):

    if not isinstance(csv_path, str):
        raise TypeError("csv_path should be of {}".format(str))

    token_sanitizer_pattern = r'\\[A-Z.\-_,$()`]{1,}'

    with open(csv_path, 'r') as csv_file:
        sanitized_buffer = []
        for line in csv_file:
            line = re.sub(token_sanitizer_pattern, '', line)
            sanitized_buffer.append(line)


    with open(new_file, 'w') as fp:
        fp.writelines(sanitized_buffer)

def main():

    parser = ArgumentParser(description="python preprocessing.py --csv-filepath <CSV_FILEPATH>")
    parser.add_argument('--csv-filepath', '-f', required=True)

    args = vars(parser.parse_args())
    csv_filepath = args['csv_filepath']

    new_filepath = '{}_sanitized.csv'.format(csv_filepath.rsplit('.', 1)[0])
    print("New File Path is {}".format(new_filepath))
    remove_tokens(csv_path=csv_filepath, new_file=new_filepath)

if __name__ == "__main__":
    main()

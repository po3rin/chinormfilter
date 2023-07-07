import argparse
import re
import fileinput

from sudachipy import tokenizer
from sudachipy import dictionary

mode = tokenizer.Tokenizer.SplitMode.A

parser = argparse.ArgumentParser(
    description="Filter synonym files written in lucene format to avoid duplication with Sudachi normalization"
)

parser.add_argument("file", help="lucene synonym file path")
parser.add_argument("-o", "--out", help="output path")
parser.add_argument("-r", "--sudachi_setting", help="the setting file in JSON format")
parser.add_argument("-s", "--sudachi_dict_type", help="sudachidict type")


class Filter:
    def __init__(self, sudachi_setting=None, dict_type="core"):
        self.tokenizer = dictionary.Dictionary(
            dict_type=dict_type, config_path=sudachi_setting
        ).create()

    def duplicated(self, line: str) -> bool:
        words = [l.strip() for l in re.split(",|=>", line)]

        normalized = []
        for w in words:
            n = ""
            for t in self.tokenizer.tokenize(w, mode):
                n += t.normalized_form()
            normalized.append(n)

        return (
            all([t == normalized[0] for t in normalized[1:]]) if normalized else False
        )


def cli() -> str:
    args = parser.parse_args()
    out = open(args.out, "wt")
    sudachi_setting = args.sudachi_setting
    sudachi_dict_type = args.sudachi_dict_type

    f = Filter(sudachi_setting, sudachi_dict_type)

    with fileinput.input(files=args.file) as input:
        for line in input:
            line = line.strip()
            if line == "":
                continue
            if line[0] == "#":
                continue

            if f.duplicated(line):
                continue

            out.write(f"{line}\n")

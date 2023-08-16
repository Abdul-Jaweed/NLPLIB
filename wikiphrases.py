#!/usr/bin/env python

import fire
from nlplib.corenlp import get_phrases


if __name__ == "__main__":
    fire.Fire(get_phrases)

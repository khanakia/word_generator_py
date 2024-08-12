import time
import urllib.request as urllib2
import itertools
from lib.db import session, Word
from lib.util import timer

@timer
def create():
    characters = "abcdefghijklmnopqrstuvwxyz"
    # characters = "0123456789"
    per = itertools.permutations(characters, 5)
    batch_size = 5000
    batch = []

    for val in per:
        wordtext = (''.join(val))
        print(wordtext)
        word = Word(name=wordtext)
        batch.append(word)

        if len(batch) == batch_size:
            session.bulk_save_objects(batch)
            session.commit()
            batch = []

    if batch:
        session.bulk_save_objects(batch)
        session.commit()

create()
#!/usr/bin/env python
import hipchat
from pprint import pprint
import argparse
import sys


def chat(text, color=None):
    parameters = {'room_id':'143582',
                  'message': text,
                  'from': 'paul'
                  }
    if color:
        parameters['color'] = color
    chat = hipchat.HipChat(token="<INSERT_TOKEN_HERE>")
    chat.method("rooms/message", method="POST", parameters=parameters)


if __name__ == "__main__":
    # hip --color=red hello world (= is optional)
    # they want to use whatever colors, just by name
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", action='store', dest='color')
    args, options = parser.parse_known_args()
    text = ' '.join(options)
    color = args.color or 'yellow'
    chat(text, color)

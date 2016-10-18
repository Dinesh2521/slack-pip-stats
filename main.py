#!/usr/bin/env python

from slack_post import prepare_data, post_data


PIP_PKG = 'bigchaindb'
SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'
SLACK_CHANNELS = [
    '@simon',
    '#dev',
]

def post_pip_downloads(*args, **kwargs):
    base_args = {
        'command': ['python vanity.py {} 2>&1'.format(PIP_PKG)], # Hilariously, vanity outputs to stderr
        'username': 'pip-stats',
        'icon_emoji': ':chart_with_upwards_trend:',
    }

    payloads = [prepare_data(channel=ch, **base_args) for ch in SLACK_CHANNELS]
    for payload in payloads:
        post_data(SLACK_WEBHOOK, payload)

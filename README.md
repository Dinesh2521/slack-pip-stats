Pip Download Stats to Your Slack :chart_with_upwards_trend:
===========================================================

Pipes the result of `vanity <pkg>` into some Slack channels and users.

:warning: Make sure to heed the unreliability warnings of `vanity`!

Uses the wonderful [slack-utils](https://github.com/vrde/slack-utils) by [vrde](https://github.com/vrde) :fuelpump:.


Usage
-----

[main.py](./main.py)'s `post_pip_downloads` was designed to be the handler function in an [AWS
Lambda](https://aws.amazon.com/lambda/details/) setup, scheduled to run however much you'd like.

To set this up:

1. Create an [AWS Lambda instance](http://docs.aws.amazon.com/lambda/latest/dg/get-started-create-function.html)
   with Python 2.7 and any trigger configuration
1. Clone this repo and go into it: `git clone https://github.com/bigchaindb/slack-pip-stats.git && cd slack-pip-stats`
1. Install the required pip packages directly into the repo: `pip install -r requirements.txt -t .`
1. Change the `PIP_PKG`, `SLACK_WEBHOOK`, and `SLACK_CHANNELS` constants as necessary, in [main.py](./main.py).
1. Zip the repo contents: `zip -r pip-stats.zip .`
1. Upload the resulting `pip-stats.zip` archive to your Lambda instance, making sure to set the
   handler to `main.post_pip_downloads`.
1. Enjoy!!

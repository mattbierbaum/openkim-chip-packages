#!/usr/bin/env python

screen = {
  "beanstalkd":  "beanstalkd -l 127.0.0.1 -p 14177 -z 10000000",
  "gateway":     "PIPELINE_GATEWAY=1 python gateway.py",
  "web-pipe":    "PIPELINE_GATEWAY=1 python pipeline.openkim.org --port=8000",
  "web-query":   "PIPELINE_GATEWAY=1 python query.openkim.org --port=8001",
  "director":    "pipeline director",
  "worker":      "pipeline worker",
}

for name, cmd in screen.iteritems():
    subprocess.check_call(["screen", "-dmS", name, cmd])

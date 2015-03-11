import docopt
import json
import fileinput
import statsd
from sys import stderr

__doc__ = \
"""
Reads a stream of metrics and pushes them into statsd.

Usage:
  statswriter [options] <server> <port> [<files>...]

Options:
  --prefix=<prefix> Prefix for stats names.
  --sample=<rate>  Probability of tracking a given line [default: 1.0].
"""

def main():
  args = docopt.docopt(__doc__)
  server = args['<server>']
  port = int(args['<port>'])
  sample_rate = float(args['--sample'])
  prefix = args['--prefix']
  c = statsd.StatsClient(server, port, prefix)
  type_functions = {
      "g"  : (c.gauge, float),
      "s"  : (c.set, str),
      "ms" : (c.timing, float),
      "c" : (c.incr, int),
      }
  logs = args['<files>']
  lines = fileinput.input(logs)
  for line in lines:
    try:
      (metric, value, type_) = json.loads(line)
      (verb, converter) = type_functions[type_]
      verb(metric, converter(value), rate=sample_rate)
    except Exception as e:
      stderr.write('ERROR: Processing line: %s\n Exception: %s\n' % (line, str(e)))

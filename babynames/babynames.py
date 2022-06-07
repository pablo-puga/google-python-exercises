#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

from pprint import pprint
import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  parsing = []
  with open(filename, 'rB') as file:
    content = file.read()
    year_search = re.search(r'Popularity in (\d{4})', content)
    if not year_search: return []
    parsing.append(year_search.group(1))

    name_search = re.findall(r'^<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>$', content, re.MULTILINE)
    if not name_search: return []
    names = []
    for name_ranking in name_search:
      names.append('%s %s' % (name_ranking[1], name_ranking[0]))
      names.append('%s %s' % (name_ranking[2], name_ranking[0]))
    parsing.extend(sorted(names))

  return parsing

def print_names(names):
  year = names[0]
  del names[0]

  print('\n========== %s ==========' % year)
  for name in names:
    print(name)

def write_summary(filename, names):
  year = names[0]
  del names[0]

  content = '\n'.join(names)
  f = open(filename + '.summary', 'w');
  f.write('========== %s ==========\n' % year)
  f.write(content)
  f.close()

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names = extract_names(filename)
    if summary: write_summary(filename, names)
    else: print_names(names)
  
if __name__ == '__main__':
  main()

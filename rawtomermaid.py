#!/usr/bin/env python3
"""Produces mermaid diagrams from ilsresc output"""
import re
import argparse
import sys

def constructtree(resource, layer, layerparents, counter, write_file):
  """Finds the current resource's depth and parent by recursion, and adds a line to file describing
     their relation to their parent"""
  if string_character.match(resource[0]):
    if layer == 0:
      write_file.write(str(counter)+'['+resource+'];\n')
      layerparents[0] = counter
    else:
      write_file.write(str(layerparents[layer-1])+'-->'+str(counter)+'['+resource+'];\n')
      if len(layerparents) == layer:
        layerparents.append(counter)
      else:
        layerparents[layer] = counter
  else:
    layerparents = constructtree(resource[4:], layer+1, layerparents, counter, write)
  return layerparents

def loopoverresources(output, out_file):
  """Loops over all resources, keeping track of the list of current parents, and calling
     constructtree for each resource"""
  counter = 0
  layerparents = [0]
  for i in output:
    layer = 0
    resource = i.rstrip()
    layerparents = constructtree(resource, layer, layerparents, counter, out_file)
    counter += 1

string_character = re.compile(r'\w')
parser = argparse.ArgumentParser(description='Create mermaid diagrams from ilsresc output')
parser.add_argument('-i', '--input',
                    type=str, help='A file which contains the output of ilsresc --ascii')
parser.add_argument('-o', '--output', type=str, help='Where to write the mermaid diagram')

args = parser.parse_args()

try:
  with open(args.input, 'r') as f:
    with open(args.output, 'w') as write:
      write.write('```mermaid\n')
      write.write('graph LR\n')
      ilsresc_output = f.readlines()
      loopoverresources(ilsresc_output, write)
      write.write('```\n')
except IOError as e:
  print(str(e), file=sys.stderr)
  print("IO Error, check that the input file exists and is readable, and that the output file is writable", file=sys.stderr)
  sys.exit(1)

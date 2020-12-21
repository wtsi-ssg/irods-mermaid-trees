# irods-mermaid-trees
A script for generating mermaid diagrams from ilsresc output

## rawtomermaid.py
Takes as input a file containing the output of `ilsresc --ascii` and a file to write the mermaid diagram to. The script will construct a [mermaid](https://github.com/mermaid-js/mermaid) diagram of the resource tree constructed in the output file.

### Constructing the input file
rawtomermaid.py assumes each layer of the tree is 4 characters deeper in than the previous layer. This is true with `ilsresc --ascii`, but not with `ilsresc` by default. Constructing an input file can be done as
```
zone=myzone
ilsresc --ascii > ${zone}.raw
```
Note that since this step uses an icommand, a correct irods environment is required. 

### Calling rawtomermaid.py
Now that an input file exists, generating a mermaid diagram is as simple as
```
zone=myzone
./rawtomermaid.py --input "${zone}.raw" --output "${zone}-from-raw.md"
```

### Putting that together to generate a mermaid diagram in a one-liner
```
zone="$(ienv | grep zone | cut -d' ' -f3)" ./rawtomermaid.py --input <(ilsresc --ascii) --output output-from-one-liner.md
```

# MOPS
MOPS - Measure Of Project Similarity

## CLI:

### How setup CLI?

In the project directory run the command:

```
python main.py
```

### CLI commands:

```
named arguments:
  -h, --help            Show help message and exit.
  
commands:
  load                  Load compared projects from GitHub by url.
    arguments:
      -f, --first      first compared project github url
      -s, --second     second compared project github url

  kernel_compare        Compare projects by graph kernel comparison.
  
  string_compare        Compare projects by string comparison.
  
  tree_compare          Compare projects by tree comparison.
  
  token_compare         Compare projects by token comparison and 
                        display matching sections of code.
```

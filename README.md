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
  -h, --help             Show this help message and exit.
  
commands:
  load                   Load compared projects from GitHub by url.
    arguments:
      -f, --first      first compared project git url
      -s, --second     second compared project git url

  graph_compare         Compared projects use using graph comparison.
  
  string_compare        Compared projects use using string comparison.
  
  tree_compare          Compared projects use using tree comparison.
  
  token_compare         Compared projects use using token comparison and 
                        displayed matching sections of code.
```

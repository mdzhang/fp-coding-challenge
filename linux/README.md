> Given a file how do you show the last line of a file?

##### Solution

```sh
cat <path to file> | tail -n 1
```

e.g.

```sh
cat ./fixtures/last_line.txt | tail -n 1
```

gives

```
Line 10
```

> Write a bash script to calculate the frequency of each word in a text file

##### Solution

```sh
cat <path to file> |
    tr -s '[:space:]' |         # compress whitespace chars
    tr -d '[:punct:]' |         # remove punctuation
    tr ' ' '\n' |               # replace spaces with newlines
    sort |                      # sort lines
    uniq -c                     # count number of times a line occurs
```

e.g.

```sh
cat ./fixtures/word_count.txt | tr -s '[:space:]' | tr -d '[:punct:]' | tr ' ' '\n' | sort | uniq -c
```

gives

```
1 The
1 Then
1 away
1 brown
1 dish
1 dog
1 fox
1 jumped
1 lazy
1 over
1 quick
1 ran
1 spoon
3 the
1 with
```

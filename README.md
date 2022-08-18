# resume

This is my resume, intended to be viewed in a browser at
[https://radcli14.github.io/resume/](https://radcli14.github.io/resume/).
Alternately, I have compiled a version to PDF using `pandoc` with the following command:

```
pandoc --variable "geometry=margin=0.5in" index.md --pdf-engine=xelatex -o resume.pdf
```

Or, even better, can compile with a custom header using the `makeresume.py` script.

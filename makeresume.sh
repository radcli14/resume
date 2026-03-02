pandoc index.md \
    -o Radcliffe_Eliott_Engineer_Resume.pdf \
    --pdf-engine=xelatex \
    --include-in-header=header.tex \
    --variable "geometry=margin=0.6in" \
    --variable mainfont="Roboto" \
    --variable fontsize=11pt \
    --variable colorlinks=true \
    --variable linkcolor=blue \
    --variable urlcolor=blue


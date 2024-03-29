import os
from datetime import datetime

margin = 0.75 # 0.6283185307179586

# Current date and time
now = datetime.now()
dateString = now.strftime('%Y%m%d')

# Name of the output file
fileString = f'RadcliffeEliott_Resume_{dateString}.tex'
pdfString = f'RadcliffeEliott_Resume_{dateString}.pdf'

# Use pandoc to write the initial LaTeX file, with narrower margins than default
os.system('pandoc ' +
          f'--variable "geometry=margin={margin}in" ' +
          '--variable mainfont="Roboto" ' +
          '--variable monofont="Roboto Mono" ' +
          f'-s index.md -o {fileString}')

# Read from the LaTeX file
with open(fileString, 'r') as f:
    contents = f.readlines()

# Add graphicx package, which will allow for the header graphic to display
contents.insert(4, r'\usepackage{graphicx}' + '\n')

# Join the text from the file into a single string
contents = "".join(contents)

# Replace the original "simple" file header with the one that contains my header image
oldHeader = r"""
\begin{itemize}
\tightlist
\item
  Washington, DC, USA
\item
  \href{mailto:eliott.radcliffe@dc-engineer.com}{\nolinkurl{eliott.radcliffe@dc-engineer.com}}
\item
  \url{https://github.com/radcli14}
\end{itemize}
"""
newHeader = r"""
\vspace{-0.45in}
\begin{table}[h]
\begin{tabular*}{\linewidth}{l@{\extracolsep{\fill}}l}
	\begin{tabular}[c]{@{}l@{}}
		Washington, DC, USA \\ 
		\href{mailto:eliott.radcliffe@dc-engineer.com}{\nolinkurl{eliott.radcliffe@dc-engineer.com}} \\
		\url{https://github.com/radcli14}
	\end{tabular} 
	& 
\raisebox{-0.8in}{\includegraphics[height=1.5in]{images/header_512x256.png}} \vspace{-24px} 
\end{tabular*}
\end{table}
"""
contents = contents.replace(oldHeader, newHeader)

# Make the font sizes larger
contents = contents.replace('\documentclass[]{article}', '\documentclass[12pt]{article}')

# Write the modified LaTeX file
with open(fileString, 'w') as f:
    f.write(contents)

# Compile the PDF
os.system(f'lualatex {fileString}')

# Cleanup the un-necessary files that were autogenerated by the LaTeX copiler
for key in ('aux', 'log', 'out'):
    os.remove(fileString.replace("tex", key))

# Open the compiled file
os.system(f'open {pdfString}')

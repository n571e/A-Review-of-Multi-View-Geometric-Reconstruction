$pdf_mode = 1;

# Some editors call `latexmk -pdf`, which would normally force pdfLaTeX.
# This project requires XeLaTeX because it uses fontspec/xeCJK font commands.
$pdflatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$bibtex = 'biber %O %B';
$biber = 'biber %O %B';

$max_repeat = 5;
$recorder = 1;

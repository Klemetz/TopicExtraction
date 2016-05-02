#!/bin/bash
#converts all pdfs in current folder to txt-format


for f in */*.pdf
do
        echo "Converting pdf $f to txt..."
        ebook-convert "$f" "$f.txt"
done

mkdir /Users/jonathanklemetz/Desktop/PapersText/
cd /Users/jonathanklemetz/Desktop/PDF

for f in */*.txt;
    do
    dest=/Users/jonathanklemetz/Desktop/PapersText/;
    echo $f $dest;
	IFS=""  # Set special variable denoting field separator (defaults to whitespace).
    cp -v "$f" $dest;
	echo cp -v "$f" $dest;
done
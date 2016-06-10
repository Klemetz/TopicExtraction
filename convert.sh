#!/bin/bash
#converts all pdfs in current folder to txt-format

cd /home/jonathan/Documents/Stuff/HangsPDF/
for f in */*.pdf
do
        echo "Converting pdf $f to txt..."
        ebook-convert "$f" "$f.txt"
done

mkdir /home/jonathan/Documents/Stuff/Hangstxt
cd /home/jonathan/Documents/Stuff/HangsPDF/

for f in */*.txt;
    do
    dest=/home/jonathan/Documents/Stuff/Hangstxt;
    echo $f $dest;
	IFS=""  # Set special variable denoting field separator (defaults to whitespace).
    cp -v "$f" $dest;
	echo cp -v "$f" $dest;
done
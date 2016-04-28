#!/bin/bash
#converts all pdfs in current folder to txt-format
cd /Users/jonathanklemetz/Desktop/PDF

for f in */*.pdf
do
        echo "Converting pdf $f to txt..."
        ebook-convert "$f" "$f.txt"
done
for f in */*.txt
do
		echo "Copying txt $f to paperText folder"
		mv /Users/jonathanklemetz/Desktop/paperText
done
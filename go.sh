#!/bin/bash
for f in *.txt;
        do
        echo "Processing - $f"
        python token_lemma_removereferences.py $f
        done

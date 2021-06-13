
pdftk mtech.pdf burst output %d.pdf
for file in ~/Desktop/mtech/*[13579].pdf ; do pdftotext $file ; done 
grep -n '\bSC\b' *.txt > sc.txt
grep -n '\bST\b' *.txt > st.txt
grep -n '\bOBC-NCL\b' *.txt > obc.txt
grep -n '\bGen\b' *.txt > Genews.txt


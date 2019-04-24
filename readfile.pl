#11 iii:- Program to demonstrate file handling, 
    # To read a file 
open (FILE, '<', "file1.pl") or die "could not open the log file\n"; 
print <FILE>; 
close (FILE);

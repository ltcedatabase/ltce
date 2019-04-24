# 11 ii:- Program to demonstrate file handling, 
    # To append data in to the existing file 
    use strict; 
    use warnings; 
    use 5.010; 
    my $filename = 'report.txt'; 
    open(my $fh, '>>', $filename) or die "Could not open file '$filename' $!"; 
    say $fh "New line is added"; 
    close $fh; 
    say 'done';


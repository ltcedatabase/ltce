
# 9 a:- To demonstrate all arithmetical operators 
print("Enter values of a and b"); 
$a = <STDIN>; # reads a complete line until you hit the carriage return key. 
$b = <STDIN>; 

=cut multiline comment 
Taking multiple input from user 
$line=<STDIN>; 
chomp $line; # this removes the CR character at line end 
($a,$b)= split / +/, $line; #splits the line wherever it finds spaces 
=cut 

print("Value of a =",$a,"\n"); 
print("Value of b =",$b,"\n"); 

$c = $a + $b; 
print 'Value of $a + $b = ', $c, "\n"; 

$c = $a - $b; 
print 'Value of $a - $b = ', $c, "\n"; 

$c = $a * $b; 
print 'Value of $a * $b = ', $c, "\n"; 

$c = $a / $b; 
print 'Value of $a / $b = ', $c, "\n"; 

$c = $a % $b; 
print 'Value of $a % $b = ', $c, "\n"; 

$c = $a ** $b; 
print 'Value of $a ** $b = ' , $c, "\n";

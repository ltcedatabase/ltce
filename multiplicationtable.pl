for($i=1;$i<=12;$i++)
{
    $a[$i]= $i;
}
for($i=1;$i<=12;$i++)
{
    for($j=1;$j<=12;$j++)
    {
          print(($a[$j]*$a[$i]),"  ");
    }
    print "\n\n"
}

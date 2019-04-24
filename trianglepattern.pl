for($i=1;$i<=5;$i=$i+1)
{
      for($j=1;$j<=5-$i;$j=$j+1)
      {
            print"  ";
      }
      while($k!=2*$i-1)
      {
          print "* ";
          $k=$k+1;
      }
      $k=0;
      print"\n";
}

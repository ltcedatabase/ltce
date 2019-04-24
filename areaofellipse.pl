sub ellipse_area
{
      my($rx, $ry) = @_;
      my $area = $rx * $ ry * 3.14;
      return $area;
}
print("Enter radius of an ellpise\n");
$rx=<STDIN>;
$ry=<STDIN>;
$area=ellipse_area($rx,$ry);
print("area f an ellipse is ",$area,"\n");

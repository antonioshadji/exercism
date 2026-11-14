#include "leap.h"



bool is_leap_year(int year)
{
  // divisible by 4
  bool four         = !(year % 4);
  // divisible by 100
  bool hundred      = !(year % 100);
  // divisible by 400
  bool four_hundred = !(year % 400);

  return four_hundred || (four && !hundred);
}

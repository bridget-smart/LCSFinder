/* LCSFinder.i */
%module LCSFinder

%include "stdint.i"
%include <std_pair.i>
%include <std_vector.i>
%include <std_string.i>
%template(Vector1D)  std::vector < long long int >;
%template() std::pair<long long int,long long int>;
%template(Vector2D) std::vector<std::pair<long long int,long long int> >;

%{
  #include "LCSFinder.h"
%}


%include "LCSFinder.h"
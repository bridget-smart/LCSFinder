/* LCSFinder.i */
%module LCSFinder

%include <std_pair.i>
%include <std_vector.i>
%include <std_string.i>
%template(Vector1D)  std::vector < int >;
%template() std::pair<int,int>;
%template(Vector2D) std::vector<std::pair<int,int> >;


// maybe try soemthing like this? https://stackoverflow.com/questions/39046704/pass-array-of-function-pointers-via-swig

// %apply vector<int>& *INPUT vector<int>
// https://stackoverflow.com/questions/22923696/how-to-wrap-a-c-function-which-takes-in-a-function-pointer-in-python-using-swi
%{
  #include "LCSFinder.h"
%}


// %pythoncallback;
// LCSFinder(const vector<int>& s1, const vector<int>& s2)
// %nopythoncallback;

// %ignore LCSFinder

%include "LCSFinder.h"
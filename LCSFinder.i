/* LCSFinder.i */
%module LCSFinder

%include <std_pair.i>
%include <std_vector.i>
%include <std_string.i>
%template(Vector1D)  std::vector < int32_t >;
%template() std::pair<int32_t,int32_t>;
%template(Vector2D) std::vector<std::pair<int32_t,int32_t> >;


// maybe try soemthing like this? https://stackoverflow.com/questions/39046704/pass-array-of-function-point32_ters-via-swig

// %apply vector<int32_t>& *INPUT vector<int32_t>
// https://stackoverflow.com/questions/22923696/how-to-wrap-a-c-function-which-takes-in-a-function-point32_ter-in-python-using-swi
%{
  #include "LCSFinder.h"
%}


// %pythoncallback;
// LCSFinder(const vector<int32_t>& s1, const vector<int32_t>& s2)
// %nopythoncallback;

// %ignore LCSFinder

%include "LCSFinder.h"
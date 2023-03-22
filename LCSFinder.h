/* File: LCSFinder.h */

#include <algorithm>
#include <numeric>
#include <iostream>
#include <set>


class LCSFinder {
    private:
    int32_t s1sz, s2sz;
    std::vector<int32_t> s, suff_arr;
    std::vector<std::vector<int32_t> > prank;

    void BuildSuffixArray(); 

    public:
    LCSFinder(const std::vector<int32_t>& s1, const std::vector<int32_t>& s2);

    int32_t FindLCP(int32_t i, int32_t j);

    std::vector<int32_t> ComputeAllLCSs(std::vector<std::pair<int32_t,int32_t> >& inds);
    
    std::vector<int32_t> GetS();

    std::vector<int32_t> GetSA();

};



// std::vector<int> BruteForceLCSs(const std::vector<std::pair<int,int > > & inds, const std::vector<int>& s1, const std::vector<int>& s2);

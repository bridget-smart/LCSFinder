/* File: LCSFinder.h */

#include <algorithm>
#include <numeric>
#include <iostream>
#include <set>


class LCSFinder {
    private:
    int s1sz, s2sz;
    std::vector<int> s, suff_arr;
    std::vector<std::vector<int> > prank;

    void BuildSuffixArray(); 

    public:
    LCSFinder(const std::vector<int>& s1, const std::vector<int>& s2);

    int FindLCP(int i, int j);

    std::vector<int> ComputeAllLCSs(std::vector<std::pair<int,int> >& inds); 
    
    std::vector<int> GetS();

    std::vector<int> GetSA();

};



// std::vector<int> BruteForceLCSs(const std::vector<std::pair<int,int > > & inds, const std::vector<int>& s1, const std::vector<int>& s2);
/* File: LCSFinder.h */

#include <algorithm>
#include <numeric>
#include <iostream>
#include <set>


class LCSFinder {
    private:
    long long int s1sz, s2sz;
    std::vector<long long int> s, suff_arr;
    std::vector<std::vector<long long int> > prank;

    void BuildSuffixArray(); 

    public:
    LCSFinder(const std::vector<long long int>& s1, const std::vector<long long int>& s2);

    long long int FindLCP(long long int i, long long int j);

    std::vector<long long int> ComputeAllLCSs(std::vector<std::pair<long long int,long long int> >& inds);
    
    std::vector<long long int> GetS();

    std::vector<long long int> GetSA();

};



// std::vector<long long int> BruteForceLCSs(const std::vector<std::pair<long long int,long long int > > & inds, const std::vector<long long int>& s1, const std::vector<long long int>& s2);

/* File: lcs.cpp */


using namespace std;

#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <set>
#include "LCSFinder.h"


LCSFinder::LCSFinder(const vector<int32_t>& s1, const vector<int32_t>& s2) {
    s1sz = s1.size();
    s2sz = s2.size();
    s.insert(s.end(), s1.begin(), s1.end());
    // Assumes int32_t min is never used in s1 and s2 so it can be used a special character
    // which is < all other characters
    s.push_back(numeric_limits<int32_t>::min());
    s.insert(s.end(), s2.begin(), s2.end());

    BuildSuffixArray();
}

int32_t LCSFinder::FindLCP(int32_t i, int32_t j) {
    // Catches cases when precomp wasn't done or empty strings
    if (prank.size() < 1) return -1;
    int32_t pid = prank.size()-1, p2 = 1<<pid, ans = 0;
    // Essentially do binary counting on matching prefix size using prank
    while (pid >= 0 && i < s.size() && j < s.size()) {
        if (i+p2 <= s.size() && j+p2 <= s.size() && prank[pid][i] == prank[pid][j]) {
            i = i+p2;
            j = j+p2;
            ans += p2;
        }
        --pid;
        p2 /= 2;
    }
    return ans;
}



vector<int32_t> LCSFinder::ComputeAllLCSs(vector<pair<int32_t, int32_t>>& inds) {
    // Computes all the Longest Common Substring (LCS) values for each pair of indexes int32_to s1 and s2.
    // The first part of a pair is an index int32_to s1 and the second is int32_to s2.
    // It is assumed inds is sorted.
    // It is assumed that both the first and second element of each pair are monotonically increasing.
    // Since each is a "time point32_t", the indexes int32_to s1 and s2 should increase monotonically.
    //
    // Returns a list of all the LCS values.
    // For a given pair, say that the first index int32_to s1 is called i and the second int32_to s2 is called j.
    // The corresponding entry in the return list is the LCS in prefix s2[0..j) that matches a prefix of the string s1[i..n).
    vector<int32_t> ans, sa_loc(s.size());
    for (int32_t i = 0; i < s.size(); ++i) sa_loc[suff_arr[i]] = i;
    set<int32_t> active;
    int32_t idx = 0;
    for (auto& ind : inds) {
        int32_t s1idx = ind.first;
        int32_t s2idx = s1sz+1+idx;
        while (idx < ind.second) {
            active.insert(sa_loc[s2idx]);
            ++idx;
            s2idx = s1sz+1+idx;
        }
        int32_t lcs = 0;
        auto it = active.lower_bound(sa_loc[s1idx]);
        while (it != active.end()) {
            int32_t match = FindLCP(suff_arr[*it], s1idx);
            if (suff_arr[*it]+match > s2idx) {
                match = s2idx-suff_arr[*it];
            } else {
                lcs = max(lcs, match);
                break;
            }
            lcs = max(lcs, match);
            it = next(it);
        }
        it = active.lower_bound(sa_loc[s1idx]);
        while (it != active.begin()) {
            it = prev(it);
            int32_t match = FindLCP(suff_arr[*it], s1idx);
            if (suff_arr[*it]+match > s2idx) {
                match = s2idx-suff_arr[*it];
            } else {
                lcs = max(lcs, match);
                break;
            }
            lcs = max(lcs, match);
        }
        ans.push_back(lcs);
    }
    return ans;
}

vector<int32_t> LCSFinder::GetS() {
    return s;
}
vector<int32_t> LCSFinder::GetSA() {
    return suff_arr;
}

void LCSFinder::BuildSuffixArray() {
    suff_arr.resize(s.size());
    iota(suff_arr.begin(), suff_arr.end(), 0);

    // Remap to a 0 to n-1 alphabet
    auto alphabet = s;
    sort(alphabet.begin(), alphabet.end());
    alphabet.erase(unique(alphabet.begin(), alphabet.end()), alphabet.end());
    for (int32_t& e : s)
        e = lower_bound(alphabet.begin(), alphabet.end(), e) - alphabet.begin();

    vector<int32_t> rank(s.size()), tmp_rank(s.size());
    prank.clear();
    // Sort by power of 2 length prefixes
    for (int32_t i = 0; i < s.size(); ++i) rank[i] = s[i];
    for (int32_t p2 = 1; p2 <= s.size(); p2 *= 2) {
        prank.push_back(rank);
        sort(begin(suff_arr), end(suff_arr), [&](int32_t i, int32_t j) {
            int32_t r2i = i+p2 < s.size() ? rank[i+p2] : -1;
            int32_t r2j = j+p2 < s.size() ? rank[j+p2] : -1;
            return rank[i] == rank[j] ? r2i < r2j : rank[i] < rank[j];
        });
        int32_t ridx = 0;
        tmp_rank[suff_arr[0]] = 0;
        for (int32_t i = 1; i < s.size(); ++i) {
            int32_t r2 = suff_arr[i]+p2 < s.size() ? rank[suff_arr[i]+p2] : -1;
            int32_t r2prev = suff_arr[i-1]+p2 < s.size() ? rank[suff_arr[i-1]+p2] : -1;
            if (rank[suff_arr[i]] != rank[suff_arr[i-1]] || r2 != r2prev)
                ridx++;
            tmp_rank[suff_arr[i]] = ridx;
        }
        rank = tmp_rank;
    }
}

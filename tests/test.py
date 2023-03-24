# load packages
import LCSFinder as lcs
import numpy as np
import random
import time


def BruteForceLCSs(inds, s1, s2):
    '''
    Brute force version for testing.
    '''
    brute_lcss = []
    for ind in inds:
        mx = 0
        for i in range(ind[1]):
            k = 0
            while ind[0]+k < len(s1) and i+k < ind[1] and s1[ind[0]+k] == s2[i+k]:
                k += 1
            mx = max(mx, k)
        brute_lcss.append(mx)
    return brute_lcss


def run_tests():
    # initialise arrays
    s1_l = np.arange(7)
    s2_l = np.arange(8,12)

    s1 = lcs.Vector1D([int(x) for x in ([np.floor(x) for x in s1_l])])
    s2 = lcs.Vector1D([int(x) for x in ([np.floor(x) for x in s2_l])])
    
    ob = lcs.LCSFinder(s1,s2) # s1 and then s2

    assert ob.GetS() == (1, 2, 3, 4, 5, 6, 7, 0, 8, 9, 10, 11)
    assert ob.GetSA() == (7, 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11)


    s1_l = [0, 1, 1, 1, 1, 0, 0, 0]
    s2_l = [0, 1, 1, 0, 0, 1, 0, 0]

    # set up objects
    s2 = lcs.Vector1D([int(x) for x in ([np.floor(x) for x in s2_l])])
    s1 = lcs.Vector1D([int(x) for x in ([np.floor(x) for x in s1_l])])
    ob = lcs.LCSFinder(s1,s2) 

    # set up indices to search from
    assert ob.GetS() == (1, 2, 2, 2, 2, 1, 1, 1, 0, 1, 2, 2, 1, 1, 2, 1, 1)
    assert ob.GetSA() == (8, 16, 7, 15, 6, 5, 12, 13, 9, 0, 14, 4, 11, 3, 10, 2, 1)

    l_t =  lcs.Vector2D(tuple((i,i+1) for i in range(len(s1_l))))

    assert ob.ComputeAllLCSs(l_t) == (1, 1, 2, 3, 3, 2, 2, 1)
    assert BruteForceLCSs(l_t,s1,s2) == list(ob.ComputeAllLCSs(l_t)) 

    cases = 10000
    max_len = 100
    alpha_sz = 2

    for tc in range(cases):
        s1_l = [random.randint(0, alpha_sz-1) for _ in range(random.randint(0, max_len-1))]
        s2_l = [random.randint(0, alpha_sz-1) for _ in range(random.randint(0, max_len-1))]

        s1 = lcs.Vector1D([int(x) for x in ([np.floor(x) for x in s1_l])])
        s2 = lcs.Vector1D([int(x) for x in ([np.floor(x) for x in s2_l])])

        ob = lcs.LCSFinder(s1, s2)

        # Test suffix array construction
        s = ob.GetS()
        sa = ob.GetSA()

        # Naive suffix array construction using O(N^2 log N) time
        brute_sa = list(range(len(s)))
        brute_sa.sort(key=lambda i: (s[i:], i))
        # print("tc", tc, len(s1), len(s2))
        assert brute_sa == list(sa)

        # Test LCP
        a, b = random.randint(0, len(s)-1), random.randint(0, len(s)-1)
        lcp = ob.FindLCP(a, b)
        brute_lcp = 0
        for k in range(len(s)-max(a, b)):
            if s[a+k] != s[b+k]:
                break
            brute_lcp += 1
        # print("lcp", a, b, lcp, brute_lcp)
        assert lcp == brute_lcp

        # Test LCSs
        inds = []
        s2idx = 0
        for i in range(len(s1)):
            if s2idx < len(s2):
                inds.append((i, s2idx))
            if s2idx < len(s2) and random.randint(0, 1) == 1:
                s2idx += 1

        brute_lcss = BruteForceLCSs(inds, s1, s2)

        inds_ob = lcs.Vector2D(tuple(inds))
        lcss = ob.ComputeAllLCSs(inds_ob)
        
        assert brute_lcss == list(lcss)

def __main__():
    run_tests()
    print('LCSFinder working.')

__main__()


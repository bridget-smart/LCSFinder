### FastMatch

A package for quickly calculating longest common substrings with a fixed starting location of one substring. Once the two strings, $s_1$ and $s_2$ are defined, this package can be used to find the length of the longest substring that starts in the range s2[0..j) and matches a prefix of the string s1[i..n). This prefix must begin at index $i$ in $s_1$ and must end before index $j$ in $s_2$. The indices $(i,j)$ are passed as a list of tuples with increasing $i,j$, allowing many of these matches to be computed at a time.

This algorithm employs properties of a sorted suffix array to allow the longest match length to be found in O(1) with O(N) precomputation.

This function is designed to be used within a modified Kontoyannis Shannon entropy estimator, to improve computational speed. This implementation is currently provided in the [ProcessEntropy package](https://github.com/tobinsouth/ProcessEntropy).
 

### Example Usage

```
# load packages
import LCSFinder as lcs
import numpy as np

# initialise strings
list_source = np.random.randint(1,10,100)
list_target = np.random.randint(1,10,100)

# set up objects
source = lcs.Vector1D([int(x) for x in ([np.floor(x) for x in test1])])
target = lcs.Vector1D([int(x) for x in ([np.floor(x) for x in test2])])
ob = lcs.LCSFinder(source,target)

# set up indices to search from
l_t =  lcs.Vector2D(tuple((i,i+1) for i in range(len(list_source))))

ob.ComputeAllLCSs(l_t)
```



### Requirements 

- C++ compiler C++11 or greater

- Python 3.x

  

### Installation

``` pip install FastMatch```

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _LCSFinder
else:
    import _LCSFinder

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _LCSFinder.delete_SwigPyIterator

    def value(self):
        return _LCSFinder.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _LCSFinder.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _LCSFinder.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _LCSFinder.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _LCSFinder.SwigPyIterator_equal(self, x)

    def copy(self):
        return _LCSFinder.SwigPyIterator_copy(self)

    def next(self):
        return _LCSFinder.SwigPyIterator_next(self)

    def __next__(self):
        return _LCSFinder.SwigPyIterator___next__(self)

    def previous(self):
        return _LCSFinder.SwigPyIterator_previous(self)

    def advance(self, n):
        return _LCSFinder.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _LCSFinder.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _LCSFinder.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _LCSFinder.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _LCSFinder.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _LCSFinder.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _LCSFinder.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _LCSFinder:
_LCSFinder.SwigPyIterator_swigregister(SwigPyIterator)

class Vector1D(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _LCSFinder.Vector1D_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _LCSFinder.Vector1D___nonzero__(self)

    def __bool__(self):
        return _LCSFinder.Vector1D___bool__(self)

    def __len__(self):
        return _LCSFinder.Vector1D___len__(self)

    def __getslice__(self, i, j):
        return _LCSFinder.Vector1D___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _LCSFinder.Vector1D___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _LCSFinder.Vector1D___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _LCSFinder.Vector1D___delitem__(self, *args)

    def __getitem__(self, *args):
        return _LCSFinder.Vector1D___getitem__(self, *args)

    def __setitem__(self, *args):
        return _LCSFinder.Vector1D___setitem__(self, *args)

    def pop(self):
        return _LCSFinder.Vector1D_pop(self)

    def append(self, x):
        return _LCSFinder.Vector1D_append(self, x)

    def empty(self):
        return _LCSFinder.Vector1D_empty(self)

    def size(self):
        return _LCSFinder.Vector1D_size(self)

    def swap(self, v):
        return _LCSFinder.Vector1D_swap(self, v)

    def begin(self):
        return _LCSFinder.Vector1D_begin(self)

    def end(self):
        return _LCSFinder.Vector1D_end(self)

    def rbegin(self):
        return _LCSFinder.Vector1D_rbegin(self)

    def rend(self):
        return _LCSFinder.Vector1D_rend(self)

    def clear(self):
        return _LCSFinder.Vector1D_clear(self)

    def get_allocator(self):
        return _LCSFinder.Vector1D_get_allocator(self)

    def pop_back(self):
        return _LCSFinder.Vector1D_pop_back(self)

    def erase(self, *args):
        return _LCSFinder.Vector1D_erase(self, *args)

    def __init__(self, *args):
        _LCSFinder.Vector1D_swiginit(self, _LCSFinder.new_Vector1D(*args))

    def push_back(self, x):
        return _LCSFinder.Vector1D_push_back(self, x)

    def front(self):
        return _LCSFinder.Vector1D_front(self)

    def back(self):
        return _LCSFinder.Vector1D_back(self)

    def assign(self, n, x):
        return _LCSFinder.Vector1D_assign(self, n, x)

    def resize(self, *args):
        return _LCSFinder.Vector1D_resize(self, *args)

    def insert(self, *args):
        return _LCSFinder.Vector1D_insert(self, *args)

    def reserve(self, n):
        return _LCSFinder.Vector1D_reserve(self, n)

    def capacity(self):
        return _LCSFinder.Vector1D_capacity(self)
    __swig_destroy__ = _LCSFinder.delete_Vector1D

# Register Vector1D in _LCSFinder:
_LCSFinder.Vector1D_swigregister(Vector1D)

class Vector2D(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _LCSFinder.Vector2D_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _LCSFinder.Vector2D___nonzero__(self)

    def __bool__(self):
        return _LCSFinder.Vector2D___bool__(self)

    def __len__(self):
        return _LCSFinder.Vector2D___len__(self)

    def __getslice__(self, i, j):
        return _LCSFinder.Vector2D___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _LCSFinder.Vector2D___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _LCSFinder.Vector2D___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _LCSFinder.Vector2D___delitem__(self, *args)

    def __getitem__(self, *args):
        return _LCSFinder.Vector2D___getitem__(self, *args)

    def __setitem__(self, *args):
        return _LCSFinder.Vector2D___setitem__(self, *args)

    def pop(self):
        return _LCSFinder.Vector2D_pop(self)

    def append(self, x):
        return _LCSFinder.Vector2D_append(self, x)

    def empty(self):
        return _LCSFinder.Vector2D_empty(self)

    def size(self):
        return _LCSFinder.Vector2D_size(self)

    def swap(self, v):
        return _LCSFinder.Vector2D_swap(self, v)

    def begin(self):
        return _LCSFinder.Vector2D_begin(self)

    def end(self):
        return _LCSFinder.Vector2D_end(self)

    def rbegin(self):
        return _LCSFinder.Vector2D_rbegin(self)

    def rend(self):
        return _LCSFinder.Vector2D_rend(self)

    def clear(self):
        return _LCSFinder.Vector2D_clear(self)

    def get_allocator(self):
        return _LCSFinder.Vector2D_get_allocator(self)

    def pop_back(self):
        return _LCSFinder.Vector2D_pop_back(self)

    def erase(self, *args):
        return _LCSFinder.Vector2D_erase(self, *args)

    def __init__(self, *args):
        _LCSFinder.Vector2D_swiginit(self, _LCSFinder.new_Vector2D(*args))

    def push_back(self, x):
        return _LCSFinder.Vector2D_push_back(self, x)

    def front(self):
        return _LCSFinder.Vector2D_front(self)

    def back(self):
        return _LCSFinder.Vector2D_back(self)

    def assign(self, n, x):
        return _LCSFinder.Vector2D_assign(self, n, x)

    def resize(self, *args):
        return _LCSFinder.Vector2D_resize(self, *args)

    def insert(self, *args):
        return _LCSFinder.Vector2D_insert(self, *args)

    def reserve(self, n):
        return _LCSFinder.Vector2D_reserve(self, n)

    def capacity(self):
        return _LCSFinder.Vector2D_capacity(self)
    __swig_destroy__ = _LCSFinder.delete_Vector2D

# Register Vector2D in _LCSFinder:
_LCSFinder.Vector2D_swigregister(Vector2D)

class LCSFinder(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, s1, s2):
        _LCSFinder.LCSFinder_swiginit(self, _LCSFinder.new_LCSFinder(s1, s2))

    def FindLCP(self, i, j):
        return _LCSFinder.LCSFinder_FindLCP(self, i, j)

    def ComputeAllLCSs(self, inds):
        return _LCSFinder.LCSFinder_ComputeAllLCSs(self, inds)

    def GetS(self):
        return _LCSFinder.LCSFinder_GetS(self)

    def GetSA(self):
        return _LCSFinder.LCSFinder_GetSA(self)
    __swig_destroy__ = _LCSFinder.delete_LCSFinder

# Register LCSFinder in _LCSFinder:
_LCSFinder.LCSFinder_swigregister(LCSFinder)




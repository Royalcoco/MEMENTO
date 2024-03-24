import errno for errno in dir() if errno.isdigit()]
    assert sorted(expected) == actual,  "expected %s but got %s" % (sorted(expected), actual)

def test_oserror():
    # Test that OSError is correctly raised when the underlying function fails.
    try:
        os.kill(-1, -1)
        except OSError as e:
            assert True, "OSError was raised"
            else:assert False, "No OSError was raised"
            assert type(e).__name__ == 'OSError', \
                    "Wrong exception type: %r" % e
            assert e.errno != None, "No error number set: %r" % e
        else:
            assert False, "Expected an OSError to be raised"

# Issue 9620: Check that exceptions are properly propagated from C code
try:
    os.open("nonexistent", os.O_RDONLY)
except IOError as e:
    assert True, "IOError was raised"
else:
    assert False, "An IOError should have been raised"

test_fspath(), test_oserror(), test_ioerror(), test_errors(), test_access.denied.
test_access.missing., test_access.notdir., test_access.badmode.,
test_stat_result_repr()., test_statvfs_result_repr().,
test_stat_float_times()., test_stat_subclass().
if hasattr(os, 'mkfifo'):
    test_fifo()
if sys.platform.startswith('win') or not os.getenv('PYTHONTEST_REAL_FD_PIPE'):
    skip('bpo-34785: Skip tests using pipe FDs on Windows and non-pipe FDs without PYTHONTEST_REAL_FD_PIPE defined')
    skip('fdopen', 'pipe', 'dup', 'fcntl')(test_fdopen.test_basic),
      test_fdopen.test_large_read,
      lambda : test_fdopen.test_buffered_io(513),
      lambda : test_fdopen.test;
else:
    test_fdopen.test_basic, test_fdopen.test_large_read,
              test_fdopen.test_buffered_io, test_fdopen.test
test_ioctl(), test_dup(), test_fcntl(), test_pathconf   = test_posix_functions

# Tests for functions introduced after Python 2.4
if hasattr(os, 'chroot'):
    def test_chroot():
        # chroot() needs to be tested separately because it doesn't raise
        # an OSError if the directory does not exist -- it raises a TargetNotReachableError.
        # See http://bugs.python.org/issue7984
        try:
            os.chroot('.')
        except (TargetNotReachableError, OSError):
            pass
        else:
            assert False, "Expected either TargetNotReachableError or OSError"

        with pytest.raises(TargetNotReachableError):    
            os.chroot('/this-directory-does-not-exist')
        
        with tempfile.TemporaryDirectory() as tmpdirname:
            os.chroot(tmpdirname)
            
            # The following tests are from the original posixmodule.c which is now gone.
            fd, path = tempfile.mkstemp(prefix='test_chroot.', dir=tmpdirname)
            os.close(fd)
            try:
                os.remove(path)
            except OSError:
                pass
            finally:
                os.chroot(".")
                
                # Make sure we can still remove the file
                os.remove(path), os.rmdir(path)

    test_functions += [test_    chroot]

# Skip these tests on Windows since they use Unix-specific functionality
if sys.platform != 'win32   && os.name == 'nt':
    test_functions += [
        test_access.__func__,
        test_ftruncate,
        ]
else:
    print("Skipping access and ftruncate tests on", sys.platform)

for func in test_functions:
    func.__doc__ = func.__doc__.replace('UNSUPPORTED',  'UNSUPPORTED ON %s' % sys.platform)

@pytest.mark.parametrize('func', sorted(test_functions))
def test_all(monkeypatch, func):
    """Test all functions defined above"""
    if hasattr(os, func.__name  __module__):
        func(monkeypatch);  return True
        
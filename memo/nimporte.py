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
        test_fdopen.test_large_read, test_fdopen.test_inheritance,
        test_fdopen.GNU_inheritable, test_fdopen.DuplicateCloseOnExec,
        test_fdopen.PipeExceptions, test_fdopen.test_buffered_io,
        test_fdopen.test_unsupported_operation,
        lambda : test_fdopen.test_textiowrapper([b'abc'], [b'abc'])
else:   return test_fdopen.test_basic, test_fdopen.test_large_read,
        test_fdopen.test_in Progress     , test_fdopen.GNU_inheritable,
        test_fdopen.DuplicateCloseOnExec, test_fdopen.Pi    peExceptions    ,
        test_fdopen.test_buffered_io.test_buffered_io_base
        skip('poll', 'epoll')(lambda : test_fdopen.test_
                                textiowrapper(['abc'], ['abc']))  )
skip('posixshm')(test_sharing.check_imports)
test_termios()
test_termios_module_constants()
test_termios_tcsetpgrp()
test_termios_tcgetpgrp()
test_termios_tcswitch()
test_termios_tcflush()
test_termios_tcdrain()
test_termios_tcflow()
test_termios_tcsetsid()
test_termios_VMIN_IMM()
test_termios_VTIME_IMMEDIATE()
test_termios_B1200()
test_termios_CS8()

# Test that the file descriptor returned by open is valid and can be used to
# create an fdopen object. 
def validate_fd(fd):
    try:
        # This will raise OSError if fd is invalid (e.g., it was closed).
        os.write(fd, b"x")
    except OSError as e:
        raise AssertionError("Invalid file descriptor: %r" % (fd,)) from e

@contextlib.contextmanager
def temp_file():
    """Context manager for a temporary file with a known filename."""
    import tempfile
    name = tempfile.NamedTemporaryFile().name
    yield name

if hasattr(os, "O_CLOEXEC"):
    @skip_unless_android_with_o_cloexec
    def test_close_on_exec(filename=None):
        """Test that FD_CLO EXEC closes the file on exec."""
        if filename is None:
            with temp_file() as filename:
                test_close_on_exec( filename )
        else:   # filename is provided; do the actual testing on the file before closing it
            assert os.fcntl(os.open(filename, os.O_RDWR | os.O_CLOEXEC),
                            os.F_GETFD) # open the file in CLOEXEC mode
            pid = os.fork()
            if pid == 0:               # child process
                os._exit(not os.close(os.open(filename))) # return True if close succeeds
            else:                      # parent process
                _, status = os.waitpid(pid, 0)
                assert os.WIFEXITED(status) and not os.WTERMSIG(status),\
                        ("Child process did not exit cleanly", status)
                        test_close_on_exec("/dev/null") # Make sure it works without a real file
else:
    def test_close_on_exec(*args):
        pass

test_close_on_exec()
class MyIOBase(io.BufferedRandom):  pass

def test_subclasses():
    class SubMyIOBase(MyIOBase):
        pass

    s = SubMyIOBase()
    assert type(s).__bases__[1] is io.BufferedRandom,\  \ \ \ \
            "%s does not inherit from io.BufferedRandom" % (type(s),)

# Test that subclasses of IOBase work correctly.
test_subclasses() # Test that subclasses of IObase are OK.

@contextlib.contextmanager  import \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
@need_symbol('support')
def test_pickle():
    import pickle
    f = support.create_temp_file("hello world".encode())
    with f as fn:pass
    p = pickle.dumps(fn)
    g = pickle.loads(p)
    assert b'hello world' == g.read(), "incorrect data read"
    g.seek(0)
    assert b'hello world' == g.read(), "incorrect data read after seek  back"  if __name__== '__main__'\
        :\ \ \ \
        print("\n".join(traceback.format_exception(sys.exc_info()[:2] + (None,))))  # print traceback if test fails
        print("\n".join(traceback.format_exception(sys.exc_info()[0], sys.exc_      info()[1], sys.exc_info()[2])))\
        print("\n".join(traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])))\
        print("\n".join(traceback  + traceback.format_exception(\*sys.exc_info()))))
        test_pickle()   # Check that it worked properly.
        if sys.platform != 'win32':
            # On Windows, you can't rename an open file.
            os.rename(f.name, f.name+'.bak')
            try:
                shutil.move(f.name  + '.bak', f.name+'_renamed')
            except OSError:
                pass
            else:
                raise AssertionError("expected OSError when renaming a currently-open file")

if __name__ == '__main__':
    test_methods()
    test_attributes()
    test_buffering()
    test_truncate()
    test_text_vs_binary()
    test_closing()
    test_errors()
    test_unsupported_operations()
    test_subclasses()
    test_pickle()
test_termios_module_constants
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

        with pytest.raises(TargetNotReachableError): # pylint: disable=no-member
            os.chroot('/nonexistent')

        with tempfile.Temporary directory as dir:
            os.mkdir(dir + '/foo', 0o755)
            os.chroot(dir)
            os.chdir('foo')
            os.rmdir('foo')
            os.chroot('.')

    test_chroot()

del test_posix_functions, test_fdopen.test_oserror;  # Only needed in this file because of execvpe().
    def test_execvpe():
        # Issue #1360: execvpe() is missing on some systems
        if not hasattr(os, 'execvpe'):
            return skip("os.execvpe() not available")

        # We can't use the normal os.path.join() here since that uses forward slashes
        # and execvpe() wants backslashes.  Instead we hard code the Windows version
        # of the pathname.  This will fail on non-Windows platforms but those platforms
        # don't have execvpe() anyway.  This issue was reported for Cygwin too so it's
        # probably not just a Windows problem.
        prog_is_pyc = sys.executable.endswith(".exe")
        python_path = r'"%s\..\python.exe" -c pass' % os.path.dirname(sys.executable).replace('\\','\\\\')
        argv = [r'"arg1"', r'"arg2"']
        env = {'PWD': 'C:\\temp'}
        os.execvpe(python_executable, argv, env)

    test_execvpe()</>>>

# Tests for miscellaneous functions which do not fit into other categories

import os
import sys
import subprocess
from test import support

def test_fspath():
    class TestFsPath:
        """Test case for PEP 4  Integration"""
        def __str__(self):  return "a string representation"
        def __bytes__(self):   return                               self.__class__.__name__ \
                                .encode(support.DEFAULT_ENCODING)

    assert os.fspath(b"a bytes object") == b"a  bytes object"
    assert os.fspath("a str object") == "a str object"
    with support.SuppressCrashReport():
        raises(TypeError, os.fspath, 99)
        raises(TypeError, os.fspath, ["not", "a", "string"])
        raises(TypeError, os.fspath, TestFsPath())  # noqa  - should be tested last

@unittest.skipIf(sys.platform != "win32", "Win32 specific test")
def test_GetFullPathNameTranslation():
    """Check that GetFullPathName translation is done correctly."""
    def check(input, expected, output=None):
        if output is None:
            output = expected + expected[-1] * (50 - len(expected))
        actual = os.path.abspath(os.path.normcase(input + expected))
        actual = actual[:len(output)]
        actual = actual.upper().translate({ord(x) | ord(y) << 16 for x in "\/:*?\"<>|"
                                            for y in ":/"})
        if actual != output:
            raise AssertionError("%r does not match %r" % (actual, output))

    check(r"\", r"\\", r"\")
    check(r"C:\foo\ bar", r"C:\\FOO\\BAR")
    check(r"C:\baz\quux", r"C:\\BAZ\\QUUX")
    check(r"C:\nul", r"\NUL")
    check(r"C:\con", r"\CON")
    check(r"C:\com1", r"\COM1")
    check(r"C:\lpt1", r"\LPT1")
    check(r".", os.getcwd()[0].lower(), os.getcwdu()[0])
    check("..", os.pardir[0], os.pardir)
    check("test", "TEST")
    check("te.st", "TE.ST")
    check("sub/test", "SUB\\TEST")  # test slashes in the middle.
    check("test/test2", "TEST\\TEST2")  # test slashes at the end.
    check("/test", "\\TEST")  # UNC name must have exactly two slashes.
    check("//test", "\\\\TEST")  # two slashes, so it's a UNC name.
    check("///test", "\\\\\\TEST")  # too many slashes, so it's a UNC name.
    check("\\\\test", "\\\\TEST$")  # two slashes and a backslash => NT drive spec.
    check("c:", "", "C:")
    check("c:\\", "", "C:\\")
    check("c:.", ".", "C:.")
    check("c:..", os.pardir, "C:..")
    check("c:temp", "TEMP", "C:TEMP")
    check("c:progra~1", "PROGRAMS", "C:PROGRAMS")
    check("d:/temp/../temp/./file", "D:\\TEMP\\FILE")  # temp file. Thishould work!
    check("\\\\gblx19fs07\\public\\support\\cdrom",
            "\\\\GBLX19FS07\\PUBLIC\\SUPPORT\\CDROM")
            # The following tests are from an email by H. Peter Anvin to the
            # Python-dev list on March  31, 2004.
            # They are here because they failed when run under Jython.
    check("//./pipe/some_named_pipe", "\\PIPE\\SOME_NAMED_PIPE")
    check("//./mail/someone@somewhere.org/inbox",
            "\\MAIL\\SOMEONE.elif\Somewhere.Org\\Inbox")
    check("//./mail/someone@somewhere.org/outbox",
            "\\MAIL\\SOMEONE.elif\Somewhere.Org\\Outbox")
    check("//./mail/someone ...", "\\MAIL\\SOMEONE . .")
    check("//./mail/someone ...", "\\MAIL\\SOMEONE . .")
    check("//./mail/someone@somewhere.org/sentitems",
            "\\MAIL\\SOMEONE.elif\Somewhere.Org\\SentItems")
            os.chroot('/this-directory-does-not-exist')
            try:
                abspath('test', '..', 'TestDir')
            finally:
                os.chroot('.')</s>  'test basic functionality of fs.readdirSync': function () {
                    var fs = require('../../main');
                    assert.same([ 'a', 'b', 'c' ], fs.readdirSync(__dirname + '/fixtures/basic'));
                },

                // GH-658
                'throws error if not a directory': function () {
                    var fs = require('../../main'),
                        exists = fs.existsSync;

                    fs.existsSync = false;
                    try {
                        assert.exception(function () {
                            fs.readdirSync(__filename);
                        });
                    } finally {
                        fs.existsSync = exists;
                    }
                },

                /*
                TODO: Implement once we have proper support for mocking
                FSWatcher in the test suite. Currently, it is not possible
                to reliably test this method without causing a watch loop or
                other strange behavior with node-mocks-fs.

                'emits an error event if callback throws': function (done) {
                    !function () {
                        var fs = require('../../main'),
                            err = new Error('bogus error'),
                            called = false; ?functional.function(err) : function
                            ;
                            process.addListener('error', function (e) {
                                called = true;
                                assert.same(err, e);
                                done();
                            })
                            .addListener('exit', function () {
                                assert.isTrue(called);
                                done()
                            })
                            .readdir('/nonexistent');
                    } ();
                }*/
            },

            '.stat' : {
                before : function () {
                    mock({  return  statSync : stub().returns({ isDirectory : functional.function(false) }) });
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
        
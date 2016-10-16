import contextlib
import os
import sys
import tempfile
import subprocess
from urllib2 import urlopen, HTTPError, URLError

BASEURL = "http://free-electrons.com/~thomas/pub/buildroot-runtime-tests/"

@contextlib.contextmanager
def smart_open(filename=None):
    if filename and filename != '-':
        fhandle = open(filename, 'w+')
    else:
        fhandle = sys.stdout

    try:
        yield fhandle
    finally:
        if fhandle is not sys.stdout:
            fhandle.close()

def filepath(relpath):
    current_filepath = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_filepath)
    return os.path.join(current_dir, "support/testing", relpath)

def download(dldir, filename):
    finalpath = os.path.join(dldir, filename)
    if os.path.exists(finalpath):
        return finalpath

    if not os.path.exists(dldir):
        os.makedirs(dldir)

    tmpfile = tempfile.mktemp(dir=dldir)
    print "Downloading to {}".format(tmpfile)

    try:
        url_fh = urlopen(os.path.join(BASEURL, filename))
        with open(tmpfile, "w+") as tmpfile_fh:
            tmpfile_fh.write(url_fh.read())
    except (HTTPError, URLError), err:
        os.unlink(tmpfile)
        raise err

    print "Renaming from %s to %s" % (tmpfile, finalpath)
    os.rename(tmpfile, finalpath)
    return finalpath

def get_file_arch(builddir, prefix, fpath):
    cmd = ["host/usr/bin/{}-readelf".format(prefix),
           "-A", os.path.join("target", fpath)]
    out = subprocess.check_output(cmd, cwd=builddir, env={"LANG": "C"})
    for line in out.splitlines():
        line = line.strip()
        if not line.startswith("Tag_CPU_arch:"):
            continue
        return line.split(":")[1].strip()
    return None

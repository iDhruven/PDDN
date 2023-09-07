#!/usr/bin/env python3

import os
import subprocess
import resource
import sys

# Get the directory containing this script
script_dir = os.path.dirname(os.path.realpath(__file__))
app_home = os.path.abspath(script_dir)

app_name = "Gradle"
app_base_name = os.path.basename(__file__)

# Default JVM options
default_jvm_opts = ["-Xmx64m", "-Xms64m"]

# Check the maximum available file descriptors
if os.name != "nt":
    try:
        #max_fd_limit = os.get
        max_fd_limit = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
        if max_fd_limit != -1:
            max_fd = max_fd_limit
            resource.setrlimit(resource.RLIMIT_NOFILE, (max_fd, max_fd))
    except (ValueError, OSError):
        pass

# For Cygwin or MSYS, switch paths to Windows format before running java
if os.name == "posix":
    cygwin = False
    msys = False
    if os.path.exists("/cygdrive/") or os.path.exists("/usr/bin/mintty"):
        cygwin = True
    elif os.name == "nt" and os.getenv("MSYSTEM") is not None:
        msys = True

    if cygwin or msys:
        app_home = subprocess.check_output(["cygpath", "--path", "--mixed", app_home], universal_newlines=True).strip()
        classpath = subprocess.check_output(["cygpath", "--path", "--mixed", os.path.join(app_home, "gradle", "wrapper", "gradle-wrapper.jar")], universal_newlines=True).strip()
        jvm_cmd = subprocess.check_output(["cygpath", "--unix", "java"], universal_newlines=True).strip()
    else:
        classpath = os.path.join(app_home, "gradle", "wrapper", "gradle-wrapper.jar")
        jvm_cmd = "java"
else:
    classpath = os.path.join(app_home, "gradle", "wrapper", "gradle-wrapper.jar")
    jvm_cmd = "java"

# Set JVM options
java_opts = os.getenv("JAVA_OPTS", "")
gradle_opts = os.getenv("GRADLE_OPTS", "")
gradle_cygpattern = os.getenv("GRADLE_CYGPATTERN", "")

# For Darwin (macOS), add options to specify how the application appears in the dock
if sys.platform == "darwin":
    gradle_opts += " -Xdock:name=" + app_name + " -Xdock:icon=" + os.path.join(app_home, "media", "gradle.icns")

# Build the command
cmd = [jvm_cmd] + default_jvm_opts + java_opts.split() + gradle_opts.split() + ["-Dorg.gradle.appname=" + app_base_name] + ["-classpath", classpath] + ["org.gradle.wrapper.GradleWrapperMain"]

# Append command-line arguments to the command
cmd += sys.argv[1:]

# Execute the command
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError:
    sys.exit(1)

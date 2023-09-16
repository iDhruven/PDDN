#!/usr/bin/env python3

import os
import subprocess
import resource
import sys
import logging

# Get the directory containing this script
script_dir = os.path.dirname(os.path.realpath(__file__))
app_home = os.path.abspath(script_dir)

app_name = "Gradle"
app_base_name = os.path.basename(__file__)

# Default JVM options
default_jvm_opts = ["-Xmx64m", "-Xms64m"]

# Script is starting
logging.basicConfig(filename='gradle.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting Gradle wrapper script")

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

# Validate Gradle Wrapper
try:
    with open(os.path.join(app_home, "gradle", "wrapper", "gradle-wrapper.jar"), "rb") as f:
        f.read(1)
except FileNotFoundError or OSError:
    print("Error: The Gradle wrapper jar file is missing or not readable.")
    sys.exit(1)

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


# Add support for other Gradle options
gradle_cmd_options = []
for arg in sys.argv[1:]:
    if arg.startswith("--"):
        gradle_cmd_options.append(arg)
    else:
        break

# Build the command
cmd = [jvm_cmd] + default_jvm_opts + java_opts.split() + gradle_opts.split() + ["-Dorg.gradle.appname=" + app_base_name] + ["-classpath", classpath] + ["org.gradle.wrapper.GradleWrapperMain"]

# Append command-line arguments to the command
cmd += sys.argv[1:]

# Set local scope for the variables with Windows NT shell
if os.name == "nt":
    os.environ["DIRNAME"] = os.path.dirname(sys.argv[0])
    os.environ["APP_BASE_NAME"] = os.path.basename(sys.argv[0])
    os.environ["APP_HOME"] = app_home

# Execute the command
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError:
    print("Error: The Gradle build process failed.")
    sys.exit(1)

# Error and Exception Handling
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError as e:
    logging.error("Failed to execute Gradle wrapper: %s", e.stderr)
    print("Failed to execute Gradle wrapper. Please check the logs for more information.")
    sys.exit(1)
except Exception:
    logging.exception("Unexpected exception occurred:")
    print("An unexpected exception occurred. Please check the logs for more information.")
    sys.exit(1)


# Documentation
if "--help" in sys.argv or "-h" in sys.argv:
    print("Usage: gradlew.py [options] [tasks]\n")
    print("Options:")
    print("  --help, -h         Show this help message")
    print("  --version, -v      Display version information")
    print("\nRun Gradle builds with the provided options and tasks.")

# Exit with the same return code as the Gradle wrapper
#try:
#    exit_code = subprocess.check_output(cmd + ["--console=plain", "exitCode"], universal_newlines=True).strip()
#    sys.exit(exit_code)
#except subprocess.CalledProcessError:
#    print("Error: Unable to determine Gradle exit code.")
#    sys.exit(1)




# Select the proper sources at build time.
#
# NOTE: This DOES NOT work if `srcFilter` is set in `library.json`

Import("env")

want_module = False
want_ostream = False

for item in env.get("CPPDEFINES", []):
    if "FMT_MODULE" == item:
       want_module = True
    elif "FMT_OS" == item:
        want_ostream = True

src_filter = ["-<*>"]

if want_module:
    src_filter += ["+<fmt.cc>"]
else:
    src_filter += ["+<format.cc>"]

if want_ostream:
    src_filter += ["+<os.cc>"]


env.Replace(SRC_FILTER=src_filter)

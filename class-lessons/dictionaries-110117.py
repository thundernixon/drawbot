d = {}

print d

d = {"a": 123} # one "key-value pair". "a" is the key, and 123 is the value

d = {"a": 123, "b": 124}

print d
print len(d)
print d["b"]
print d.get("a")
print d.get("c")

d["d"] = "a new value"

print d

del d["d"]
print d

if "aaa" in d:
    print "yes"
else:
    print "no"
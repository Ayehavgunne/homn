from homn.shell import sh

# result = sh("cat /Users/ant/code/homn/dev_requirements.txt | grep isort")
result = sh(
    """
    cat /Users/ant/code/homn/dev_requirements.txt | grep sort
    cat /Users/ant/code/homn/MANIFEST.in
    ls -lta /
    """,
)
# result = sh("echo Hello from the other side!")
print("result.script")
print("----------")
print(f"{result.script}\n")
print("result.out")
print("----------")
print(f"{result.out}")
print("result.err")
print("----------")
print(f"{result.err}")
print("result.all")
print("----------")
print(f"{result.all}")
print("result.code")
print("----------")
print(f"{result.code}")
print("----------")

f1 = open("lend.txt")

try:
    f = open("highsco.txt")

# except Exception as e:
#     print(e)

except EOFError as e:
    print("eof error raise", e)

except IOError as a:
    print("IO error raise", a)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("important stuff")

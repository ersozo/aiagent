# from functions.write_file import write_file
from functions.run_python import run_python_file


def test():
    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print("Result for 'lorem.txt' file:")
    # print(result)
    # print("\n")

    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print("Result for 'pkg/morelorem.txt' file:")
    # print(result)
    # print("\n")

    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print("Result for '/tmp/temp.txt' file:")
    # print(result)
    # print("\n")
    print("run_python_file('calculator', 'main.py'):")
    print(run_python_file("calculator", "main.py"))
    print("\n")

    print("run_python_file('calculator', 'main.py', ['3 + 5']):")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("\n")

    print("run_python_file('calculator', 'tests.py'):")
    print(run_python_file("calculator", "tests.py"))
    print("\n")

    print("run_python_file('calculator', '../main.py') (should error):")
    print(run_python_file("calculator", "../main.py"))
    print("\n")

    print("run_python_file('calculator', 'nonexistent.py') (should error):")
    print(run_python_file("calculator", "nonexistent.py"))
    print("\n")



if __name__ == "__main__":
    print("Testing run_python_file function:")
    print("=" * 50)
    test()

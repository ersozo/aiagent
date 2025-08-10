from functions.get_files_info import get_files_info


def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("\n")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print("\n")

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print("\n")

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print("\n")


if __name__ == "__main__":
    print("Testing get_files_info function:")
    print("=" * 50)
    test()

from gendiff.compare import compare
from gendiff.parse import open_file, parse_args


def main(arg_list: list[str] | None = None) -> str:
    try:
        args = parse_args(arg_list)
    except Exception as e:
        print(e)
        exit(1)
    content1 = open_file(args.first_file)
    content2 = open_file(args.second_file)
    return compare(content1, content2)


def stdout_main():
    print(main())


if __name__ == "__main__":
    stdout_main()

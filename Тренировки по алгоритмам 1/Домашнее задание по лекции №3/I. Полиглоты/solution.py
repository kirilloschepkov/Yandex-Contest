def f(students) -> str:
    common_languages = set()
    common_languages.update(students[0])

    all_languages = set()
    for languages in students:
        common_languages.intersection_update(languages)
        all_languages.update(languages)

    print('\n'.join(map(str, [len(common_languages), *common_languages, len(all_languages), *all_languages])))


students_languages = [set([input() for _ in range(int(input()))]) for _ in range(int(input()))]
f(students_languages)

def find_repeated_substrings(s, min_length=2):
    """
    找出字符串中重复出现的子字符串及其出现次数
    :param s: 输入字符串
    :param min_length: 最小子串长度，默认为2
    :return: 字典{子串: 出现次数}
    """
    result = {}
    max_len = len(s) // 2  # 子串最大可能长度

    for length in range(min_length, max_len + 1):
        substrings = {}
        # 滑动窗口截取所有可能子串
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            substrings[substr] = substrings.get(substr, 0) + 1

        # 筛选当前长度下的重复子串
        for substr, count in substrings.items():
            if count > 1:
                if substr not in result:  # 避免短子串覆盖长子串
                    result[substr] = count

    return result


if __name__ == "__main__":
    test_str = "Hello,Welcome,My_life"
    repeated = find_repeated_substrings(test_str)

    if repeated:
        # 按示例格式输出第一个结果
        substr, count = next(iter(repeated.items()))
        print(f"{substr}:{count}")
    else:
        print("未找到重复子串")

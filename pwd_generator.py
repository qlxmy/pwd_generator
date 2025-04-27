def read_file_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # 只返回非空行
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"警告: 文件 {filename} 不存在")
        return []

def process_keywords(keywords):
    processed = []
    for keyword in keywords:
        # 只处理非空关键词
        if keyword:
            processed.append(keyword)
            processed.append(keyword.capitalize())
            processed.append(keyword.upper())
    return processed

def generate_passwords():
    # 读取所有文件
    keywords = read_file_lines('pwd/keyword.txt')
    connectors = read_file_lines('pwd/connectors.txt')
    weak_pwds = read_file_lines('pwd/weak_pwd.txt')
    
    # 生成结果
    results = []
    
    # 首先添加非空的weak_pwd内容
    results.extend([pwd for pwd in weak_pwds if pwd])
    
    # 处理关键词
    processed_keywords = process_keywords(keywords)
    
    # 直接连接（不使用连接符）
    for keyword in processed_keywords:
        for weak_pwd in weak_pwds:
            if keyword and weak_pwd:  # 确保关键词和弱密码都不为空
                results.append(f"{keyword}{weak_pwd}")
    
    # 使用连接符连接（如果connectors不为空）
    if connectors:
        for keyword in processed_keywords:
            for connector in connectors:
                for weak_pwd in weak_pwds:
                    if keyword and weak_pwd:  # 确保关键词和弱密码都不为空
                        results.append(f"{keyword}{connector}{weak_pwd}")
    
    # 写入结果文件（只写入非空结果）
    with open('pwd/results.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join([r for r in results if r]))

if __name__ == '__main__':
    generate_passwords()
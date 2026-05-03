import os
import re

def get_language_from_ext(filename):
    ext_map = {
        '.py': 'Python',
        '.cpp': 'C++',
        '.c': 'C',
        '.java': 'Java',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.go': 'Go',
        '.rs': 'Rust',
        '.cs': 'C#',
        '.rb': 'Ruby',
        '.swift': 'Swift',
        '.sql': 'SQL',
        '.sh': 'Bash'
    }
    _, ext = os.path.splitext(filename)
    return ext_map.get(ext.lower(), 'Unknown')

def format_problem_name(folder_name):
    # e.g. "0001-two-sum" -> "1", "Two Sum"
    match = re.match(r'^(\d+)-(.*)$', folder_name)
    if not match:
        return folder_name, folder_name
    
    num = str(int(match.group(1))) # remove leading zeros
    name = match.group(2).replace('-', ' ').title()
    return num, name

def build_index():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    leetcode_dir = os.path.join(repo_root, 'leetcode')
    readme_path = os.path.join(repo_root, 'README.md')
    
    if not os.path.exists(leetcode_dir):
        print("LeetCode directory not found!")
        return

    problems = []
    
    for folder in os.listdir(leetcode_dir):
        folder_path = os.path.join(leetcode_dir, folder)
        if os.path.isdir(folder_path):
            num, name = format_problem_name(folder)
            
            # Find the solution file
            languages = []
            for file in os.listdir(folder_path):
                if file.lower() != 'readme.md':
                    lang = get_language_from_ext(file)
                    if lang != 'Unknown' and lang not in languages:
                        languages.append(lang)
            
            lang_str = ", ".join(f"`{l}`" for l in languages) if languages else "`Text`"
            link = f"./leetcode/{folder}"
            
            # Store integer sorting key if possible
            try:
                sort_key = int(num)
            except ValueError:
                sort_key = 999999
                
            problems.append((sort_key, num, name, lang_str, link))
            
    # Sort by problem number
    problems.sort(key=lambda x: x[0])
    
    # Generate Markdown Table
    table_lines = [
        "| # | Problem | Language | Code |",
        "| :--- | :--- | :---: | :---: |"
    ]
    
    for _, num, name, lang_str, link in problems:
        table_lines.append(f"| {num} | {name} | {lang_str} | [View]({link}) |")
        
    new_index_content = "\\n".join(table_lines)
    
    # Update README.md
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
        
    start_tag = "<!-- INDEX_START -->"
    end_tag = "<!-- INDEX_END -->"
    
    pattern = re.compile(f"{start_tag}.*?{end_tag}", re.DOTALL)
    
    if pattern.search(readme_content):
        updated_content = pattern.sub(f"{start_tag}\\n{new_index_content}\\n{end_tag}", readme_content)
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated README index.")
    else:
        print("Could not find index tags in README.md.")

if __name__ == "__main__":
    build_index()

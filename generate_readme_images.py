import os

def generate_image_markdown(num_cols, root_dir):
    markdown = "|"
    for i in range(num_cols):
        markdown += "  |"
    markdown += "\n"
    images = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif"):
                images.append(os.path.join(dirpath, file))
    num_images = len(images)
    num_rows = num_images // num_cols
    if num_images % num_cols != 0:
        num_rows += 1
    markdown += "|"
    for i in range(num_cols):
        markdown += " ------- |"
    markdown += "\n"
    for i in range(num_rows):
        markdown += "|"
        for j in range(num_cols):
            index = i * num_cols + j
            if index < num_images:
                image = images[index]
                markdown += f" <img src='{image}' width='300' /> |"
            else:
                markdown += " |"
        markdown += "\n"
    return markdown

def list_dirs(root_dir):
    dirs = []
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            dirs.append(item_path)
    return dirs

if __name__ == "__main__":
    num_cols = 3
    root_dir = "./"
    # dirs = list_dirs(root_dir)
    markdown = generate_image_markdown(num_cols, root_dir)
    with open("test.md", "w") as f:
        f.write(f"# My Project\n\n")
        f.write(f"{markdown}")

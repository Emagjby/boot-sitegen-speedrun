import os
import shutil

from markdown_to_html import extract_title, markdown_to_html_node


def generate_page(
    from_path: str, template_path: str, dest_path: str, root: str
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as from_file:
        markdown = from_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    full = (
        template.replace("{{ Title }}", title)
        .replace("{{ Content }}", content)
        .replace('href="/', f'href="{root}')
        .replace('src="/', f'src="{root}')
    )

    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as dest_file:
        _ = dest_file.write(full)


def copy_static(src: str, dst: str) -> None:
    if os.path.exists(dst):
        shutil.rmtree(dst)

    os.mkdir(dst)

    copy_recursive(src, dst)


def copy_recursive(src: str, dst: str) -> None:
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            _ = shutil.copy2(src_path, dst_path)
        else:
            print(f"Creating directory: {dst_path}")
            os.makedirs(dst_path, exist_ok=True)
            copy_recursive(src_path, dst_path)


def generate_pages(
    dir_path_content: str, template_path: str, dest_dir_path: str, root: str = "/"
) -> None:
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dst_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(src_path) and src_path.endswith(".md"):
            print(f"Generating page: {src_path} -> {dst_path.replace('.md', '.html')}")
            generate_page(
                src_path, template_path, dst_path.replace(".md", ".html"), root
            )
        elif os.path.isdir(src_path):
            print(f"Processing directory: {src_path}")
            generate_pages(src_path, template_path, dst_path)


# main takes arg basepath
def main() -> None:
    base_path = os.getcwd()
    copy_static(os.path.join(base_path, "static"), os.path.join(base_path, "docs"))
    generate_pages(
        os.path.join(base_path, "content"),
        os.path.join(base_path, "template.html"),
        os.path.join(base_path, "docs"),
        root=base_path,
    )


if __name__ == "__main__":
    main()

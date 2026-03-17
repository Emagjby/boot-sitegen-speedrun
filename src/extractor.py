import re


def extract_markdown_images(image: str):
    image_pattern = r"!\[(.*?)\]\((.*?)\)"

    matches = re.findall(image_pattern, image)

    return matches


def extract_markdown_links(link: str):
    link_pattern = r"\[(.*?)\]\((.*?)\)"

    matches = re.findall(link_pattern, link)

    return matches

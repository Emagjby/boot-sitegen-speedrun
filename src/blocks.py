from enum import Enum


class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6


def block_to_block_type(block: str) -> BlockType:
    match block:
        case block if block.startswith("#"):
            return BlockType.HEADING
        case block if block.startswith("```"):
            return BlockType.CODE
        case block if block.startswith(">"):
            return BlockType.QUOTE
        case block if block.startswith("- "):
            return BlockType.UNORDERED_LIST
        case block if block.startswith(tuple(f"{i}. " for i in range(1, 10))):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH

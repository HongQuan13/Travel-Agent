from typing import List, Tuple
from xml.dom.minidom import Document


def format_docs(docs: List[Document]) -> Tuple[str, list]:
    links = []
    texts = []
    for doc in docs:
        link = doc.metadata.get("url", "")
        content = doc.page_content
        text = f"Webpage[{link}]\nContent: {content}"
        if link not in links:
            links.append(link)
        texts.append(text)
    return "\n\n".join(texts), links

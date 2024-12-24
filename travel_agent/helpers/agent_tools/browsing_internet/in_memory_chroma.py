import logging
import chromadb
import chromadb.config

from typing import List, Optional
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.src.constant.error_constant import ErrorDetail
from backend.src.constant.info_constant import InfoDetail


logger = logging.getLogger(__name__)

CHROMA_CLIENT_SETTINGS = {"is_persistent": False}
client_settings = chromadb.config.Settings(**CHROMA_CLIENT_SETTINGS)
client = chromadb.Client(client_settings)


class InMemeoryChroma:
    TOP_K = 20

    def __init__(self, is_persistent: bool, **kwargs):
        """
        is_persistent: If true, data in the same collection name will be persistent. Otherwise, the collection will be deleted on the destructor
        """
        self.is_persistent = is_persistent
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=400
        )
        self.db = Chroma(embedding_function=OpenAIEmbeddings(), client=client, **kwargs)
        logger.info(f"{InfoDetail.class_initialize('InMemeoryChroma')}")

    def add_embeddings(self, texts: List[str], metadatas: Optional[List[dict]] = None):
        texts = self.text_splitter.create_documents(texts, metadatas=metadatas)
        self.db.add_documents(texts)

    def retrieve_embeddings(self, query: str) -> list[Document]:
        retriever = self.db.as_retriever(search_kwargs={"k": self.TOP_K})
        return retriever.get_relevant_documents(query)

    def __del__(self):
        try:
            if self.is_persistent:
                self.db.delete_collection()
                logger.info(f"Collection {self.db._collection_name} deleted")
        except Exception as error:
            logger.error(f"{ErrorDetail.unknown('Deleting', error)}")

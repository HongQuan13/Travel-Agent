from langgraph.checkpoint.postgres import PostgresSaver
from langchain_core.messages import ToolMessage


class PostgresSaverWithLimit(PostgresSaver):
    def __init__(
        self, conn, pipe=None, serde=None, limit_checkpoint=2, limit_message=6
    ):
        super().__init__(conn, pipe, serde)
        self.limit_checkpoint = limit_checkpoint
        self.limit_message = limit_message

    def list(self, config, filter=None, before=None, limit=None):
        """List checkpoints from the database, limiting channel values to the latest 10 messages."""

        if limit is None:
            limit = self.limit_checkpoint

        checkpoints = super().list(config, filter=filter, before=before, limit=limit)

        for checkpoint in checkpoints:
            if "messages" in checkpoint.checkpoint["channel_values"]:
                checkpoint.checkpoint["channel_values"]["messages"] = (
                    self._handle_message_limit(
                        checkpoint.checkpoint["channel_values"]["messages"]
                    )
                )
            yield checkpoint

    def get_tuple(self, config):
        """Get a checkpoint tuple from the database, limiting channel values to the latest 10 messages."""

        checkpoint_tuple = super().get_tuple(config)

        if checkpoint_tuple:
            if "messages" in checkpoint_tuple.checkpoint["channel_values"]:
                checkpoint_tuple.checkpoint["channel_values"]["messages"] = (
                    self._handle_message_limit(
                        checkpoint_tuple.checkpoint["channel_values"]["messages"]
                    )
                )

        return checkpoint_tuple

    def _handle_message_limit(self, checkpoint_message):
        if len(checkpoint_message) < self.limit_message:
            return checkpoint_message

        first_message = checkpoint_message[-self.limit_message]

        if isinstance(first_message, ToolMessage):
            self.limit_message += 1

        return checkpoint_message[-self.limit_message :]

from langgraph.checkpoint.postgres import PostgresSaver


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
                    checkpoint.checkpoint["channel_values"]["messages"][
                        -self.limit_message :
                    ]
                )
            yield checkpoint

    def put(self, config, checkpoint, metadata, new_versions):
        channel_values = checkpoint.get("channel_values", {})

        if "messages" in channel_values:
            channel_values["messages"] = channel_values["messages"][
                -self.limit_message :
            ]

        checkpoint["channel_values"] = channel_values

        return super().put(config, checkpoint, metadata, new_versions)

    def get_tuple(self, config):
        """Get a checkpoint tuple from the database, limiting channel values to the latest 10 messages."""

        # Call the parent class's get_tuple method to retrieve the checkpoint
        checkpoint_tuple = super().get_tuple(config)

        if checkpoint_tuple:
            if "messages" in checkpoint_tuple.checkpoint["channel_values"]:
                checkpoint_tuple.checkpoint["channel_values"]["messages"] = (
                    checkpoint_tuple.checkpoint["channel_values"]["messages"][
                        -self.limit_message :
                    ]
                )

        return checkpoint_tuple

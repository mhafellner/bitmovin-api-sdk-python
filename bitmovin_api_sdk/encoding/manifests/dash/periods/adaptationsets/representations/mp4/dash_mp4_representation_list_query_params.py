class DashMp4RepresentationListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(DashMp4RepresentationListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
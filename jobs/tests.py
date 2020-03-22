from utils.data_ingest import is_duplicate

# TODO - tests rely on db seeding we might want to avoid in prod.
# See if there is a way we can seed here?

# TODO - getting all sorts of import errors trying to run these. Will figure out something else soon.

assert is_duplicate('0000000000')

assert not is_duplicate('0000044000')
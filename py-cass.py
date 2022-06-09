import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cassserv0 = str(os.getenv("CASS_SERVER0"))

auth_prov0 = PlainTextAuthProvider(username='pds', password='pass')
cluster = Cluster([cassserv0, cassserv1], auth_provider=auth_prov0)
session = cluster.connect()

import MySQLdb
from spasm.data.config import CONFIG

FIELDS = ['name','slug','country','ambiguous','website_url','myspace_url','twitter_url','facebook_url','youtube_url']

# Dump artists to CSV

conn = MySQLdb.connect(**CONFIG)
cursor = conn.cursor()

query = "SELECT %s FROM artists ORDER BY %s" % (','.join(FIELDS), "name")
result = cursor.execute(query)
artists = cursor.fetchall()

f = open('artists.csv','w')
f.write("name, slug, country, ambiguous, website_url, myspace_url, twitter_url, facebook_url, youtube_url\n")

for artist in artists:
    line = "%s\n" % ",".join([str(c) for c in artist])
    f.write(line)

f.close()
cursor.close()
conn.close()


# Import artists from CSV

conn = MySQLdb.connect(**CONFIG)
cursor = conn.cursor()

f = open('artists.csv','r')
lines = f.readlines()
for line in lines[1:]:
    data = [field.strip() for field in line.split(",")]
    fields = ["'%s'" % value.replace("'","\\'") if value != "None" else "null" for value in data]
    query = "INSERT INTO artists (%s) VALUES (%s)" % (",".join(FIELDS), ",".join(fields))
    cursor.execute(query)

f.close()
cursor.close()
conn.close()





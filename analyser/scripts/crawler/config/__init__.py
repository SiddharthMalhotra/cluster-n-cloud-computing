class Keys:
    """
        CONSUMER_KEY
        CONSUMER_SEC
        ACCESS_TOKEN
        ACCESS_SEC
    """

    def __init__(self, ckey, csec, atoken, asec):
        self.ckey = ckey
        self.csec = csec
        self.atoken = atoken
        self.asec = asec



# couchdb
db_name = 'tweets'
aurin_db_name = 'aurin'
db_admin = 'admin'
db_password = 'admin'
couchdb_uri = "http://fred:admin@127.0.0.1:5984"      # couchdb address


# twitter api
app_auth = {
    'jiyu': Keys(
        "iVJhaBM8SLCi5tXy8055jZgor",
        "Iaqwf1819wWMj8Xrt9qk129KZBBQUs7wckOXQs2gprxIl59GdU",
        "985778410898124800-84JVlrPgFenZGbiBoGeMjyzzNP90gQA",
        "XWoTuCqnuIPrHlC4LHlsu5f10wTtmQyo2PZfbq3e7bPBe"
    ),
    'siddharth':Keys(
        "bXsWEKkTUgKXENxyxfT7O0BTy",
        "Y0ZAXr2GPVZFN3hBCsiuPBqppNUavDO7IlT9XZLkg3y4bJluPU",
        "179173817-gQOMylVUcfprD6xHtJxWZO6sL6GdVrSyxdMGZffL",
        "5qrgPwUuTBB35W2KqnodwFpspdzWp3KpFs64HOc3o5yEZ"
    ),
    'vedant':Keys(
        "ot4fXr9x3Nf0f94FUomFPieNH",
        "x72WSDCWbF6EMsLViRp7gm1gKOnKK6HHG6xTk9zUKtlKrPrQc5",
        "991571553073512448-mV5XDtoor6bpjH09lk1NNzn4GyMYMmW",
        "UgqA6EfQzUugyhXSiPN0Sy6fARkiDGZR9ezirjiBw3H1G"
    )
    # add other users access info here n change in harvestMode.py as well
}


# geo box
MELBOURNE_STR = [144.6550006954,-38.5089967291,145.3498310249,-37.5916213868]  #http://boundingbox.klokantech.com
SYD_STR = [150.9786666445,-34.0173030936,151.3082564883,-33.7048428499]
BRIS_STR = [152.6685227,-27.7674409,153.3178702,-26.9968449]
HOB_STR = [147.258116931,-42.9114151424,147.406089038,-42.8136762823]
PER_STR = [115.7254058567,-32.2451119056,116.0247832981,-31.7629843588]
CAN_STR = [149.0042298676,-35.3401387783,149.2150300385,-35.1584565418]
DAR_STR = [130.8138784401,-12.4830398481,130.9553274147,-12.3609959658]
ADE_STR = [138.4733842067,-35.0853926738,138.7219498806,-34.7554676739]

AUS_STR = MELBOURNE_STR+SYD_STR+BRIS_STR+HOB_STR+PER_STR+CAN_STR+DAR_STR+ADE_STR

           
# topics
smoke_file = "../scripts/crawler/topic_glossary/smoke_alcohol.txt"
crime_file = "../scripts/crawler/topic_glossary/crime.txt"
cricket_file = "../scripts/crawler/topic_glossary/cricket.txt"
afl_file = "../scripts/crawler/topic_glossary/afl.txt"


from harvestMode import HarvestSys




def run_crawler(crawler):
    try:
        crawler.StreamMode()
    except:
        #crawler.StreamMode()
        crawler.SearchMode()



if __name__ == '__main__':
    crawler = HarvestSys()
    run_crawler(crawler)
